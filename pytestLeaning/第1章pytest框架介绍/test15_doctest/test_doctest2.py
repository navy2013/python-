"""
    function：两个数相乘
    >>> multiply(4,8)
    12
    >>> multiply('a',5)
    'aaa'
"""

def multiply(a, b):

    return a * b


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
