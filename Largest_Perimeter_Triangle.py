# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area,
# formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0.
#
# Example 1:
#
# Input: [2,1,2]
# Output: 5
# Example 2:
#
# Input: [1,2,1]
# Output: 0
# Example 3:
#
# Input: [3,2,3,4]
# Output: 10
# Example 4:
#
# Input: [3,6,2,3]
# Output: 8
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/largest-perimeter-triangle


class Solution:
    def largestPerimeter(self, A):
        if len(A)<3:
            return 0
        A.sort()
        for i in range(len(A)-1,1,-1):
            if A[i]<A[i-1]+A[i-2]:
                return A[i]+A[i-1]+A[i-2]
        return 0


class Solution1:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        return next((x+y+z for x, y, z in zip(A, A[1:], A[2:]) if x<y+z), 0)



