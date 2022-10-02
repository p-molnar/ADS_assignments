import numpy as np
from exercise_1 import *

def pretty_printer(route_map):
    
    char_set = {
        -1: '❌',
        0: '🏢', 
        1: '🛣️', 
        10: '⬆️',
        20: '⬇️',
        30: '⬅️',
        40: '➡️',
    }
    
    arr = []
    
    for i in range(len(route_map)):
        row = []
        for j in range(len(route_map[0])):
            row.append(char_set[route_map[i][j]])
        arr.append(row)

    print(np.array(arr))

    return None

print("\n")
pretty_printer(mark_parking_locations(city_map))
