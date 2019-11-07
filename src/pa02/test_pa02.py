# -*- coding: utf-8 -*-

__author__ = 'Christine Brinchmann', 'Marie Kolvik Valøy'
__email__ = 'christibr@nmbu.no', 'mvaloy@nmbu.no'

import src.pa02.snakes_simulations as ss


class TestPBoard2:
    """Tests that Board works as supposed."""

    def test_goal_reached(self):
        board = ss.Board(goal=100)
        assert board.goal_reached(5) is False

    def test_position_adjustment(self):
        board = ss.Board()
        assert board.position_adjustment(8) == 10-8

        assert board.position_adjustment(56) == 56-37
