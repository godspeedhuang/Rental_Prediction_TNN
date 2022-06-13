import folium
from dash import html
import json

def get_data(villname):
    with open('vill.geojson',mode='r',encoding='utf-8') as file:
        data=json.load(file)
    for i in data['features']:
        if i['properties']['VILLNAME']==villname:
            vill=i
    return vill


def make_map(villname):
    map=folium.Map(
        location=(22.99717028569345, 120.21292880134021),
        zoom_start=13,
        tiles='CartoDB positron',
        control_scale=True
    )
    
    data=get_data(villname)

    folium.GeoJson(
        data,
        # tooltip=folium.GeoJsonTooltip(fields=['COUNTYNAME'],aliases=['市名'])
    ).add_to(map)
    map.fit_bounds(map.get_bounds(),padding=(100,100))
    map.save('map_test.html')
    return html.Div(
        className='map-container',
        children=[
            html.Iframe(srcDoc=open('map_test.html','r',encoding='utf-8').read(),width='100%',height=750),
        ]
    )

    