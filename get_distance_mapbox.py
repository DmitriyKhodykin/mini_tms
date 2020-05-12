# Модуль для получения расстояния между пунктами А и Б
# по данным бесплатного сервиса MapBox
# Api https://docs.mapbox.com/api/

import requests
import json
# pip install xlrd >=1.1


class GetDistanceMapBox:
    """GetDistanceMapBox(point_a, point_b)
    - point_a - отправная точка,
    - point_b - точка доставки"""

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
        """Получение расстояния между пунктами А и Б в км"""
        point1 = self.get_coordinates_mapbox(self.point_a)
        point2 = self.get_coordinates_mapbox(self.point_b)
        profile = 'driving-traffic'
        # Опции метода:
        # - driving-traffic - Исторический трафик для автомобиля
        # - driving - Самый быстрый путь для автомобиля
        # - walking - Пешеходный маршрут
        # - cycling - Веломаршрут
        r = requests.get(
            f'https://api.mapbox.com/directions/v5/mapbox/{profile}/{point1};{point2}?access_token={self.token}').text
        output = json.loads(r)
        return int(output['routes'][0]['distance']) // 1000
