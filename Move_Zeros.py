#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,0,0,1,0,3,12]
# Output: [1,3,12,0,0,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/move-zeroes


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        m = len(nums)
        k = 0

        while m > 0:
            if nums[k] == 0:
                nums.pop(k)
                nums.append(0)

            else:
                k += 1
            m -= 1


class Solution1:
    def moveZeroes(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
            right += 1
            print(nums)


# 使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
# 右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。
# 注意到以下性质：
# 左指针左边均为非零数；
# 右指针左边直到左指针处均为零。
# 因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变
# [0, 0, 0, 1, 0, 3, 12]
# [0, 0, 0, 1, 0, 3, 12]
# [0, 0, 0, 1, 0, 3, 12]
# [1, 0, 0, 0, 0, 3, 12]
# [1, 0, 0, 0, 0, 3, 12]
# [1, 3, 0, 0, 0, 0, 12]
# [1, 3, 12, 0, 0, 0, 0]

s = Solution1()
nums = [0,0,0,1,0,3,12]
s.moveZeroes(nums)