# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
# there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/4sum-ii
import collections


class Solution:
    def fourSumCount(self, A=[ 1, 2], B=[-2,-1], C=[-1, 2], D=[ 0, 2]):
        n = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        if A[i] + B[j] + C[k] + D[l] == 0:
                            n += 1

        return n


class Solution1:
    def fourSumCount(self, A=[ 1, 2], B=[-2,-1], C=[-1, 2], D=[ 0, 2]):
        countAB = collections.Counter(u + v for u in A for v in B)
        print(countAB)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans


S = Solution1()
print(S.fourSumCount())






