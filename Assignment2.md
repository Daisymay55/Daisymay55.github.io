*Assignment 2 - Earthquake Mapping*

*Assignment Details*

For this module I created an earthquake map which shows the 2000 largest earthquakes by magnitude, from 01/01/1900 to 01/01/2020, for across the globe. 

The earthquakes are colour coded by magnitude and range from Magnitude 6.0 upwards.
Each earthquake marker is clickable to show additional information as a pop-up, the markers have also been set with a transparency so any overlapping points can be seen. 

The original earthquake file needed amendments in order to style the pop-ups. A selection of information was taken from the earthquake file as not all the data needed to be displayed. It was decided to show the location name, date and magnitude of the earthquakes. The location name had the first letter of each word capitlised in order to make it more aesthetically pleasing. The date field had the time aspect removed as it was deemed unnecessary to show the precise seconds of an earthquake that occured a century ago, I would have liked to of reordered the date field so it read day-month-year rather than year-day-month however I was unable to achieve this. Finally the precise magnitude was included as it was deemed useful for the user to know the exact magnitude of each earthquake after they had chosen a magnitude range that was of interest to them. 

The map also contains a terrain baselayer and a population overlay which shows each country colour coded by population. It was decided it may be useful to include the population for each country as this could be used in combination with the earthquake data to gauge the risk to each country. 

The map is designed so that each layer can be turned on/off indivdually so the map output can be tailored to the users needs. 

With regards to map furniture, a scale bar, legend, fullscreen option, search bar, layer toggles and editing tools have been added. These tools are designed to aid user understanding and interaction with the map. The legend was adapted from another persons code and it was made fixed in the bottom right corner rather than moveable as the original version was. It was decided to make it a fixed object as I did not want to have too many moving items obscuring map details. When the search bar was added it searched by country from the GeoJson layer which allowed the user to navigate to a particular country with ease. It has since stopped working despite the code not being changed however I have left it on the map with the hopes that it may start working again, or that another user may be able to fix it. The editing tools were added so the user could customise their outputs and measure the distances between earthquakes or locations with ease.

*Suggested Improvements*

I would have liked to get the search bar functioning again during this project and it is hoped that another user may be able to fix it. 

It was attempted to add a print from browser functionality using the *leafet.browser.print* option however upon investigation into this tool it is part of the *leaflet* package which runs with JavaScript and is not yet adapted for Python. 
Most of the map features were made using *folium* which is a Python version of the *leaflet* package however print & export functions have not yet been added to *folium*. This was an oversight on my part when I began this project as I am unable to add a print/export function to the map. However the user can still use the standard print from webpage options given by all browsers. If and when a broswer print option is added to *folium* I would like to add it to the map to increase user functionality. 

*The Code & The Earthquake Map*

Please click here the source code

Please click here for the Earthquake Map

Please click here for the UML Diagram

For assistance please refer to the [readme](https://daisymay55.github.io/as2readme.html) file.

[Return to Home](https://daisymay55.github.io/home.html)
