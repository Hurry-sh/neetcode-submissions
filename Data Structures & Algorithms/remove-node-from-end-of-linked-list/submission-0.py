class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, size = head, 0

        # Step 1: find length of linked list
        while curr:
            size += 1
            curr = curr.next

        # Step 2: if head needs to be removed
        if n == size:
            return head.next

        # Step 3: find the node before the one to delete
        tmp = head
        for i in range(size - n - 1):
            tmp = tmp.next

        # Step 4: remove the nth node from end
        tmp.next = tmp.next.next

        return head
