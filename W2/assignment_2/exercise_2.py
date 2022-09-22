def ln2_approximation(N):
    """Return an approximation for natural logarithm of 2
    iterated over `N` terms
    
    :param N: iteration count, defines the number of terms of the series
    :type N: int
    
    :rtype: float
    :return: approximation of natural logarithm of 2
    """
    ln2_approximate_value = 0

    # iterate the formula `N` times with counter of `k` starting from 1
    for k in range(1, N + 1):
        ln2_approximate_value += 1 / ((3 ** k) * k) + 1 / ((4 ** k) * k)

    return ln2_approximate_value
