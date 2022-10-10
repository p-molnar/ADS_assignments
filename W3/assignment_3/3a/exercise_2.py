def filter_data(data, col_idx, condition):
    """Filter out rows from `data` based on a single `condition`

    :param data: body of a csv file
    :type data: list
    :param col_idx: column identifier, defines the column against which condition is tested
    :type col_idx: int
    :param condition: a collection of rules based on which the filteration is applied
    :type condition: dict

    :rtype: list|None
    :return: rows of `data` where the `condition` was satisfied
    """
    data_selection = []

    # if filter is of type list
    if isinstance(condition, list):
        # filter out rows
        for col_val in condition:
            data_selection += list(filter(lambda row: row[col_idx] == col_val, data))

    # if filter is of type tuple
    elif isinstance(condition, tuple):
        # check if all values in the given column are of numeric type
        if not all([val[col_idx].isnumeric() for val in data]):
            return None

        # unpack tuple
        lower_bound, upper_bound = condition

        data_selection += list(
            filter(
                lambda row: int(row[col_idx]) > lower_bound
                and int(row[col_idx]) < upper_bound,
                data,
            )
        )

    return data_selection


def get_group(data, headers, condition):
    """Retrieve a subset of data based on a collection of condition

    :param data: body of a csv file
    :type data: list
    :param headers: headers of a csv file
    :type headers: list
    :param condition: a collection of filteration condition based on 
        which the a group of data to be created
    :type condition: dict

    :rtype: list|None
    :return: a group of data where the condition is satisfied
    """

    # check if condition is of type str, or int
    if isinstance(condition, str) or isinstance(condition, int):
        filtered_data = get_by_axis(data, headers, condition)

    elif isinstance(condition, dict):

        # preserve the original data by creating a copy
        filtered_data = data[:]

        # iterate through conditions
        for col_name, rule in condition.items():
            # error handling - invalid column name
            if col_name not in headers:
                return None

            # get column index position based on column name
            col_idx = headers.index(col_name)
            filtered_data = filter_data(filtered_data, col_idx, rule)

    return filtered_data
