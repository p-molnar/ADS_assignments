from data_loader import *
from exercise_1 import *

def filter_data(data, col_idx, condition):
	data_selection = []

	if isinstance(condition, list):	
		for criteria in condition:
			data_selection += list(filter(lambda row: row[col_idx] == criteria, data))
	elif isinstance(condition, tuple):
		lower_bound, upper_bound = condition 
		data_selection += list(filter(lambda row: int(row[col_idx]) > lower_bound and int(row[col_idx]) < upper_bound, data))

	return data_selection

def get_group(data, headers, condition):	

	if isinstance(condition, str) or isinstance(condition, int):
		data_selection = get_by_axis(data, headers, condition)

	elif isinstance(condition, dict): # do error checking!
		data_selection = data.copy()

		for k, v in condition.items():
			col_idx = headers.index(k)
			data_selection = filter_data(data_selection, col_idx, v)

	return data_selection

data, headers = load_data_from_csv("kwb-2019.csv")
# print(get_group(data, headers, {'men': ["581", "17703"]}))
# print(get_group(data, headers, {'region': ["Amsterdam", "Utrecht"]}))
# print(get_group(data, headers, {'region': ["Rotterdam", "Utrecht"], 'population': (500000, 700000)})criteria)