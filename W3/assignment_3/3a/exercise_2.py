from data_loader import *
from exercise_1 import *

def filter_data(data, col_idx, condition):
	data_selection = []

	# if filter is of type list
	if isinstance(condition, list):	
		# filter out rows 
		for col_val in condition:
			data_selection += list(filter(lambda row: row[col_idx] == col_val, data))

	# if filter is of type typle
	elif isinstance(condition, tuple):
		lower_bound, upper_bound = condition 
		data_selection += list(condition(lambda row: int(row[col_idx]) > lower_bound and int(row[col_idx]) < upper_bound, data))

	return data_selection

def get_group(data, headers, condition):	

	if isinstance(condition, str) or isinstance(condition, int):
		data_group = get_by_axis(data, headers, condition)

	elif isinstance(condition, dict): # do error checking!

		data_group = data.copy()

		for col_name, filter in condition.items():
			# error handling - invalid column name
			if col_name not in headers:
				return None

			col_idx = headers.index(col_name)
			data_group = filter_data(data_group, col_idx, filter)

	return data_group

data, headers = load_data_from_csv("kwb-2019.csv")
print(get_group(data, headers, {'men': ["581", "17703"]}))
# print(get_group(data, headers, {'region': ["Amsterdam", "Utrecht"]}))
# print(get_group(data, headers, {'region': ["Rotterdam", "Utrecht"], 'population': (500000, 700000)}))