# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(l1, l2):
    curr1 = l1
    curr2 = l2
    more = 0 
    l = []
    while curr1 or curr2:
        if curr1 and curr2:
            val = curr1.val + curr2.val + more
            if val >= 10:
                more = val // 10
                val = val - more * 10
            else:
                more = 0
            l.append(val)
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1 == None:
            val = curr2.val + more 
            if val >= 10:
                more = val // 10
                val = val - more * 10
            else:
                more = 0
            l.append(val)
            curr2 = curr2.next
        else:
            val = curr1.val + more 
            if val >= 10:
                more = val // 10
                val = val - more * 10
            else:
                more = 0
            l.append(val)
            curr1 = curr1.next
    
    if more:
        l.append(more)
    head = curr = ListNode(l[0])
    for i in range(1, len(l)):
        curr.next = ListNode(l[i])
        curr = curr.next
    return head
        
