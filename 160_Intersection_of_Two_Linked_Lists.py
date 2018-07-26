# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lena, lenb = self.get_length(headA), self.get_length(headB)
        a_p, b_p = headA, headB
        
        if(lena > lenb):
            for i in range(lena - lenb):
                a_p = a_p.next
        else:
            for i in range(lenb - lena):
                b_p = b_p.next
        
        while(a_p is not None or b_p is not None):
            if(a_p == b_p): 
                return a_p
            a_p, b_p = a_p.next, b_p.next
        return None
    
    def get_length(self, head):
        l = 0
        while head:
            l+=1
            head=head.next
        return l

