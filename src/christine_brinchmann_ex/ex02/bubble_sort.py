# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


def bubble_sort(data_input):
    """
    The function sorts data using the bubble sort method.

    Parameters
    ----------
    data_input: the data to be sorted.

    Returns
    -------
    A new tuple with the data in sorted order.

    """
    new_data = list(data_input)
    n = len(new_data)

    for i in range(n-1):
        for j in range(n-1-i):
            if new_data[j] > new_data[j+1]:
                new_data[j], new_data[j+1] = new_data[j+1], new_data[j]

    return tuple(new_data)


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
