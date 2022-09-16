def ln2_approximation(N):
    """Return an approximation for natural logarithm of 2 for `N` terms
    
    :param N: an integer, it tells the iteration count
    :type N: int
    
    :rtype: int|float
    :return: approximation of natural logarithm of 2
    """
    ln2_approximate_value = 0
    for k in range(1, N + 1):
        ln2_approximate_value += 1 / ((3 ** k )* k) + 1 / ((4 ** k )* k)
    return ln2_approximate_value