# -*- coding: utf-8 -*-

"""
Acceptance test suite for EX04.
Your code should pass these tests before submission.

Source: https://github.com/yngvem/INF200-2019-Exercises/blob/master/src
/YOUR_NAME_ex/ex04/test_ex04.py
"""

import pytest
from src.christine_brinchmann_ex.ex04.myrand import LCGRand, ListRand
from src.christine_brinchmann_ex.ex04.walker import Walker

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def test_lcg():
    """Test that LCG generator works."""

    lcg = LCGRand(346)
    assert lcg.rand() == 5815222
    assert lcg.rand() == 1099672039


def test_list_rng():
    """Test that ListRNG generator works."""
    numbers = [4, 5, 29, 11]
    lr = ListRand(numbers)
    assert [lr.rand() for _ in range(len(numbers))] == numbers
    with pytest.raises(RuntimeError):
        lr.rand()


def test_walker():
    """Test that Walker class can be used as required."""

    start, home = 10, 20
    w = Walker(start, home)
    assert not w.is_at_home()
    w.move()
    assert w.get_position() != start
    w.move()
    assert w.get_steps() == 2
