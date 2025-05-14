# Check if Linked List is Palindrome
# Check if Linked List is Palindrome

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow  = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    temp = slow.next
    prev = None
    slow.next = prev
    prev = slow
    slow = temp

    # Step 3: Compare bot halves
    left =  head
    right = prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

# Helper function to build linked list
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test Cases
head1 = build_linked_list([1, 2, 3, 4])
head2 = build_linked_list([1, 2, 3, 2, 1])

print(is_palindrome(head1))
print(is_palindrome(head2))

