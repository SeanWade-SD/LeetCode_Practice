# Given an array nums sorted in ascending order,
# return true if and only if you can split it into 1 or more subsequences such that each subsequence
# consists of consecutive integers and has length at least 3.

# Example 1:
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
#
# Input: [1,2,3,4,4,5]
# Output: False
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
import collections
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())






