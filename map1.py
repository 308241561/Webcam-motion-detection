import folium
import pandas

data = pandas.read_csv("/Users/xingguohuang/Documents/app2/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if(elevation < 1000):
        return "green"
    elif(1000 <= elevation < 1500):
        return "orange"
    elif(1500 <= elevation < 2000):
        return "purple"
    elif(2000 <= elevation < 2500):
        return "red"    
    else:
        return "darkred"



map = folium.Map(location = [47.245518, -122.433743], zoom_start= 4, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup=folium.Popup(iframe), 
    fill_color = color_producer(el), color = "white", fill = True, fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("/Users/xingguohuang/Documents/app2/world.json","r", encoding="utf-8-sig").read(), 
style_function= lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 
else "pink" if 20000000 <= x["properties"]["POP2005"] < 30000000 
else "blue" if 30000000 <= x["properties"]["POP2005"] < 40000000
else "black" if 40000000 <= x["properties"]["POP2005"] < 50000000
else "brown" if 50000000 <= x["properties"]["POP2005"] < 60000000
else "silver" if 60000000 <= x["properties"]["POP2005"] < 70000000
else "olive" if 70000000 <= x["properties"]["POP2005"] < 80000000
else "red" if 90000000 <= x["properties"]["POP2005"] < 100000000 
else "darkred"
}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl() )
map.save("/Users/xingguohuang/Documents/app2/Map1.html")

