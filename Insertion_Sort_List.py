
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
# Source：力扣（LeetCode）
# Link：https://leetcode-cn.com/problems/insertion-sort-list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def insertionSortList(self, head):
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next


head = Solution()
m = ListNode('4')
m2 = ListNode('3')
m3 = ListNode('2')
m4 = ListNode('5')
m.next = m2
m2.next = m3
m3.next = m4


head.insertionSortList(m)
print(m)


