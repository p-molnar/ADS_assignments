from asyncio.proactor_events import _ProactorDuplexPipeTransport
from exercise_2 import *


def convert_data_percentages(data, col_id):
	data_percentage = []

	for row in data:
		population = int(row[col_id])

		cols_excl = row[:col_id + 1]
		cols_incl = row[col_id + 1:]		
		data_percentage.append(cols_excl + [int(col) / population for col in cols_incl])
		
	return data_percentage

print(convert_data_percentages(data, col_id=2))
