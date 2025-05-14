# Merge Two Sorted Linked Lists	

# Merge Two Sorted Linked Lists

class Node:
    def __init__(self, val):
        self.val = val
        self.next =  None

def merge_sorted_lists(l1,l2):
        # create a dummy node to simplify code
        dummy = Node(0)
        current = dummy

        # merge the list until one of them is empty
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        #If any element left in either lists, append them
        if l1:
            current.next = l1
        if l2:
            current.next  = l2

        return dummy.next

    #helper function to build a linked list
def build_linked_list(values):
        if not values:
            return None
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        return head

    # helper function to print linked list
def print_linked_list(head):
        current = head
        while current:
            print(current.val, end = " -> ")
            current = current.next
        print("None")

#Test cases
l1 = build_linked_list([1 ,3, 5, 7])
l2 = build_linked_list([2, 4, 6, 8])
merged = merge_sorted_lists(l1, l2)
print("Merged List : ")
print_linked_list(merged)

