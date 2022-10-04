def mark_parking_locations(city_map):
    """Mark the parking lots on a city map

    :param city_map: an array representing a city map
    :type city_map: numpy.ndarray

    :rtype: numpy.ndarray
    :return: the marked city map
    """
    for y, row in enumerate(city_map):
        for x, el in enumerate(row):
            if el == 0:
                if y - 1 in range(len(city_map)):
                    city_map[y - 1][x] = -1
                if y + 1 in range(len(city_map)):
                    city_map[y + 1][x] = -1
                if x - 1 in range(len(city_map[y])):
                    city_map[y][x - 1] = -1
                if x + 1 in range(len(city_map[y])):
                    city_map[y][x + 1] = -1
            
    return city_map
