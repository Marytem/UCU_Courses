import math
import copy

def tsp(data):
    """
    :param data: [[X, Y],[X, Y]]
    :return:(length, path) - len of way, way itself [ind, ind, ...] - n+1
    """
    copy_data = copy.deepcopy(data)
    length = 0
    path = []
    path.append(0)
    copy_data.pop(0)
    while copy_data:
        close = closest(data[path[-1]], copy_data)
        path.append(data.index(close[0]))
        copy_data.remove(close[0])
        length += close[1]
    length += math.sqrt((data[0][0] - data[path[-1]][0]) ** 2 + (data[0][1] - data[path[-1]][1]) ** 2)
    path.append(0)
    return length, path

def closest(coord, cities):
    """
    :param coord: coordinates, to which the closest city must be found
    :param cities: list of coordinates of the cities
    :return: coordinates of the closest city and a distance to it
    """
    closest_city = 0
    min_dist = 10**300
    for city in cities:
        dist = math.sqrt((coord[0] - city[0]) ** 2 + (coord[1] - city[1]) ** 2)
        if dist < min_dist:
            min_dist = dist
            closest_city = city
    return closest_city, min_dist


def description():
    return "tsp(data):  Since it does not matter from which city to start, the algorithm starts from the first one(0). \
It appends the city's index to path variable and delete's that city from the copy of data, made before. While there is \
something left in that copy, it finds the closest city in the copy and a distance to it using closest(), deletes a found \
city from the copy list, appends its index in the data to the path, and increases length variable by the distance found.\n \
closest(coord, cities): finds the closest city to the given coord and a distance to it. Iterates through a given list \
of coords and changes min_dist and closest variables if the calculated distance to coord is less than on the previous \
iteration."