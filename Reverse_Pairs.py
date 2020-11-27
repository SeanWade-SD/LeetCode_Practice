# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/reverse-pairs
import bisect


class Solution:
    def reversePairs(self, nums = [2,4,3,5,1]):
        n = 0
        for i in range(len(nums)-1):
            if nums[i]/2 > nums[i+1:]:
                n += 1
        return n

class Solution1:
    def reversePairs(self, nums= [1,8,2,3,1]):
        tb, res = [], 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            bisect.insort_left(tb, n2)

        return res


# 我们倒序遍历 nums，遍历过的数我们将它 \times 2×2，放入 tb 中，同时保持 tb 是按升序排列的。
# 因此对于 nums 中的任意一个 n，此时已经在 tb 中的元素都是在原数组中位于 n 之后的元素，这样就保证了 i < ji<j。
# 我们再找到 2\times n2×n 在 tb 中的插入位置索引，该位置之前的就是满足题意的元素，因此我们累加这个索引就可以得到答案。

