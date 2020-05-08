# Module for get distance between points A and B
# MapBox Api https://docs.mapbox.com/api/

import requests
import json
# pip install xlrd >=1.1


class GetDistanceMapBox:
    """Get distance between points A and B"""

    token = ''  # MapBox Token

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def get_coordinates_mapbox(self, get_point):
        """Get coordinates: [longitude{longitude}, latitude{latitude}], ex, 38.05,41.06"""
        point = str(get_point)
        r = requests.get(
            f'https://api.mapbox.com/geocoding/v5/mapbox.places/{point}.json?limit=2&access_token={self.token}').text
        geo_point = json.loads(r)
        return str(geo_point['features'][0]['geometry']['coordinates'])[1:-1].replace(' ', '')

    def distance_mapbox(self):
        """Get distance measured in km"""
        point1 = self.get_coordinates_mapbox(self.point_a)
        point2 = self.get_coordinates_mapbox(self.point_b)
        profile = 'driving-traffic'
        '''Options:
        - driving-traffic - Historical traffic conditions to avoid slowdowns
        - driving - The fastest routes, preferring express roads such as highways
        - walking - Shows the shortest path using sidewalks and trails
        - cycling - Shows routes that are shorter and safer for cyclists'''
        r = requests.get(
            f'https://api.mapbox.com/directions/v5/mapbox/{profile}/{point1};{point2}?access_token={self.token}').text
        output = json.loads(r)
        return int(output['routes'][0]['distance']) // 1000
