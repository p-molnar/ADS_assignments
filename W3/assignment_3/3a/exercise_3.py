from exercise_2 import *


def convert_data_percentages(data, col_id):
    """Convert row values to percentages, whereby the whole of
     the percentage is referred to as by `col_id`
    
    :param data: body of a csv file
    :type data: list
    :param col_id: column index of the particular column based
     on which the percentage is calculated
    :type col_id: int

    :rtype: list|None
    :return: converted data
    """
    # error handling - index out of range
    if col_id < 0 or col_id >= len(data[0]):
        return None

    # create a copy of data to preserve
    # the original data from in-place changes
    converted_data = data.copy()

    for row in converted_data:
        whole = int(row[col_id])
        row[col_id + 1 :] = map(lambda part: int(part) / whole, row[col_id + 1:])

    return converted_data
