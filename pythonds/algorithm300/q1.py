#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: q1.py
@time:  17:41
@welcom to learn ai
"""
class Solution():

    def quickSort(self,iList,start,end):
        if start >= end:
            return
        l = start+1
        r = end
        while r>=l:
            while r>=l and iList[start] <= iList[r]:
                r -= 1
            while r >=l and iList[start] >= iList[l]:
                l += 1
            if r > l:
                iList[l],iList[r] = iList[r],iList[l]
        #if iList[start] < iList[r]:
        #    r -= 1
        iList[start], iList[r] = iList[r], iList[start]

        self.quickSort(iList,start,r-1)
        self.quickSort(iList,r+1,end)
        return iList

    def integerReplacement(self,n):
        memo={}
        self.dfs(n,memo)
        print(memo[n])
        return len(memo[n])-1

    def dfs(self,n,memo):
        if n == 1:
            memo[n] = [1]

        if n in memo:
            return memo[n]

        temp = []
        if n % 2 == 0:
            temp.append(n)
            cur = self.dfs(n//2,memo)
            temp.extend(cur)
            memo[n] = temp
            return  temp
        else:
            temp2 =  temp.copy()
            temp.append(n)
            cur = self.dfs(n +1, memo)
            temp.extend(cur)

            temp2.append(n)
            cur2 =self.dfs(n -1 ,memo)
            temp2.extend(cur2)

            if len(temp) < len(temp2):
                memo[n] = temp
                return temp
            else:
                memo[n]= temp2
                return temp2

    def devide(self,dividend,divisor):
        INT_MAX = 2147483647
        if divisor ==0:
            return INT_MAX
        a =abs(dividend)
        b = abs(divisor)
        shift =31
        ans = 0
        while shift >= 0:
            if a >= b<<shift:
                a -= b<<shift
                ans += 1<<shift
            shift -=1
        if dividend >0 and divisor<0 or dividend<0 and divisor>0:
            ans = - ans

        if ans > INT_MAX:
            return INT_MAX
        return ans

    def aPlusB(self,a,b):
        while b !=0:
            a,b = a^b, a&b<<1
        return  a

    def mergeNumber(self,iList):
        import heapq
        Q = []
        ans = 0
        for i in iList:
            heapq.heappush(Q,i)
        while len(Q)>1:
            a = heapq.heappop(Q)
            b = heapq.heappop(Q)
            heapq.heappush(Q,a+b)
            ans += a+b
        return ans

    def isNumber(self,s):
        INVALID = 0
        SPACE = 1
        SIGN = 2
        NUMBER =  3
        DOT =4
        EXPONENT = 5
        transitionTable = [
        #invalid spa sign num dot exp
            [-1,  0,  3,  1,  2, -1],  # 0 空格
            [-1,  8, -1,  1,  4,  5],  # 1 数字
            [-1, -1, -1,  4, -1, -1],  # 2 只有小数点
            [-1, -1, -1,  1,  2, -1],  # 3 符号
            [-1,  8, -1,  4, -1,  5],  # 4 小数点 + 数字
            [-1, -1,  6,  7, -1, -1],  # 5 e
            [-1, -1, -1,  7, -1, -1],  # 6 e后符号
            [-1,  8, -1,  7, -1, -1],  # 7 e后数字
            [-1,  8, -1, -1, -1, -1],  # 8 输入后空格
        ]
        state = 0
        for i in s:

            if i == " ":
                chartype = SPACE
            elif i == "-" or i == "+":
                chartype = SIGN
            elif i in "0123456789":
                chartype = NUMBER
            elif i == '.' :
                chartype = DOT
            elif i == "e" or i =="E":
                chartype =  EXPONENT
            else:
                chartype = INVALID

            state = transitionTable[state][chartype]
            if state == -1:
                return False
        return  state  == 1 or state ==4 or state  ==7 or state == 8

    def nextSparseNumber(self,x):
        s=  bin(x)[2:]

        while True:
            position  = -1
            for  i in range(len(s)-1):
                if s[i]==s[i+1]=="1":
                    position = i
                    break
            if position == -1:
                return int(s,2)
            if position == 0:
                s = "1" + "0" * (len(s) - position)
            else:
                s = s[:position-1] + "1" + "0" * (len(s) - position)

    def maxSlidingWindow(self,nums,k):
        from collections import deque
        if not k or not nums:
            return []
        dq = deque([])
        for i in range(k-1):
            self.push(dq,nums,i)
        result = []
        for j in range(k-1,len(nums)):
            self.push(dq,nums,j)
            result.append(nums[dq[0]])
            if j-k+1 ==dq[0]:
                dq.popleft()
        return result

    def push(self,dq,nums,i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

    def maxNumber(self,nums1,nums2,k):
        len1 = len(nums1)
        len2 = len(nums2)
        ans = []
        for x in range(max(0,k- len2),min(k,len1)+1):
            temp =  self.merge(self.getMax(nums1,x), self.getMax(nums2,k-x))
            ans = max(ans,temp)
        return ans

    def getMax(self,nums,x):
        ans =[]
        for i,num in enumerate(nums):
            if ans and len(ans)+ len(nums) - i   > x and ans[-1] <num:
                ans.pop()
            if len(ans) < x:
                ans.append(num)
        return ans

    def merge(self,nums1,nums2):
        return [max(nums1,nums2).pop(0) for _ in nums1+ nums2]


def main():
    from pythonds.test import randomList,sortVerify
    # iList= randomList(30)
    #iList = [87, 61, 4, 2, 64]
    #iList =[4, 86, 4, 24, 0]
    #iList = []
    #iList =[10, 70, 14, 48, 28, 85, 8]
    #iList =[81, 11, 31, 18, 8, 81, 85, 81, 77]
    # print("iList is {}".format(iList))

    solution = Solution()
    # print("quickSort is {}".format(solution.quickSort(iList,0,len(iList)-1)))
    # sortVerify(1000,20,solution.quickSort)

    # print("integerReplacement is {}".format(solution.integerReplacement(18)))

    print("devide is {}".format(solution.devide(21,3)))

    print("aPlusB is {}".format(solution.aPlusB(8,18)))

    print("mergeNumber is {}".format(solution.mergeNumber([6,7,8,9,10])))

    print("isNumber is {}".format(solution.isNumber("23")))

    print("nextSparseNumber is {}".format(solution.nextSparseNumber(50)))

    print("maxSlidingWindow is {}".format(solution.maxSlidingWindow([2,6,5,3,1,8],2)))

    print("maxNumber is {}".format(solution.maxNumber([1,-1,-2,1],[3,-2,2,1],3)))
    print("maxNumber is {}".format(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8 ,3], 5)))
    print("maxNumber is {}".format(solution.maxNumber([6, 7], [6,0,4], 5)))
    print("maxNumber is {}".format(solution.maxNumber([3, 9], [8,9], 3)))

if __name__ == "__main__":
    main()