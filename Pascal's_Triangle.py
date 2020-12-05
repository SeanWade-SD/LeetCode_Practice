# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows=5):
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = [[1], [1, 1]]
        m = [1, 1]
        for k in range(3, (numRows+1)):                          
            r = [1]
            q = []
            for i in range(0, (len(m) - 1)):
                q.append(m[i] + m[i + 1])
            r.extend(q)
            r.append(1)

        return result



class Solution1:
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res

# 观察一下规律，发现当前一行只比上一行多了一个元素，最最关键的一点：本行元素等于上一行元素往后错一位再逐个相加：