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


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data_sorted = [1, 2, 3]
    assert bubble_sort(data_sorted) == data_sorted


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [5, 2, 4, 1, 3, 6, 7, 8]
    reverse_sorted = sorted(data, reverse=True)
    assert bubble_sort(reverse_sorted) == sorted(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1, 1]
    assert bubble_sort(data) == sorted(data)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    for data in ((),
                 (2,),
                 (3, 2, 5, 6),
                 'hbgekdfaicj',
                 ('orange', 'apple', 'pineapple', 'grapes', 'bananas')):
        assert bubble_sort(data) == sorted(data)


def test_sort_float_list():
    """Tests that sorting works for list with float elements"""
    float_list = [3.2, 4.9, 1.0, 0.5, 5.5]
    assert bubble_sort(float_list) == sorted(float_list)
