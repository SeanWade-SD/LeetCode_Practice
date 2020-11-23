# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.
#
# Initially the number of elements in A and B are m and n respectively.
#
# Example:
#
# Input:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/sorted-merge-lcci
#

class Solution:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify A in-place instead.
        """
        i = m
        k = 0
        while i < m+n:
            A[i] = B[k]
            i += 1
            k += 1
        A.sort()

        print(A)


class Solution1:
    def merge(self, A, m, B):

        A[m:] = B
        A.sort()

