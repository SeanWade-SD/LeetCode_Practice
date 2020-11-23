# There are some spherical balloons spread in two-dimensional space. For each balloon,
# provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal,
# y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice.
# The start is always smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
# There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend],
# return the minimum number of arrows that must be shot to burst all balloons.

# Example 1:
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6])
# and another arrow at x = 11 (bursting the other two balloons).
# Example 2:
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Example 3:
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Example 4:
#
# Input: points = [[1,2]]
# Output: 1
# Example 5:
#
# Input: points = [[2,3],[2,3]]
# Output: 1
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points):
        if len(points) == 1:
            return 1

        m = 0

        while m < len(points) - 1:
            n = m + 1
            while n < len(points):

                if (points[n][0] <= points[m][0]) & (points[m][1] <= points[n][1]):
                    points.pop(n)

                if (points[n][0] <= points[m][0]) & (points[m][0] <= points[n][1]) & (points[m][1] >= points[n][1]):
                    points[m][1] = points[n][1]

                    points.pop(n)

                if (points[m][0] <= points[n][0]) & (points[n][1] >= points[m][1]) & (points[m][1] >= points[n][0]):
                    points[m][0] = points[n][0]

                if (points[n][0] >= points[m][0]) & (points[m][1] >= points[n][1]):
                    points[m][0] = points[n][0]
                    points[m][1] = points[n][1]

                    points.pop(n)
                n += 1
                if n == len(points):
                    break
            m += 1
            if m == len(points) - 1:
                break

        print(points[n][0])


class Solution1:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans



