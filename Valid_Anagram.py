# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/valid-anagram



class Solution:
    def isAnagram(self, s, t):

        hashtable1 = {}
        hashtable2 = {}
        for i, m in enumerate(s):
            if m in hashtable1:
                hashtable1[m] += 1
            else:
                hashtable1[m] = 1

        for i, m in enumerate(t):
            if m in hashtable2:
                hashtable2[m] += 1
            else:
                hashtable2[m] = 1

        return hashtable1 == hashtable2


class Solution1:
    def isAnagram(self, s, t):
        m = sorted(s)
        n = sorted(t)
        return m == n






