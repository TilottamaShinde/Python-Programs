# Node class for Linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#Function to remove duplicates from sorted linked list
def remove_duplicate(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next            #skip duplicates
        else:
            current = current.next
    return head

# Helper function to build a linked list
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

#Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("None")

#Test Case
head = build_linked_list([1,1,2,3,4,5,5])
print("Original List : ")
print_linked_list(head)

head = remove_duplicate(head)
print("Ater Removing Duplicates : ")
print_linked_list(head)
