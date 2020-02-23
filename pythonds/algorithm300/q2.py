#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: q2.py
@time:  23:34
@welcom to learn ai
"""


class Solution():

    def k_closest_number(self, ilist, target, k):
        # for i, num in enumerate(ilist):
        #     if num > target:
        #         right = i
        #         break
        #     else:
        #         right = i + 1
        right = self.binary_search(ilist,target)
        left = right - 1
        result = []
        for i in range(k):
            if left < 0:
                result.append(ilist[right])
                right += 1
                continue
            if right >= len(ilist):
                result.append(ilist[left])
                left -= 1
                continue
            if target - ilist[left] <= ilist[right] - target:
                result.append(ilist[left])
                left -= 1
            else:
                result.append(ilist[right])
                right += 1
        return result

    def intersect(self, ilist):
        pos_index = 0
        neg_index = 1
        while pos_index < len(ilist) or neg_index <len(ilist):
            if pos_index < len(ilist) and ilist[pos_index] > 0:
                pos_index += 2
            if neg_index < len(ilist) and ilist[neg_index] < 0:
                neg_index += 2
            if pos_index < len(ilist) and ilist[pos_index] < 0 and neg_index < len(ilist) and ilist[neg_index] > 0:
                ilist[pos_index], ilist[neg_index] = ilist[neg_index], ilist[pos_index]
        if ilist[-1] < 0 :
            ilist.insert(0,ilist.pop())
        return ilist


    def nextGreaterElement(self,nums):
        if not nums:
            return []
        stack = []
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index  = stack.pop()
                res[index] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index  = stack.pop()
                res[index] = nums[i]
            stack.append(i)
            if stack[0] == stack[-1]:
                break
        return res

    def single_number_a(self,nums):
        ans = 0
        for i in nums:
            ans ^= i
        return ans

    def single_number_b(self,nums):
        nums_dict = {}
        ans = 0
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
                if nums_dict[i] == 3:
                    nums_dict.pop(i)
        return nums_dict.popitem()[0]

    def single_number_c(self,nums):
        nums_set = set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                nums_set.remove(i)
        return nums_set

    def single_number_d(self,nums):
        i =  1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            i += 2
        return nums[-1]

    def symmetry_number(self,n):
        if n <=0:
            return []
        if n % 2 == 0:
            base = [""]
            i= 0
        else:
            base = ["0","1","8"]
            i = 1

        temp =[["0","0"],["1","1"],["8","8"],["6","9"],["9","6"]]
        res =  base
        while i < n:
            res =[]
            for num in base:
                for add_list in temp:
                    res.append("".join([add_list[0],num,add_list[-1]]))
            base= res
            i += 2

        return res

    def issymmetry_number(self,s):
        left  = 0
        right = len(s) - 1
        map_dict = { "0":"0" , "1":"1" , "8":"8" , "6":"9" , "9":"6" }
        while right >left:
            if map_dict[s[right]] !=s[left]:
                return False
            right -= 1
        return True

    def binary_search(self,nums,q):
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid  =  (left + right) // 2
            if nums[mid] < q:
                left  = mid
            else:
                right = mid
        if nums[left] >= q:
            return left
        if nums[right] >= q:
            return right
        return right + 1

    def counter_smaller_number(self,nums,queries):
        sorted_nums = sorted(nums)
        res = []
        for num in queries:
            res.append(self.binary_search(sorted_nums,num))
        return res


def main():
    # iList= randomList(30)
    # iList = [87, 61, 4, 2, 64]
    # iList =[4, 86, 4, 24, 0]
    # iList = []
    # iList =[10, 70, 14, 48, 28, 85, 8]
    # iList =[81, 11, 31, 18, 8, 81, 85, 81, 77]
    # print("iList is {}".format(iList))

    solution = Solution()

    # print("quickSort is {}".format(solution.quickSort(iList,0,len(iList)-1)))
    # sortVerify(1000,20,solution.quickSort)

    print("k_closest_number is {}".format(solution.k_closest_number([1, 4, 6, 8], 3, 3)))

    print("intersect is {}".format(solution.intersect([2, -4, 6, 8, -10])))

    print("nextGreaterElement is {}".format(solution.nextGreaterElement([1 , 2, 1])))

    print("single_number_a is {}".format(solution.single_number_a([4, 6 , 4, 6, 3])))

    print("single_number_b is {}".format(solution.single_number_b([4, 6 , 4, 6, 3, 4, 6])))

    print("single_number_c is {}".format(solution.single_number_c([1,2,2,3,4,4,5,3])))

    print("single_number_d is {}".format(solution.single_number_d([1,1,2,2,4,4,5,5,3])))

    print("symmetry_number is {}".format(solution.symmetry_number(4)))

    print("issymmetry_number is {}".format(solution.issymmetry_number("68")))

    print("counter_smaller_number is {}".format(solution.counter_smaller_number([1,2,7,8,5],[1,8,5])))


if __name__ == "__main__":
    main()
