import os
import sys
import json
import math

FILE_PATH = 'bars.json'
LONGITUDE = 37.683185
LATITUDE = 55.740071


def load_data(filepath):
    if os.path.exists(filepath):
        with open(file=filepath, mode='r') as datafile:
            return json.load(datafile)
    else:
        raise FileNotFoundError


def get_biggest_bar(data):
    return max(data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    return min(data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    return min(data['features'],
               key=lambda x: math.hypot(x['geometry']['coordinates'][0] - longitude,
                                        x['geometry']['coordinates'][1] - latitude))


if __name__ == '__main__':
    try:
        all_bars = load_data(FILE_PATH)
        biggest_bar_attributes = get_biggest_bar(all_bars)['properties']['Attributes']
        print('Самый большой бар на {seats} мест: {name} по адресу {address}'.format(
            seats=biggest_bar_attributes['SeatsCount'],
            name=biggest_bar_attributes['Name'],
            address=biggest_bar_attributes['Address']
        ))
        smallest_bar_attributes = get_smallest_bar(all_bars)['properties']['Attributes']
        print('Самый маленький бар на {seats} мест: {name} по адресу {address}'.format(
            seats=smallest_bar_attributes['SeatsCount'],
            name=smallest_bar_attributes['Name'],
            address=smallest_bar_attributes['Address']
        ))
        closest_bar_attributes = \
            get_closest_bar(all_bars, LONGITUDE, LATITUDE)['properties']['Attributes']
        print('Самый близкий бар: {name} по адресу {address}'.format(
            name=closest_bar_attributes['Name'],
            address=closest_bar_attributes['Address']
        ))
    except FileNotFoundError:
        sys.exit('File with data is missed!')
