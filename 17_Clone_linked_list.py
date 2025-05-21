from stringprep import map_table_b2

from Palindrom_linked_list import head1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def clone_linked_list_with_random(head):
    if not head:
        return None

    #Step 1: Insert clones nodes in between original nodes
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    #Stop 2: assign random pointers to the cloned nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    #step 3: separate original and cloned list
    original = head
    clone = head.next
    cloned_head =  head.next

    while original:
        original.next = original.next.next
        if clone.next:
            clone.next = clone.next.next
        original = original.next
        clone = clone.next
    return cloned_head


# helper function to print list with random pointers
def print_linked_list_with_random(head):
    current = head
    while current:
        rand = current.random.val if current.random else None
        print(f"Value : {current.val}, Random: {rand}")
        current = current.next

#Test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

n1.random = n3
n2.random = n1
n3.random = n2

print("Original List : ")
print_linked_list_with_random(n1)

clone_head = clone_linked_list_with_random(n1)

print("\nCloned List : ")
print_linked_list_with_random(clone_head)

'''
Original List : 
Value : 1, Random: 3
Value : 2, Random: 1
Value : 3, Random: 2

Cloned List : 
Value : 1, Random: 3
Value : 2, Random: 1
Value : 3, Random: 2


'''
