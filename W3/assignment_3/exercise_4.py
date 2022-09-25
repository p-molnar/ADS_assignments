from doctest import DocTestCase
from exercise_3 import *

def sort_table(data, headers, condition, k=10, descending=True):
	col_idx = headers.index(condition)

	sorted_data = sorted(data, key=lambda row: row[col_idx], reverse=descending)

	return sorted_data[:k] # error checking for signed values?

# data_1 = convert_data_percentages(data, col_id=2)
# print(sort_table(data_1, headers, condition="region", k = 2, descending=False))