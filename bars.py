import os
import sys
import json

FILE_PATH = 'bars.json'


def load_data(filepath):
    if os.path.exists(filepath):
        with open(file=filepath, mode='r') as datafile:
            return json.load(datafile)
    else:
        raise FileNotFoundError


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    try:
        all_bars = load_data(FILE_PATH)

    except FileNotFoundError:
        sys.exit('File with data is missed!')
