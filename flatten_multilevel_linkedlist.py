# python code to flatten multilevel linked list
'''
input: 1->2->3
             |
             4->5
                |
                6->7

Output: 1->2->3->4->5->6->7

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None

def flatten_list(head):
    if not head:
        return None

    # Use a stack to simulate the recursion(DFS)
    stack = []
    current = head

    while current:
        if current.child:
            if current.next:
                stack.append(current.next)
            current.next = current.child
            current.child = None
        if not current.next and stack:
            current.next = stack.pop()
        current = current.next
    return head

def print_flattened_list(head):
    while head:
        print(head.val, end = " -> ")
        head = head.next
    print(None)

# Example Usage
#Creating nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.next.next.child = Node(7)
head.next.next.child.next = Node(8)
head.next.next.child.next.child = Node(11)
head.next.next.child.next.child.next = Node(12)

# Flatten and print
flat = flatten_list(head)
print_flattened_list(flat)

























