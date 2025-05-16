class Node:
    def __init__(self, val):
        self.val = val
        self.next =  None

def remove_duplicates_unsorted(head):
    if not head:
        return None

    seen = set()
    current = head
    seen.add(current.val)

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next        #skip duplicates
        else:
            seen.add(current.next.val)
            current =current.next

    return head

# helper function
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val , end = " -> ")
        current = current.next
    print("None")

#Test Case
head = build_linked_list([4,2,3,2,4,1,5,1,3])
print("Original List: ")
print_linked_list(head)
head = remove_duplicates_unsorted(head)
print("After Removing Duplicates : ")
print_linked_list(head)