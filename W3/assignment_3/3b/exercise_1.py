def mark_parking_locations(city_map):
    for i, row in enumerate(city_map):
        for j, el in enumerate(row):
            if el == 0:
                if i - 1 in range(len(city_map)):
                    city_map[i - 1][j] = -1
                if i + 1 in range(len(city_map)):
                    city_map[i + 1][j] = -1
                if j - 1 in range(len(city_map[0])):
                    city_map[i][j - 1] = -1
                if j + 1 in range(len(city_map[0])):
                    city_map[i][j + 1] = -1
            
    return city_map
