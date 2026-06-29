# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针法：
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB

        # 只要pA和pB不相等，就继续移动
        while pA != pB:
            # 如果pA走到了末尾，就转到链表B的头部；否则继续走下一步
            pA = pA.next if pA else headB
            # 如果pB走到了末尾，就转到链表A的头部，否则继续走下一步
            pB = pB.next if pB else headA

        # 循环结束时，如果相交，返回相遇节点；如果不相交，此时 pA 和 pB 均为 None，返回 None
        return pA