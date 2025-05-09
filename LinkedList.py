class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_recursive(head):
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head

    #Recursive call
    new_head = reverse_recursive(head.next)

    # reverse the current node pointer
    
