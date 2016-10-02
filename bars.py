import json


def load_data(filepath):
    strin = ''
    with open(filepath, encoding='utf8') as iner:
        for line in iner:
            strin += line
    return strin


def get_biggest_bar(data):
    number_of_seats = 0
    bar_index = 0
    for idx,vocabul in enumerate(data):
        if vocabul['Cells']['SeatsCount'] >= number_of_seats:
            number_of_seats = vocabul['Cells']['SeatsCount']
            bar_index = idx
    return bar_index


def get_smallest_bar(data):
    bar_index = 0
    for idx,vocabul in enumerate(data):
        if idx == 0:
            number_of_seats = vocabul['Cells']['SeatsCount']
            continue
        if vocabul['Cells']['SeatsCount'] <= number_of_seats:
            number_of_seats = vocabul['Cells']['SeatsCount']
            bar_index = idx
    return bar_index


def get_closest_bar(data, longitude, latitude):
    bar_index = 0
    for idx, vocabul in enumerate(data):
        if idx == 0:
            distance = ((vocabul['Cells']['geoData']['coordinates'][0]-longitude)**2+(vocabul['Cells']['geoData']['coordinates'][1]-latitude)**2)**0.5
            continue
        if ((vocabul['Cells']['geoData']['coordinates'][0]-longitude)**2+(vocabul['Cells']['geoData']['coordinates'][1]-latitude)**2)**0.5 < distance:
            distance = ((vocabul['Cells']['geoData']['coordinates'][0]-longitude)**2+(vocabul['Cells']['geoData']['coordinates'][1]-latitude)**2)**0.5
            bar_index = idx
    return bar_index


if __name__ == '__main__':
    filepath='Бары.json'
    strin=load_data(filepath)
    data = json.loads(strin)

    max_bar_idx = get_biggest_bar(data)
    print('Самый большой бар:',data[max_bar_idx]['Cells']['Name'])

    min_bar_idx = get_smallest_bar(data)
    print('Самый маленький бар:',data[min_bar_idx]['Cells']['Name'])

    coords = [float(coord) for coord in input().split(',')]

    closet_bar_idx = get_closest_bar(data,coords[0],coords[1])
    print('Самый ближайший к Вам бар:', data[closet_bar_idx]['Cells']['Name'])
