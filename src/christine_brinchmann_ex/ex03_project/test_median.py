# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    :source of code: https://github.com/yngvem/INF200-2019-Exercises/blob
    /master/exersices/ex03.rst

    The code has been modified
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
            ) / 2


def test_single_element_list():
    """Tests that the median of a single element list is that element"""
    assert median([2]) == 2


def test_odd_number_elements_list():
    """
    Tests that the correct median is returned for a list with odd numbers
    of elements.
    """
    odd_list = [1, 2, 3, 4, 5]
    assert median(odd_list) == 3
