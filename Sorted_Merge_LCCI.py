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


class Solution2:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify A in-place instead.
        """
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted.append(A[pa])
                pa += 1
            else:
                sorted.append(B[pb])
                pb += 1
        A[:] = sorted


class Solution3:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify A in-place instead.
        """
        pa, pb = m - 1, n - 1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1
