# Place your answers here.

def contains_only_unique_chars(s: str) -> bool:
    """Evaluate string whether it contains only unique characters.
    
    :param s: string to be evaluated
    :type s: str

    :rtype: bool
    :return: True if `s` contains only unique characters, else False
    """ 
    for i, cur_char in enumerate(s):
        if (cur_char in s[i + 1:]):
            return False
    return True

def substrings(s: str) -> list:
    """Create a list of unique substrings from `s`
    
    :param s: string for substring creation
    :type s: str
    
    :rtype: list
    :return: list of substrings
    """
    list_of_substrings = []
    str_len = len(s)

    for start in range(str_len):
        for end in range(start + 1, str_len + 1):
            substring = s[start:end]
            if (substring not in list_of_substrings):
                list_of_substrings.append(substring)
    return list_of_substrings
    
def longest_nonrepeating_substring(l: list) -> str:
    """Find and return the longest non-repeating substring in a list of strings
    
    :param l: list of substrings
    :type l: list
    
    :rtype: str
    :return: longest non-repeating string
    """
    longest_substring = ""
    
    for curr_string in l:
        if (contains_only_unique_chars(curr_string) and len(curr_string) > len(longest_substring)):
            longest_substring = curr_string
            
    return longest_substring