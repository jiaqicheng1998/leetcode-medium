# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

def removeNthFromEnd(head, n):
    # count the length of the list
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
    
    # if the first the element will be removed
    if length - n == 0:
        return head.next
    
    # remove the nth element from the beginning
    curr = head
    prev = None
    for i in range(length - n):
        prev = curr
        curr = curr.next
    prev.next = curr.next
    return head
