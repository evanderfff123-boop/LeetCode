# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head

        # 1.遍历链表，将值复制到数组中
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # 2.利用切片[::-1]快速判断数组是否与其反转后相同
        return vals == vals[::-1]