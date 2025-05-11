class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_recursive(head):
    #Base case: empty list or single node
    if head is None or head.next is None:
        return head

    #Recursive call
    new_head = reverse_recursive(head.next)

    #reverse the current node's pointer
    head.next.next = head
    head.next = None

    return new_head

#Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end = " -> ")
        head = head.next
    print("None")

# Build the linked list: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original List : ")
print_list(head)

# Reverse the list
reversed_head = reverse_recursive(head)
print("Reversed List : ")
print_list(reversed_head)
