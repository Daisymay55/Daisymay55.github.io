# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:31:14 2019

@author: Lucy Ewers
"""
import folium
from folium import plugins
import pandas
import string
#import leaflet
#import legend
from branca.element import Template, MacroElement


#creates basemap - tiles determines the basemap design (stamen chosen as it shows terrain rather than openstreetmap) - 1.5 zoom shows whole world. 
    #N.B. depending on monitor size 1.5 zoom can cause a grey bar at top of page but increasing zoom doesnt show world view on smaller monitors (too zoomed in).
map = folium.Map(location=[42,-30],zoom_start=1.5, tiles ='stamen terrain',control_scale= True)

# feature groups determine what is displayed on map and which layers can be turned on/off
    # one FG for each earthquake magnitude allows the different mags to be turned on/off independantly dependant on user interests
fge6 = folium.FeatureGroup(name='Mag 6-6.9 Earthquakes')
fge7 = folium.FeatureGroup(name='Mag 7-7.9 Earthquakes')
fge8 = folium.FeatureGroup(name='Mag 8-8.9 Earthquakes')
fge9 = folium.FeatureGroup(name='Over Mag 9 Earthquakes')
fgp = folium.FeatureGroup(name='Population')

#colour scheme for population polygons - green for populations less than 10million, orange for between 10m-20m and red for populations over 20million
    #N.B. population geojson from (https://geojson-maps.ash.ms/) - population estimates are based on countries last census so dates of estimates vary (typically 2010). 
def pop_style(x):
    return {'fillColor':'green' if x['properties']['pop_est']<=10000000 else 'orange' if 10000000 < x['properties']['pop_est'] < 20000000 else 'red'}
   
#adds country population polygons - overlays basemap with country polygons colour coded by population size. A transparency has been applied to allow the basemap to be visable.
fgp.add_child(folium.GeoJson(data=open('Countries.json','r',encoding='utf-8-sig').read(),style_function = pop_style))


'''adds earthquake data to script - earthquake data sourced from the USGS website (https://earthquake.usgs.gov/earthquakes/search/) 
- contains the 2000 largest earthquakes from 01/01/1900 - 01/01/2020'''
data = pandas.read_csv('Earthquakes2020.csv')

#marker attributes - lists the attributes that will be included on the marker points

lat = list(data['latitude'])
long = list(data['longitude'])
name = list(data['place'])
mag = list(data['mag'])
date = list(data['time'])


# colour codes markers by magnitude

def colour_key(mag):
    if mag <= 6.9:
        return 'beige'
    elif mag <= 7.9:
        return 'orange'
    elif mag <=8.9:
        return 'red'
    else:
        return 'black'

#adds markers to map - transparency has been applied so overlapping markers can all be seen, when clicked a pop-up with additional information will load.
    #N.B. has to be written as color, not colour.
    #N.B. the first letter of each word in the location name has been capitlised, for mag 7-7.9 earthquakes 'name' had to be converted to string first as it was reading as a float.
for lat,long,name,date,mag in zip(lat,long,name,date,mag):
   if mag <= 6.9:
        fge6.add_child(folium.CircleMarker(location=[lat,long], radius =6, popup=(string.capwords(name),str(date[:10]),str(mag)),
    fill_color=colour_key(mag), color ='grey', fill_opacity =0.75))
   elif mag <= 7.9:
        fge7.add_child(folium.CircleMarker(location=[lat,long], radius =6, popup=((string.capwords(str(name))),str(date[:10]),str(mag)),
    fill_color=colour_key(mag), color ='grey', fill_opacity =0.75))
   elif mag <=8.9:
        fge8.add_child(folium.CircleMarker(location=[lat,long], radius =6, popup=(string.capwords(name),str(date[:10]),str(mag)),
    fill_color=colour_key(mag), color ='grey', fill_opacity =0.75))
   else:
        fge9.add_child(folium.CircleMarker(location=[lat,long], radius =6, popup=(string.capwords(name),str(date[:10]),str(mag)),
    fill_color=colour_key(mag), color ='grey', fill_opacity =0.75))


# Adds a search box so the user can search for earthquake events by county
    # N.B. Had search box working but then it stopped functioning, left code in in case future user could fix issue or it began to work again.
map.add_child(folium.plugins.Search(fgp,search_label = 'name_sort', search_zoom = 8, placeholder='Search by Country'))

# Adds draw functionality for users so they can highlight features of interest and measure distances

map.add_child(folium.plugins.Draw(filename='Countries.json'))

# enables advanced measuring options with different base units

map.add_child(folium.plugins.MeasureControl(position='topleft'))

# Adds a fullscreen option

map.add_child(folium.plugins.Fullscreen(position='topright'))

# Adds minimap to the bottom left so the user always knows their location relative to the world map
    #N.B. minimap is disabled due to amount of map furniture but code is left in so user can reactivate if desired

'''map.add_child(folium.plugins.MiniMap(position='bottomleft'))'''

# Shows earthquake layer as a heatmap so earthquake clusters can be easily recognised.

data = pandas.read_csv('Earthquakes2020.csv')
lat = list(data['latitude'])
long = list(data['longitude'])

for lat,long in zip(lat,long):
    coordinates = lat,long
       
    #print(coordinates)

    map.add_child(folium.plugins.HeatMap([coordinates], name='Earthquake Heatmap',show=False))

#adds legend to the bottom right of the page
    # modified from script by: https://nbviewer.jupyter.org/gist/talbertc-usgs/18f8901fc98f109f2b71156cf3ac81cd 
template = """
        {% macro html(this, kwargs) %}
        
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Earthquake Map</title>
          <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
        
          <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
          <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
          
          <script>
          $( function() {
            $( "#maplegend" ).fixed({
                            start: function (event, ui) {
                                $(this).css({
                                    right: "200px",
                                    top: "50px",
                                    bottom: "auto"
                                });
                            }
                        });
        });
        
          </script>
        </head>
        <body>
        
         
        <div id='maplegend' class='maplegend' 
            style='position: fixed; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
             border-radius:5px; padding: 5px; font-size:14px; right: 20px; bottom: 20px;'>
             
        <div class='legend-title'>Earthquake Magnitude</div>
        <div class='legend-scale'>
          <ul class='legend-labels'>
            <li><span style='background:black;opacity:0.7;'></span>Over 9.0</li>
            <li><span style='background:red;opacity:0.7;'></span>8.0-8.9</li>
            <li><span style='background:orange;opacity:0.7;'></span>7.0-7.9</li>
            <li><span style='background:beige;opacity:0.7;'></span>6.0-6.9</li>
            
        <div class='legend-title'>Population</div>
        <div class='legend-scale'>
          <ul class='legend-labels'>
            <li><span style='background:red;opacity:0.7;'></span>Over 20 Million </li>
            <li><span style='background:orange;opacity:0.7;'></span>10 Million to 20 Million</li>
            <li><span style='background:lightgreen;opacity:0.7;'></span>Less than 10 Million</li>
        
          </ul>
        </div>
        </div>
         
        </body>
        </html>
        
        <style type='text/css'>
          .maplegend .legend-title {
            text-align: left;
            margin-bottom: 5px;
            font-weight: bold;
            font-size: 90%;
            }
          .maplegend .legend-scale ul {
            margin: 0;
            margin-bottom: 5px;
            padding: 0;
            float: left;
            list-style: none;
            }
          .maplegend .legend-scale ul li {
            font-size: 80%;
            list-style: none;
            margin-left: 0;
            line-height: 18px;
            margin-bottom: 2px;
            }
          .maplegend ul.legend-labels li span {
            display: block;
            float: left;
            height: 16px;
            width: 30px;
            margin-right: 5px;
            margin-left: 0;
            border: 1px solid #999;
            }
          .maplegend .legend-source {
            font-size: 80%;
            color: #777;
            clear: both;
            }
          .maplegend a {
            color: #777;
            }
        </style>
        {% endmacro %}"""
       
macro = MacroElement()
macro._template = Template(template)
            
map.get_root().add_child(macro)

    
   
#adds feature groups to the map       
map.add_child(fgp)
map.add_child(fge6)
map.add_child(fge7)
map.add_child(fge8)
map.add_child(fge9)

#adds layer toggle controls
map.add_child(folium.LayerControl()) 

#saves the map to html webpage
map.save('Earthquake_Distribution.html')

