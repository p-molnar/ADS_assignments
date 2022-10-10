from vars import *

def pretty_printer(route_map):
    """Print a solved `route_map` in a prettified format

    :param route_map: a route map
    :type route_map: numpy.ndarray

    :return: None
    :rtype: None
    """

    char_set = {
        -1: "❌",
         0: "🏢",
         1: "🛣️",
        10: "⬆️",
        20: "⬇️",
        30: "⬅️",
        40: "➡️",
    }

    arr = []
    
    # iterate over each position on the map
    for i in range(len(route_map)):
        row = []
        for j in range(len(route_map[0])):
            # retrieve the corresponsing unicode character at each map position
            row.append(char_set[route_map[i][j]])

        # add each row to main list
        arr.append(row)

    # convert list into numpy array, print output and return None
    return print(np.array(arr))
