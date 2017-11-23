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


def print_bar_info(kind_of_bar, bar_representation):
    print('Самый {kind} бар на {seats} мест: {name} по адресу {address}'.format(
        kind=kind_of_bar,
        seats=bar_representation['properties']['Attributes']['SeatsCount'],
        name=bar_representation['properties']['Attributes']['Name'],
        address=bar_representation['properties']['Attributes']['Address'],
    ))


if __name__ == '__main__':
    try:
        all_bars = load_data(FILE_PATH)
        print_bar_info('большой', get_biggest_bar(all_bars))
        print_bar_info('маленький', get_smallest_bar(all_bars))
        print_bar_info('ближайший', get_closest_bar(all_bars, LONGITUDE, LATITUDE))
    except FileNotFoundError:
        sys.exit('File with data is missed!')
