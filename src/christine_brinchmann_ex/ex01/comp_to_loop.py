

def squares_by_loop(n):
    """ Returns a list with the squared value of the numbers in range(n),
    for which the remainder of a division by 3 is equal to 1.
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


if __name__ == '__main__':
    if squares_by_loop(n=20) != squares_by_comp(n=20):
        print('ERROR!')
