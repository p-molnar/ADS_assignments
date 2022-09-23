from data_loader import *


def get_by_axis(data, headers, element_id):
	n_row, n_col = len(data), len(headers)

	if isinstance(element_id, int) and element_id in range(n_row + 1):
		return data[element_id]
	elif isinstance(element_id, str) and element_id in headers:
		col_list = []
		col_idx = headers.index(element_id)
		
		for row in data:
			col_list.append(row[col_idx])
		return col_list
		
	return None


data, headers = load_data_from_csv("kwb-2019.csv")
