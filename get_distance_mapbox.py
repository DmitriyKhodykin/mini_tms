# Модуль для получения расстояния между пунктами А и Б в км
# На основании бесплатного сервиса mapbox, api https://docs.mapbox.com/api/

import requests
import json
# pip install xlrd >=1.1

token = '' # Для получения - требуется зарегистрироваться на mapbox


def get_distance_mapbox(pointA, pointB):
    def get_coordinates_mapbox(get_point):
        '''Возвращает координаты в формате: [Долгота{longitude}, Широта{latitude}], например, 38.05,41.06'''
        point = str(get_point)
        r = requests.get(
            f'https://api.mapbox.com/geocoding/v5/mapbox.places/{point}.json?limit=2&access_token={token}').text
        geo_point = json.loads(r)
        return str(geo_point['features'][0]['geometry']['coordinates'])[1:-1].replace(' ', '')


    def distance_mapbox():
        '''Возвращает расстояние в киллометрах между пунктами А и Б'''
        point1 = get_coordinates_mapbox(pointA)
        point2 = get_coordinates_mapbox(pointB)
        profile = 'driving-traffic'
        '''Опции:
        - driving-traffic - Этот профиль учитывает текущие и исторические условия движения, чтобы избежать замедлений
        - driving - Этот профиль показывает самые быстрые маршруты, предпочитая скоростные дороги, такие как шоссе
        - walking - Этот профиль показывает кратчайший путь с использованием тротуаров и троп
        - cycling - Этот профиль показывает маршруты, которые являются короткими и более безопасными для велосипедистов'''
        r = requests.get(
            f'https://api.mapbox.com/directions/v5/mapbox/{profile}/{point1};{point2}?access_token={token}').text
        output = json.loads(r)
        return int(output['routes'][0]['distance']) // 1000
    return distance_mapbox()

print(get_distance_mapbox('Москва Россия', 'Воронеж Россия'))
