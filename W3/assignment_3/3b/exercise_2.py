from exercise_1 import *
from city_map import *

EMPTY = 1

direction = {
	"up": 10,
	"down": 20,
	"left": 30,
	"right": 40
}

def is_valid_coordinate(x, y, map_dimension):
	return y in range(map_dimension["HEIGHT"]) and x in range(map_dimension["WIDTH"])

def path_finder_backtracker(map, start_loc, visited_locs):
	x, y = start_loc
	dim = {
		"WIDTH": len(map[0]),
		"HEIGHT": len(map),
	}
	if not is_valid_coordinate(x, y, dim):
		return 0

	if x == dim["WIDTH"] - 1 and map[y][x] == EMPTY:
		return 1

	if is_valid_coordinate(x, y, dim) and map[y][x] == EMPTY:
		# print(map)
		visited_locs.append(start_loc)
		map[y][x] = direction["up"]
		if path_finder_backtracker(map, (x, y - 1), visited_locs):
			return 1
		map[y][x] = direction["down"]
		if path_finder_backtracker(map, (x, y + 1), visited_locs):
			return 1
		map[y][x] = direction["left"]
		if path_finder_backtracker(map, (x - 1, y), visited_locs):
			return 1
		map[y][x] = direction["right"]
		if path_finder_backtracker(map, (x + 1, y), visited_locs):
			return 1
		map[y][x] = EMPTY
	return 0

def find_route(route_map, current_loc, visited_locs):
	solved_map = route_map.copy()

	if path_finder_backtracker(solved_map, current_loc, visited_locs):
		return solved_map
	return None


# city_map = np.array([
#     [ 1, 1, 1, 1, 1 ],
#     [ 1, 0, 1, 1, 1 ],
#     [ 1, 1, 1, 1, 1 ],
#     [ 1, 1, 1, 1, 0 ],
#     [ 1, 1, 1, 0, 1 ]])

marked_map = mark_parking_locations(city_map)

# marked_map = np.array([
# 	[ 1, 1, 1, ],
# 	[ 1, 0, 1, ],
# 	[ 1, 0, 1, ]])
print(marked_map)

for i in range(12):
	print(f"iter: (0, {i})")
	print(find_route(marked_map, (0, i), []))

