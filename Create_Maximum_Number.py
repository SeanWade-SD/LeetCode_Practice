# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array must be preserved. Return an array of the k digits.
#
# Note: You should try to optimize your time and space complexity.
#
# Example 1:
#
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]

# Example 2:
#
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
# Example 3:
#
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/create-maximum-number


class Solution:
    def maxNumber(self, nums1=[6, 7], nums2= [6, 0, 4], k=5):
        T = []
        T.extend(nums1)
        T.extend(nums2)
        T = sorted(T, reverse=True)
        print(T)
        index1 = -1
        index2 = -1
        result = []

        while len(result) < k:
            if T[0] in nums1:
                if nums1.index(T[0]) > index1:
                    index1 = nums1.index(T[0])
                    result.append(T[0])

            if T[0] in nums2:
                if nums2.index(T[0]) > index2:
                    index2 = nums2.index(T[0])
                    result.append(T[0])

            T.pop(0)




class Solution1:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))



