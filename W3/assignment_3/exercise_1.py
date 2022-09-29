from data_loader import *

def get_by_axis(data, headers, element_id):
	"""Return row or column values based on `element_id`

	:param data: row values of a csv file
	:type data: list
	:param headers: column names of a csv file
	:type headers: list
	:param element_id: index of a row, or label of a column
	:type element_id: int|str

	:rtype: list|None
	:return: row or column values of `data`
	"""
	n_row, n_col = len(data), len(headers)
		
	if isinstance(element_id, int):
		if element_id < 0 or element_id not in range(n_row):
			return None
		return data[element_id]
	elif isinstance(element_id, str):
		if element_id not in headers:
			return None
		
		column = []
		col_idx = headers.index(element_id)
		
		for row in data:
			column.append(row[col_idx])
		return column
		
	return None

data, headers = load_data_from_csv("kwb-2019.csv")
# print(get_by_axis(data, headers, 355))
