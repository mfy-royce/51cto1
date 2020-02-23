#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: q5.py
@time:  16:01
@welcom to learn ai
"""


class Solution():
    def searchmatrix_1(self, matrix, target):
        x = 0
        y = len(matrix[0]) - 1

        while y >= 0 and x <= len(matrix) - 1:
            ref = matrix[x][y]
            if target > ref:
                x += 1
            elif target < ref:
                y -= 1
            else:
                return True
        return False

    def searchmatrix_2(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        i = row - 1
        j = 0
        count = 0
        while i >= 0 and j < col:
            ref = matrix[i][j]
            if target > ref:
                j += 1
            elif target < ref:
                i -= 1
            elif target == ref:
                count += 1
                i -= 1
                j += 1
        return count

    def set_zero(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        rowzero = [False for _ in range(row)]
        colzero = [False for _ in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowzero[i], colzero[j] = True, True

        for i in range(row):
            for j in range(col):
                if rowzero[i] or colzero[j]:
                    matrix[i][j] = 0
        return matrix

    def findrepeatDNA_1(self, s):
        res = set()
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j] = 0
                elif s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] == 10:
                    res.add(s[i - 10: i])
        return res

    def findrepeatDNA_2(self, s):
        res = []
        s_dict = {}
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key not in s_dict:
                s_dict[key] = 1
            else:
                s_dict[key] += 1
            if s_dict[key] == 2:
                res.append(key)
        return res

    def spiralorder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        mx = [[False] * (m+2) for _ in range(n + 2)]
        for i in range(n + 2):
            mx[i][0],mx[i][m+1] = True, True
        for i in range(m + 2):
            mx[0][i], mx[n+1][i] = True,True
        x =1
        y =1
        res =[]
        direct = 0
        dir =[[0,1],[1,0],[0,-1],[-1,0]]
        for k in range(n * m):
            mx[x][y] = True
            res.append(matrix[x-1][y-1])
            nextx = x + dir[direct][0]
            nexty = y + dir[direct][1]
            if  mx[nextx][nexty]:
                direct=(direct +1)  % 4
                nextx = x + dir[direct][0]
                nexty = y + dir[direct][1]
            x = nextx
            y = nexty
        return res


def main():
    solution = Solution()

    print("searchmatrix is {}".format(
        solution.searchmatrix_1([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 4)))  # [-1, -1, 1, 1, 2, -2]

    print("searchmatrix_2 is {}".format(
        solution.searchmatrix_2([[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]], 10)))  # [-1, -1, 1, 1, 2, -2]

    print("set_zero is {}".format(solution.set_zero([[1, 3, 0, 7], [2, 4, 7, 8], [3, 5, 9, 10]])))  # [-1, -1, 1, 1, 2, -2]

    print("findrepeatDNA is {}".format(solution.findrepeatDNA_2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))  # [-1, -1, 1, 1, 2, -2]

    print("spiralorder is {}".format(solution.spiralorder([[1,2,3],[4,5,6],[7,8,9]])))  # [-1, -1, 1, 1, 2, -2]


if __name__ == "__main__":
    main()
