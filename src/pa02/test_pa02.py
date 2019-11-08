# -*- coding: utf-8 -*-
import random

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

        assert board.position_adjustment(56) == 37-56

        assert board.position_adjustment(63) == 0


class TestPlayer2:
    """Tests that Player works as supposed."""

    def test_move(self):
        player = ss.Player()
        assert player.position == 0, 'Start position is not 0'
        random.seed(2)
        player.move()
        assert player.position > 0, 'The player has not moved'
        assert player.position != 1, 'The player cant be at the bottom of a ' \
                                     'ladder'
        random.seed(1)
        player.move()
        assert player.position != 42, 'The player cant be at the top of a ' \
                                      'snake'


class TestResilientPlayer2:
    """Tests that ResilientPlayer works as supposed."""
    def test_move(self):
        """Test that ResilientPlayer takes one extra step after sliding
        down a snake"""
        player = ss.ResilientPlayer()
        random.seed(2)
        player.move()
        random.seed(1)
        player.move()
        random.seed(2)
        player.move()
        assert player.position == 32


class TestLazyPlayer2:
    """Tests that ResilientPlayer works as supposed."""
    def test_move(self):
        """
        Test that LazyPlayer takes one step less after going up a ladders.
        """
        player = ss.LazyPlayer()
        random.seed(2)
        player.move()
        random.seed(1)
        player.move()
        assert player.position == 41
