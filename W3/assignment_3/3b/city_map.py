import numpy as np

city_map_orig = np.array([
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]])

city_map = np.array([
    [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 1, 0, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 1, 1, 0, 1, 1, -1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, -1, 1 ],
    [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, -1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, -1, 1 ]])
# [ 1, -1,  1,  1,  1,  1,  1,  1,  1,  1],
# [-1,  0, -1, -1,  1,  1,  1,  1,  1,  1],
# [ 1, -1, -1,  0, -1,  1,  1,  1,  1,  1],
# [ 1,  1,  1, -1,  0, -1,  1,  1,  1,  1],
# [ 1,  1,  1,  1, -1, -1,  1,  1,  1,  1],
# [ 1, -1,  1,  1, -1,  0, -1,  1, -1,  1],
# [-1,  0, -1,  1,  1, -1,  1, -1,  0, -1],
# [ 1, -1,  1,  1,  1,  1,  1,  1, -1,  1],
# [-1,  1,  1,  1,  1, -1,  1,  1,  1,  1],
# [ 0, -1,  1,  1, -1,  0, -1,  1,  1,  1],
# [-1,  1,  1, -1,  1, -1,  1,  1,  1,  1],
# [ 1,  1, -1,  0, -1,  1,  1,  1,  1,  1]


# direction = {
# "up": 10,
# "down": 20,
# "left": 30,
# "right": 40,
# }