from exercise_1 import *
from city_map import *

BUILDING = 0
EMPTY = 1
PARKING = -1

direction = {"up": 10, "down": 20, "left": 30, "right": 40}

print("START")

def is_valid_coordinate(x, y, map_dimension):
	return y in range(map_dimension["HEIGHT"]) and x in range(map_dimension["WIDTH"])

def find_route(route_map, current_loc, visited_locs):

	x, y = current_loc
	dim = {
		"WIDTH": len(route_map[0]),
		"HEIGHT": len(route_map),
	}
	
	if x == dim["WIDTH"] - 1:
		print("finish\n")
		return 1
	
	visited_locs.append((x, y))

	if is_valid_coordinate(x, y, dim) and route_map[y][x] == EMPTY:
		
		route_map[y][x] = direction["up"]
		if find_route(route_map, (x, y - 1), visited_locs):
			return 1
		route_map[y][x] = direction["down"]
		if find_route(route_map, (x, y + 1), visited_locs):
			return 1
		route_map[y][x] = direction["left"]
		if find_route(route_map, (x - 1, y), visited_locs):
			return 1
		route_map[y][x] = direction["right"]
		if find_route(route_map, (x + 1, y), visited_locs):
			return 1

		route_map[y][x] = EMPTY
	# if y - 1 in range(len(route_map)) and route_map[y - 1][x] == EMPTY and (y - 1, x) not in visited_locs:
	# 	route_map[y][x] = direction["up"]
	# 	find_route(route_map, (x, y - 1), visited_locs)
	# elif x + 1 in range(len(route_map)) and route_map[y][x + 1] == EMPTY and (y, x + 1) not in visited_locs:
	# 	route_map[y][x] = direction["right"]
	# 	find_route(route_map, (x + 1, y), visited_locs)
	# elif y + 1 in range(len(route_map)) and route_map[y + 1][x] == EMPTY and (y + 1, x) not in visited_locs:
	# 	route_map[y][x] = direction["down"]
	# 	find_route(route_map, (x, y + 1), visited_locs)
	# elif x - 1 in range(len(route_map)) and route_map[y][x - 1] == EMPTY and (y, x - 1) not in visited_locs:
	# 	route_map[y][x] = direction["left"]
	# 	find_route(route_map, (x - 1, y), visited_locs)

	# print(visited_locs)	
	# print(route_map, "\n")
	return 0

marked_map = mark_parking_locations(city_map)
# start_loc -> (x, y)
# y -> row, depth
# x -> col, width (?)
print(find_route(marked_map, (0, 2), []))