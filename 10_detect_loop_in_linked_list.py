class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dectect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# Build linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#create a loop 5->3
head.next.next.next.next = head.next.next       #Loop from 5 to 3

#dectect loop

if detect_loop(head):
    print("Loop detected in linked list")
else:
    print("No loop in th linked list")


