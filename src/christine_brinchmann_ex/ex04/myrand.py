# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        self.r = seed

    def rand(self):
        a = 7**5
        m = 2**31-1
        self.r = (a * self.r) % m
        return self.r


class ListRand:
    def __init__(self, num_list):
        self.num_list = num_list
        self.n = -1

    def rand(self):
        self.n += 1
        if self.n < len(self.num_list):
            return self.num_list[self.n]
        else:
            raise RuntimeError('No more elements in list')
