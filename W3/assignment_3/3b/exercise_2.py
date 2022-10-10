from vars import *

def is_valid_coordinate(x, y, map_dimension):
    """Logical test whether a given pair of coordinates are within the boundaries of the map

    :param x: x coordinate
    :type x: int
    :param y: y coordinate
    :type y: int
    :param map_dimension: a dictionary storing the dimensions of the map
    :type map_dimension: dict

    :rtype: Bool
    :return: True if the pair of coordinate is within the boundaries of the map, else False 
    """
    return y in range(map_dimension["height"]) and x in range(map_dimension["width"])


def path_finder_backtracker(marked_map, start_loc, visited_locs):
    """The function recursively finds and marks the first solution
    of the map

    :param map: the map on which the direction is to be marked
    :type map: numpy.ndarray
    :param start_loc: the starting position from where the map is to be solved
    :type start_loc: tuple
    :param visited_locs: a list that collects locations the backtracker visited
    :type visited_locs: list

    :rtype: Bool
    :return: returns True to the main caller, and to the recursive caller 
    either if the map is solved or a given direction is valid in a given 
    `start_loc`, 0 if the direction is invalid, or the map has no solution
    """
    

    dim = {
        "width": len(marked_map[0]),
        "height": len(marked_map),
    }

    # unpack start_loc into x and y coordinates respectively
    x, y = start_loc
    
    # recursive base condition
    if y == dim["width"] - 1 and marked_map[x][y] == space_type["empty"]:
        return True

    if is_valid_coordinate(y, x, dim) and marked_map[x][y] == space_type["empty"]:
        visited_locs.append(start_loc)
        marked_map[x][y] = direction["up"]
        if path_finder_backtracker(marked_map, (x - 1, y), visited_locs) == True:
            return True
        marked_map[x][y] = direction["down"]
        if path_finder_backtracker(marked_map, (x + 1, y), visited_locs) == True:
            return True
        marked_map[x][y] = direction["left"]
        if path_finder_backtracker(marked_map, (x, y - 1), visited_locs) == True:
            return True
        marked_map[x][y] = direction["right"]
        if path_finder_backtracker(marked_map, (x, y + 1), visited_locs) == True:
            return True
        marked_map[x][y] = space_type["empty"]
    
    return False


def find_route(route_map, current_loc, visited_locs):
    """Finds and returns a solution for the map passed to it

    :param route_map: the map on which the direction is to be marked
    :type map: numpy.ndarray
    :param start_loc: the starting position from where the map is to be solved
    :type start_loc: tuple
    :param visited_locs: a list that collects locations that the backtracker visited
    :type visited_locs: list

    :rtype: numpy.ndarray|None
    :return: if the map has a solution, it returns a potential solution, otherwise nothing
    """
    # duplicate map to avoid overriding the original map
    solved_map = route_map.copy()

    # start backtracker, return if there is solution, else return None
    if path_finder_backtracker(solved_map, current_loc, visited_locs):
        return solved_map
    return None
