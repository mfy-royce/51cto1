#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: q3.py
@time:  19:49
@welcom to learn ai
"""


from pythonds.algorithm300.segtree import Segtree


class Solution():
    def count_small_number(self, nums):
        if len(nums) == 0:
            return []
        res = []
        max_num = max(nums)
        root = Segtree(0, max_num)
        for i in nums:
            res.append(root.sum(0, i - 1))
            root.inc(i)
        return res

    def tailing_zeros(self, k):
        n = k
        n_sum = 1
        sum = 0
        while n >= 5:
            n //= 5
            sum += n
        for i in range(k):
            n_sum *= (i + 1)
        return sum, n_sum

    def digit_count(self, k, n):
        count = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    count += 1
                j //= 10
                if j == 0:
                    break
        return count

    def delete_digit(self, s, k):
        stack = []
        remain_n = len(s) - k
        for i, digit in enumerate(s):
            while stack and stack[-1] > digit and i - len(stack) < k:
                stack.pop()
            stack.append(digit)
        return stack[:remain_n]

    def find_miss_number(self, n, s):

        str_n = "".join([str(i) for i in range(1, n + 1)])
        number_dict = {}
        for c in str_n:
            if c not in number_dict:
                number_dict[c] = 1
            else:
                number_dict[c] += 1
        for c in s:
            number_dict[c] -= 1
            if number_dict[c] == 0:
                number_dict.pop(c)
        keys_list = list(number_dict.keys())
        res_str = "".join(keys_list)

        if int(res_str) >= 1 and int(res_str) <= n and res_str not in s:
            return res_str
        else:
            return res_str[::-1]

    def is_ugly(self, n):
        if n < 1:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        if n == 1:
            return True
        else:
            return False

    def nth_ugly_number(self, n):
        import heapq
        heap = [1]
        heap_set = set(heap)
        primes = [2, 3, 5]
        for i in range(n):
            minhp = heapq.heappop(heap)
            for p in primes:
                item = p * minhp
                if item not in heap_set:
                    heapq.heappush(heap, item)
                    heap_set.add(item)
        return minhp

    def nth_supper_ugly_number_dp(self, n, primes):  # 动态规划
        p_to_u_index = [0] * len(primes)  # 状态
        ugly_number = [1] * n  # 所求
        for j in range(1, n):
            for i, prime in enumerate(primes):
                alternative = prime * ugly_number[p_to_u_index[i]]
                if i == 0:
                    min = alternative
                elif min > alternative:
                    min = alternative
            ugly_number[j] = min
            for i, prime in enumerate(primes):
                alternative = prime * ugly_number[p_to_u_index[i]]
                if min == alternative:
                    p_to_u_index[i] += 1
        return ugly_number[n - 1]

    def nth_supper_ugly_number(self, n, primes):
        import heapq
        p_to_u_index = [0] * len(primes)  # 状态
        ugly_number = [1] * n  # 所求
        heap = []
        heap_set = set()
        for idx, prime in enumerate(primes):
            heapq.heappush(heap, (prime, idx))
            heap_set.add(prime)

        for j in range(1, n):
            ugly_number[j], idx = heapq.heappop(heap)
            p_to_u_index[idx] += 1
            new_ugly = ugly_number[p_to_u_index[idx]] * primes[idx]
            if new_ugly in heap_set:
                p_to_u_index[idx] += 1
                new_ugly = ugly_number[p_to_u_index[idx]] * primes[idx]
            else:
                heapq.heappush(heap, (new_ugly, idx))
                heap_set.add(new_ugly)

        return ugly_number[-1]

    def two_sum_1(self, nums, target):
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = i
        for i, num in enumerate(nums):
            if target - num in hash:
                if hash[target - num] < i:
                    return (hash[target - num], i)
                else:
                    return (i, hash[target - num])
        return (-1, -1)

    def two_sum_2(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            res = target - nums[left]
            if res == nums[right]:
                return (left + 1, right + 1)
            elif res < nums[right]:
                right -= 1
            else:
                left += 1
        return (-1, -1)


def main():
    solution = Solution()

    # print("quickSort is {}".format(solution.quickSort(iList,0,len(iList)-1)))
    # sortVerify(1000,20,solution.quickSort)

    print("tailing_zeros is {}".format(solution.tailing_zeros(25)))

    print("digit_count is {}".format(solution.digit_count(1, 12)))

    print("delete_digit is {}".format(solution.delete_digit("134542", 3)))

    print("find_miss_number is {}".format(solution.find_miss_number(20, "19201234567891011121314151618")))

    print("is_ugly is {}".format(solution.is_ugly(7)))

    print("nth_ugly_number is {}".format(solution.nth_ugly_number(10)))

    print("nth_supper_ugly_number is {}".format(solution.nth_supper_ugly_number(6, [2, 7, 13, 19])))

    print("two_sum is {}".format(solution.two_sum_1([5, 4, 3, 11], 5)))

    print("two_sum is {}".format(solution.two_sum_2([2, 7, 11, 15], 9)))

    print("count_small_number is {}".format(solution.count_small_number([1, 2, 7, 8, 5])))
if __name__ == "__main__":
    main()
