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
    A new list with the data in sorted order.

    """
    new_data = list(data_input)
    n = len(new_data)

    for i in range(n-1):
        for j in range(n-1-i):
            if new_data[j] > new_data[j+1]:
                new_data[j], new_data[j+1] = new_data[j+1], new_data[j]

    return new_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []
