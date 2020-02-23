#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: segtree.py
@time:  19:21
@welcom to learn ai
"""

class Segtree():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.count = 0
        if start != end:
            self.left = Segtree(start, (start + end) // 2)
            self.right = Segtree((start + end) // 2 + 1, end)

    def sum(self, start, end):
        if start <= self.start and end >= self.end:
            return self.count
        if self.start == self.end:
            return 0
        if end <= self.left.end:
            return self.left.sum(start, end)
        if start >= self.right.start:
            return self.right.sum(start, end)
        return self.left.sum(start, self.left.end) + self.right.sum(self.right.start, end)

    def inc(self, index):
        if index < self.start or index > self.end:
            return
        if self.left == self.right:
            self.count += 1
            return
        if index <= self.left.end:
            self.left.inc(index)
        if index >= self.right.start:
            self.right.inc(index)
        self.count = self.left.count + self.right.count