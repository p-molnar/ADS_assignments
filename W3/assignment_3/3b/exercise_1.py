from vars import *

def mark_parking_locations(city_map):
    """Mark the parking lots on a city map

    :param city_map: a numpy array representing a city map
    :type city_map: numpy.ndarray

    :rtype: numpy.ndarray
    :return: the marked city map
    """
    
    # loop through map, and in each position mark parking spots
    # if current location is a building
    for y, row in enumerate(city_map):
        for x, col in enumerate(row):
            if col == space_type["building"]:
                if y - 1 in range(len(city_map)):
                    city_map[y - 1][x] = space_type["parking"]
                if y + 1 in range(len(city_map)):
                    city_map[y + 1][x] = space_type["parking"]
                if x - 1 in range(len(city_map[0])):
                    city_map[y][x - 1] = space_type["parking"]
                if x + 1 in range(len(city_map[0])):
                    city_map[y][x + 1] = space_type["parking"]
    
    return city_map
