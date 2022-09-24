from data_loader import *
from exercise_1 import *

def filter_data(data, col_idx, condition):
	data_selection = []

	for criteria in condition:
		if isinstance(criteria, list):	
			for crit in criteria:
				data_selection += list(filter(lambda row: row[col_idx] == crit, data))
		elif isinstance(criteria, tuple):
			lower_bound, upper_bound = criteria
			data_selection += list(filter(lambda row: int(row[col_idx]) > lower_bound and int(row[col_idx]) < upper_bound, data))

	return data_selection

def get_group(data, headers, condition):	
	n_row, n_col = len(data), len(headers)
	if isinstance(condition, str) or isinstance(condition, int):
		return get_by_axis(data, headers, condition)

	elif isinstance(condition, dict): # do error checking!
		data_selection = data.copy()

		for k, v in condition.items():
			col_idx = headers.index(k)
			data_selection = filter_data(data_selection, col_idx, v)

		return data_selection

data, headers = load_data_from_csv("kwb-2019.csv")
# print(get_group(data, headers, {'region': []}))
# print(get_group(data, headers, {'region': ["Amsterdam", "Utrecht"]}))
print(get_group(data, headers, {'region': ["Rotterdam", "Utrecht"], 'population': (500000, 700000)}))