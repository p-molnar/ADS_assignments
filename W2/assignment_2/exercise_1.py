def substrings(s: str) -> list:
    """return a list of unique substrings of s

    :param s: string of which substrings are made out of
    :type s: str

    :rtype: list
    :return: list of substrings
    """
    list_of_substrings = []

    # iterate through string, slice it in each index position
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            list_of_substrings.append(s[start:end])

    # remove duplicate list items
    list_of_substrings = list(set(list_of_substrings))
    return list_of_substrings


def longest_nonrepeating_substring(l: list) -> str:
    """Return the longest non-repeating string of a list of substrings
    
    :param l: list of substrings
    :type l: list

    :rtype: str
    :return: last evaluated longest non-repeating substring

    .. note:: 
        If there are multiple equal length non-repeating substrings, 
        the last longest non-repeating substring of the list 
        is returned.
    """
    longest_substring = ""

    for cur_substr in l:
        # check if cur_substr contains unique characters only
        is_non_repeating = len(cur_substr) == len("".join(set(cur_substr)))

        if is_non_repeating and len(cur_substr) >= len(longest_substring):
            longest_substring = cur_substr

    return longest_substring
