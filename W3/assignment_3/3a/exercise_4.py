from exercise_3 import *


def sort_table(data, headers, condition, k=10, descending=True):
    """Return a sorted table

    :param data: body of a csv file
    :type data: list
    :param headers: headers of a csv file
    :type headers: list
    :param condition: header name of a column according to which
    the table is sorted
    :type condition: str
    :param k: defines the top k results of the sorted list to be returned, defaults to 10
    :type k: int
    :param descending: specifies the sorting order of the table, defaults to True
    :type descending: bool

    :rtype: list|None
    :return: a sorted table
    """
    # parameter validation - index out of range
    if k < 0 or k >= len(data) or condition not in headers:
        return None

    # get column index based on its name
    col_idx = headers.index(condition)

    # sort table according to a specific column
    sorted_data = sorted(data, key=lambda row: row[col_idx], reverse=descending)

    # return the first k results
    return sorted_data[:k]


# data_1 = convert_data_percentages(data, col_id=2)
# print(sort_table(data_1, headers, condition="married", k=5, descending=True))
