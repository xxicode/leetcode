def removeNthFromEnd(self, head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast: return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head