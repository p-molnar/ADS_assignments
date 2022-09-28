from ast import excepthandler
from email import header
from shutil import ExecError
from data_loader import *


def get_by_axis(data, headers, element_id):
	"""Return row or column values based on `element_id`

	:param data: row values of a csv file
	:type data: list
	:param headers: column names of a csv file
	:type headers: list
	:param element_id: index of a row, or label of a column
	:type element_id: int|str

	:raises IndexError:
		* if `element_id` is of type int, and is negative or greater than 
			the number of rows in `data`
		* if `element_id` is of type str and header is not in `headers` list

	:rtype: list|None
	:return: row or column values of `data`
	"""
	n_row, n_col = len(data), len(headers)
		
	if isinstance(element_id, int):
		if element_id < 0 or element_id not in range(n_row):
			raise IndexError(f"element_id of {element_id} out of range")
		return data[element_id]
	elif isinstance(element_id, str):
		col_list = []
		if element_id not in range(n_row):
			raise IndexError(f"no column named as {element_id}")
		col_idx = headers.index(element_id)
		
		for row in data:
			col_list.append(row[col_idx])
		return col_list
		
	return None


data, headers = load_data_from_csv("kwb-2019.csv")
print(get_by_axis(data, headers, ""))
