# Модуль для получения расстояния между пунктами А и Б в км
# На основании бесплатного сервиса mapbox, api https://docs.mapbox.com/api/

import requests
import json
import pandas as pd
# pip install xlrd >=1.1

token = '' # для получения - требуется зарегистрироваться на mapbox

def get_coordinates(get_point):
    '''Возвращает координаты в формате: [Долгота{longitude}, Широта{latitude}], например, 38.05,41.06'''
    point = str(get_point)
    r = requests.get(
        f'https://api.mapbox.com/geocoding/v5/mapbox.places/{point}.json?limit=2&access_token={token}').text
    geo_point = json.loads(r)
    return str(geo_point['features'][0]['geometry']['coordinates'])[1:-1].replace(' ', '')
    
def distance(pointA, pointB):
    '''Возвращает расстояние в киллометрах между пунктами А и Б'''
    point1 = get_coordinates(pointA)
    point2 = get_coordinates(pointB)
    profile = 'driving-traffic'
    r = requests.get(
        f'https://api.mapbox.com/directions/v5/mapbox/{profile}/{point1};{point2}?access_token={token}').text
    output = json.loads(r)
    return int(output['routes'][0]['distance']) // 1000
    
    print(distance('Москва Россия', 'Воронеж Россия'))
