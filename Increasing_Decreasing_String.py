# Given a string s. You should re-order the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once
# you can choose any occurrence and append it to the result.
#
# Return the result string after sorting s with this algorithm.

# Example 1:
#
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# Example 2:
#
# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
# Example 3:
#
# Input: s = "leetcode"
# Output: "cdelotee"
# Example 4:
#
# Input: s = "ggggggg"
# Output: "ggggggg"
# Example 5:
#
# Input: s = "spo"
# Output: "ops"
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/increasing-decreasing-string


class Solution:
    def sortString(self, s = "leetcode"):
        L = list(s)
        V = []
        N = []
        result = []

        for value in L:
            if value in V:
                continue
            else:
                V.append(value)
        V = sorted(V)

        for i in range(len(V)):
            N.append(L.count(V[i]))

        t = len(L)
        while len(result) < len(L):
            t1 = 0
            t2 = 0
            while t1 < len(V):

                if N[t1] > 0:
                    result.append(V[t1])
                N[t1] -= 1
                t1 += 1
                t -= 1

            while t2 < len(V):

                if N[len(V)-t2-1] > 0:
                    result.append(V[len(V)-t2-1])
                N[(len(V)-t2-1)] -= 1
                t2 += 1
                t -= 1
        return ''.join(result)


class Solution1:
    def sortString(self, s):
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1
        print(num)

        ret = list()
        while len(ret) < len(s):
            for i in range(26):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1

        return "".join(ret)

# 每个字符被选择且仅被选择一次；
# 每一轮会在字符串末尾加入一个先升后降的字符串，且该串的上升部分和下降部分都会尽可能长。
# 于是我们重复若干轮下述操作，直到每一个字符都被选择过，这样就可以构造出这个字符串：
# 先从未被选择的字符中提取出最长的上升字符串，将其加入答案。
# 然后从未被选择的字符中提取出最长的下降字符串，将其加入答案。
# 注意到在构造时我们只关注字符本身，而不关注字符在原字符串中的位置。因此我们可以直接创建一个大小为 2626 的桶，
# 记录每种字符的数量。每次提取最长的上升或下降字符串时，我们直接顺序或逆序遍历这个桶。
# 具体地，在遍历桶的过程中，如果当前桶的计数值不为零，那么将当前桶对应的字符加入到答案中，并将当前桶的计数值减一即可。
# 我们重复这一过程，直到答案字符串的长度与传入的字符串的长度相等。
