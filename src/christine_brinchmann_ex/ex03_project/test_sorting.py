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


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([3]) == [3]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data
