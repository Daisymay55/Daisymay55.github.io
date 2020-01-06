# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:31:14 2019

@author: Lucy Ewers
"""
import folium
from folium import plugins
import pandas
import string
import json
#import leaflet
#import legend
from branca.element import Template, MacroElement


#creates basemap - tiles determines the basemap design (stamen chosen as it shows terrain rather than openstreetmap) - 1.5 zoom shows whole world. 
    #N.B. depending on monitor size 1.5 zoom can cause a grey bar at top of page but increasing zoom doesnt show world view on smaller monitors (too zoomed in).
map = folium.Map(location=[42,-30],zoom_start=1.5, tiles ='stamen terrain',control_scale= True)

# Adds a search box so the user can search for earthquake events by county
    # N.B. Had search box working but then it stopped functioning, left code in in case future user could fix issue or it began to work again.
#map.add_child(folium.plugins.Search(fgp,search_label = 'name_sort', search_zoom = 8, placeholder='Search by Country'))

# Adds draw functionality for users so they can highlight features of interest and measure distances

map.add_child(folium.plugins.Draw(filename='Countries.json'))

# enables advanced measuring options with different base units

map.add_child(folium.plugins.MeasureControl(position='topleft'))

# Adds a fullscreen option

map.add_child(folium.plugins.Fullscreen(position='topright'))

# Adds minimap to the bottom left so the user always knows their location relative to the world map
    #N.B. minimap is disabled due to amount of map furniture but code is left in so user can reactivate if desired

''''map.add_child(folium.plugins.MiniMap(position='bottomleft'))'''

# Shows earthquake layer as a heatmap so earthquake clusters can be easily recognised.
    #N.B. only shows the 100 largest earthquakes (by magnitude) to reduce file size & load time.

data = pandas.read_csv('Earthquakes_100.csv')
lat = list(data['latitude'])
long = list(data['longitude'])

for lat,long in zip(lat,long):
    coordinates = lat,long
       
    #print(coordinates)
    map.add_child(folium.plugins.HeatMap([coordinates], name='Earthquake Heatmap',radius = 20, blur = 5, gradient={0.3: "blue", 0.5: 'lime', 0.8: 'red'}))


#adds legend to the bottom right of the page
    # modified from script by: https://nbviewer.jupyter.org/gist/talbertc-usgs/18f8901fc98f109f2b71156cf3ac81cd 
'''template = """
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
            
map.get_root().add_child(macro)'''


#adds layer toggle controls
map.add_child(folium.LayerControl()) 

#saves the map to html webpage
map.save('Earthquake_Heatmap.html')

