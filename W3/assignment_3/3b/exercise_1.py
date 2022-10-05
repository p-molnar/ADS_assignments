PARKING_LOT = -1
BUILDING = 0
EMPTY = 1


def mark_parking_locations(city_map):
    """Mark the parking lots on a city map

    :param city_map: an array representing a city map
    :type city_map: numpy.ndarray

    :rtype: numpy.ndarray
    :return: the marked city map
    """
    for y, row in enumerate(city_map):
        for x, col in enumerate(row):
            if col == BUILDING:
                if y - 1 in range(len(city_map)):
                    city_map[y - 1][x] = PARKING_LOT
                if y + 1 in range(len(city_map)):
                    city_map[y + 1][x] = PARKING_LOT
                if x - 1 in range(len(city_map[y])):
                    city_map[y][x - 1] = PARKING_LOT
                if x + 1 in range(len(city_map[y])):
                    city_map[y][x + 1] = PARKING_LOT
    return city_map
