import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
map=folium.Map(location=[38.5,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")


def color_produce(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'darkred'
    else:
        return 'pink'
for lt,ln,el in zip(lat,lon,elev):

    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6,popup=str(el)+"m",fill_color=color_produce(el),color='black',fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda a:{'fillColor':'yellow'}))
map.add_child(fg)
map.save("Map1.html")
