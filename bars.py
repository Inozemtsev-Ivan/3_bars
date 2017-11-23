import sys
import math
import requests
import http_status

DATA_MOS_RU_URL = 'https://apidata.mos.ru/v1/features/1796?api_key='
DATA_MOS_RU_API_KEY = 'd972f4bad54daf8410866cf9472f9efc'


def input_coordinates():
    print('Укажите широту и долготу через пробел, например, "37.6269 55.7535"')
    while True:
        elements = input('>').split()
        try:
            longitude, latitude = map(float, elements)
            return longitude, latitude
        except ValueError:
            print('Неправильно указаны координаты! Повторите ввод.')
            continue


def load_data(api_address, api_key):
    url = ''.join([api_address, api_key])
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        http_error = http_status.Status(r.status_code)
        exception_description = 'Error {code}: {desc}'.format(
            code=http_error.code,
            desc=http_error.description,
        )
        raise IOError(exception_description)


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
        all_bars = load_data(DATA_MOS_RU_URL, DATA_MOS_RU_API_KEY)
    except IOError as ex:
        sys.exit(str(ex))
    longitude, latitude = input_coordinates()
    print_bar_info('большой', get_biggest_bar(all_bars))
    print_bar_info('маленький', get_smallest_bar(all_bars))
    print_bar_info('ближайший', get_closest_bar(all_bars, longitude, latitude))
