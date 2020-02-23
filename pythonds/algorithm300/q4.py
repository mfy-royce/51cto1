#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: q4.py
@time:  8:53
@welcom to learn ai
"""


class TwoSum:
    data = []

    def add(self, number):
        self.data.append(number)

    def find(self, target):
        self.data.sort()
        left = 0
        right = len(self.data) - 1
        while right - left > 0:
            if self.data[left] + self.data[right] == target:
                return True
            if self.data[left] + self.data[right] < target:
                left += 1
            else:
                right -= 1
        return False


class Solution():
    def three_sum_closest(self, nums, target):
        nums.sort()
        ans = None
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while right > left:
                sum = nums[left] + nums[right] + nums[i]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                    if ans == target:
                        return ans
                if sum < target:
                    left += 1
                else:
                    right -= 1

        return ans

    def three_sum_zero(self, nums):
        res = []
        if len(nums) <= 3:
            return res
        nums.sort()
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            left = i
            right = len(nums) - 1
            while right > left:
                if nums[left] + nums[right] == target:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res

    def four_sum(self, nums, target):
        nums.sort()
        res = []
        if len(nums) < 4:
            return res
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                goal = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    if nums[left] + nums[right] == goal:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while right > left and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > goal:
                        right -= 1
                    else:
                        left += 1
        return res

    def dices_sum(self, n):
        res = []
        probility_matrix = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            probility_matrix[1][i] = 1 / 6
        for i in range(2, n + 1):
            for j in range(i, 6 * n + 1):
                for k in range(1, 7):
                    if j > k:
                        probility_matrix[i][j] += probility_matrix[i - 1][j - k]
                probility_matrix[i][j] /= 6
        for i in range(n, 6 * n + 1):
            res.append((i, probility_matrix[n][i]))
        return res

    def k_sum(self, nums, k, target):
        n = len(nums)
        dp = [
            [[0] * (target + 1) for _ in range(k + 1)],
            [[0] * (target + 1) for _ in range(k + 1)]
        ]
        dp[0][0][0] = 1
        dp[1][0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(k + 1, i + 1)):
                for s in range(1, target + 1):
                    dp[i % 2][j][s] = dp[(i - 1) % 2][j][s]
                    if s >= nums[i - 1]:
                        dp[i % 2][j][s] += dp[(i - 1) % 2][j - 1][s - nums[i - 1]]
        return dp[n % 2][k][target]

    def add_binary(self, s1, s2):
        s1_idx = len(s1) - 1
        s2_idx = len(s2) - 1
        carry = 0
        res = ""
        while s1_idx >= 0 or s2_idx >= 0:
            if s1_idx >= 0:
                a1 = int(s1[s1_idx])
            else:
                a1 = 0
            if s2_idx >= 0:
                a2 = int(s2[s2_idx])
            else:
                a2 = 0
            if (a1 + a2 + carry) & 1 == 1:
                res = "1" + res
            else:
                res = "0" + res
            carry = (a1 + a2 + carry) // 2
            s1_idx -= 1
            s2_idx -= 1
        if carry == 1:
            res = "1" + res
        return res

    def add_digit(self, num):
        self.num = str(num)
        self.num = map(int, self.num)
        self.num = list(self.num)
        self.num = sum(self.num)
        if self.num < 10:
            return self.num
        else:
            return self.add_digit(self.num)

    def zigzag(self, matrix):
        """
        row + col sum is even  move  up right ， row -1 and col+1  ,     col increace first
                      is odd move down left ,   row +1  and col -1 ,    row increace first


        :param matrix:
        :return:
        """
        row = len(matrix)
        col = len(matrix[0])
        x = 0
        y = 0
        up = 1
        res = []
        for i in range(row * col):
            res.append(matrix[x][y])
            if up:
                nextx = x - 1
                nexty = y + 1
            else:
                nextx = x + 1
                nexty = y - 1
            if nextx not in range(row) or nexty not in range(col):
                if up:
                    if nexty < col:
                        nextx, nexty = x, y + 1
                    else:
                        nextx, nexty = x + 1, y
                else:
                    if nextx < row:
                        nextx, nexty = x + 1, y
                    else:
                        nextx, nexty = x, y + 1
                up = False if up else True
            x, y = nextx, nexty
        return res

    def submatrix_sum(self, matrix):
        depth = len(matrix)
        wide = len(matrix[0])
        prefixsum = [[0] * (wide + 1) for _ in range(depth + 1)]
        for dy in range(1, depth + 1):
            for dx in range(1, wide + 1):
                prefixsum[dy][dx] = prefixsum[dy - 1][dx] + prefixsum[dy][dx - 1] - prefixsum[dy - 1][dx - 1] \
                                    + matrix[dy - 1][dx - 1]
                for y in range(0, dy):
                    for x in range(0, dx):
                        if prefixsum[dy][dx] == prefixsum[y][dx] + prefixsum[dy][x] - prefixsum[y][x]:
                            return ((y, x), (dy - 1, dx - 1))

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

    def searchmatrix_2(self, matrix , target):
        row  = len(matrix)
        col = len(matrix[0])
        i = row- 1
        j = 0
        count = 0
        while i >=0 and j < col:
            ref =  matrix[i][j]
            if target > ref:
                j +=1
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
                if matrix[i][j]== 0:
                    rowzero[i] , colzero[j] = True,True

        for i in range(row):
            for j in range(col):
                if rowzero[i] or colzero[j] :
                    matrix[i][j] = 0
        return matrix

    def findrepeatDNA_1(self,s):
        res = set()
        n  = len(s)
        dp= [[0] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1 , n + 1):
                if i == j:
                    dp[i][j] = 0
                elif s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] ==10:
                    res.add(s[i-10 : i])
        return res

    def findrepeatDNA_2(self,s):
        res =[]
        s_dict = {}
        for i in range(len(s)-9):
            key= s[i:i+10]
            if key not in s_dict:
                s_dict[key] = 1
            else:
                s_dict[key] += 1
            if s_dict[key] == 2:
                res.append(key)
        return  res



#import numpy as np


def main():
    solution = Solution()

    # print("quickSort is {}".format(solution.quickSort(iList,0,len(iList)-1)))
    # sortVerify(1000,20,solution.quickSort)

    ##    print("tailing_zeros is {}".format(solution.tailing_zeros(25)))
    list = []
    twosum = TwoSum()
    twosum.add(1)
    twosum.add(3)
    twosum.add(5)

    list.append(twosum.find(4))
    list.append(twosum.find(7))
    print(list)

    print("three_sum_closest is {}".format(solution.three_sum_closest([-1, 2, 1, -4], 1)))

    print("three_sum_zero is {}".format(solution.three_sum_zero([3, 0, 2, -5, 1])))  # [-1, -1, 1, 1, 2, -2]

    print("four_sum is {}".format(solution.four_sum([1, 2, 3, 4, 5, 1], 10)))  # [-1, -1, 1, 1, 2, -2]

    print("dices_sum is {}".format(solution.dices_sum(2)))  # [-1, -1, 1, 1, 2, -2]

    print("add_binary is {}".format(solution.add_binary("1", "10")))  # [-1, -1, 1, 1, 2, -2]

    print("add_digit is {}".format(solution.add_digit(38)))  # [-1, -1, 1, 1, 2, -2]

    print("k_sum is {}".format(solution.k_sum([1, 2, 3, 4], 2, 5)))  # [-1, -1, 1, 1, 2, -2]

    print("zigzag is {}".format(solution.zigzag([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])))  # [-1, -1, 1, 1, 2, -2]

    print("submatrix_sum is {}".format(solution.submatrix_sum([[0, 5, 7], [3, 7, -8], [4, -8, 9]])))  # [-1, -1, 1, 1, 2, -2]

    print("searchmatrix is {}".format(solution.searchmatrix_1([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 4)))  # [-1, -1, 1, 1, 2, -2]


    print("searchmatrix_2 is {}".format(solution.searchmatrix_2([[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]], 10)))  # [-1, -1, 1, 1, 2, -2]

    print("set_zero is {}".format(solution.set_zero([[1, 3, 0, 7], [2, 4, 7, 8], [3, 5, 9, 10]])))  # [-1, -1, 1, 1, 2, -2]

    print("findrepeatDNA is {}".format(solution.findrepeatDNA_2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))  # [-1, -1, 1, 1, 2, -2]

if __name__ == "__main__":
    main()
