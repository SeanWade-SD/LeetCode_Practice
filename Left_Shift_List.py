# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#
#
# 示例 1：
#
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
# 示例 2：
#
# 输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof

class Solution:
    def reverseLeftWords(self, s="lrloseumgh", n=6):

        s = list(s)
        while n > 0:
            s.append(s[0])
            s.remove(s[0])
            n -= 1

        return "".join(s)


class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)