# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"

import pytest


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

    if num_elements == 0:
        raise ValueError
    else:
        if num_elements % 2 == 1:
            return sorted_data[num_elements // 2]
        else:
            return (sorted_data[num_elements // 2 - 1]
                    + sorted_data[num_elements // 2]) / 2


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


def test_even_number_elements_list():
    """
    Tests that the correct median is returned for a list with even numbers
    of elements.
    """
    even_list = [1, 2, 3, 4]
    assert median(even_list) == 2.5


def test_median_for_ordered_elements():
    """Tests that the median function works for ordered elements in list"""
    example_list = [1, 2, 3, 4, 5, 6, 7]
    assert median(example_list) == 4


def test_median_for_reverse_ordered_elements():
    """
    Tests that the median function works for reverse ordered elements in
    list
    """
    example_list = [7, 6, 5, 4, 3, 2, 1]
    assert median(example_list) == 4


def test_median_for_unordered_elements():
    """Tests that the median function works for unordered elements in list"""
    example_list = [3, 1, 4, 2, 6, 7, 5]
    assert median(example_list) == 4


def test_median_raises_value_error_on_empty_list():
    """Tests that the median function raises ValueError for empty list"""
    with pytest.raises(ValueError):
        median([])


def test_median_leaves_original_data_unchanged():
    """Tests that the median function doesn't change the original input data"""
    data = [4, 3, 6, 2, 7, 8]
    median(data)
    assert data == data


def test_median_for_both_tuple_and_list():
    """
    Tests that the median function works for a tuple and a list with the
    same elements.
    """
    data = [4, 3, 6, 2, 7, 8]
    assert median(data) == median(tuple(data))


def test_median_float_list():
    """Tests that the median function works for a list with float elements"""
    float_list = [3.7, 4.1, 2.5, 7.4, 9.0]
    assert median(float_list) == 4.1
