def ln2_approximation(N):
    """Return an approximation for natural logarithm of 2 for `N` terms
    
    :param N: iteration count, defines the number of iteration for the approximation
    :type N: int
    
    :rtype: float
    :return: approximation of natural logarithm of 2
    """
    ln2_approximate_value = 0
    for k in range(1, N + 1):
        ln2_approximate_value += 1 / ((3 ** k) * k) + 1 / ((4 ** k) * k)
    return ln2_approximate_value
