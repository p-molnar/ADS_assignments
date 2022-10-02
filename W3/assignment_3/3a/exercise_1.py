from tkinter import W
from data_loader import *

def get_by_axis(data, headers, element_id):
	"""Return row or column values based on `element_id`

	:param data: body of a csv file
	:type data: list
	:param headers: header names of a csv file
	:type headers: list
	:param element_id: index of a row, or name of a column
	:type element_id: int|str

	:rtype: list|None
	:return: row or column values of `data`

	.. notes::
		* in case of invalid element_id, the function returns None
			* if element_id is of type int, it must be within [0, len(data)]
			* if element_id is of type str, it must be within `headers`
	"""
	n_row = len(data)

	# check if element_id is of type int
	if isinstance(element_id, int):

		# error handling - index out of range
		if element_id < 0 or element_id not in range(n_row):
			return None
		return data[element_id]

	# check if element_id is of type str
	elif isinstance(element_id, str):

		# error handling - str not in list
		if element_id not in headers:
			return None
		
		column = []

		# get column index based on column name
		col_idx = headers.index(element_id)

		# extract column values	
		for row in data:
			column.append(row[col_idx])
		return column
		
	return None

data, headers = load_data_from_csv("kwb-2019.csv")
# print(get_by_axis(data, headers, 355))
