def substrings(s: str) -> list:
    """return a list of unique substrings of `s`

    :param s: string of which substrings are made of
    :type s: str

    :rtype: list
    :return: list of unique substrings
    """
    list_of_substrings = []
    str_len = len(s)

    for start in range(str_len):
        for end in range(start + 1, str_len + 1):
            substring = s[start:end]
            if substring not in list_of_substrings:
                list_of_substrings.append(substring)

    return list_of_substrings


def longest_nonrepeating_substring(l: list) -> str:
    """Find and return the longest unique characters only string of list

    :param l: list of substrings
    :type l: list

    :rtype: str
    :return: longest non-repeating string
    """
    longest_substring = ""

    # iterate through the list of substrings
    for cur_substr in l:
        # check if `cur_substr` contains unique characters only
        is_non_repeating = len(cur_substr) == len("".join(set(cur_substr)))
        if is_non_repeating and len(cur_substr) > len(longest_substring):
            longest_substring = cur_substr

    return longest_substring
