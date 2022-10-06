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
    if col_id not in range(len(data[0])) or not all(
        [row[col_id].isnumeric() for row in data]
    ):
        return None

    converted_data = []

    for row_idx, row in enumerate(data):
        whole = int(row[col_id])
        converted_data.append(
            row[: col_id + 1]
            + list(map(lambda part: int(part) / whole, row[col_id + 1 :]))
        )

    return converted_data
