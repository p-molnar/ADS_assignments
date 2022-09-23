from data_loader import *
from exercise_1 import *

def get_group(data, headers, condition):	
	n_row, n_col = len(data), len(headers)
	if isinstance(condition, str) or isinstance(condition, int):
		return get_by_axis(data, headers, condition)
	elif isinstance(condition, dict): # do error checking!
		ret_list = []
		k, v = list(condition.keys()), list(condition.values())

		for col in k:
			col_idx = headers.index(col)
			for row in data:
				if row[col_idx] == v[0][0]:
					ret_list += row
		return ret_list
	return None

data, headers = load_data_from_csv("kwb-2019.csv")
print(get_group(data, headers, {'region': ["Amsterdam"]}))
