#Program to find middle node in linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #insert new node at the end 
        new_node = Node(data)
        if  not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def find_middle(self):             # Find middel node 
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return  slow.data if slow else None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' -> ')
            curr = curr.next
        print("None")

# Example usage
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.append(val)

ll.display()
print("Middle Node : ", ll.find_middle())



'''
Output:

10 -> 20 -> 30 -> 40 -> 50 -> None
Middle Node :  30
'''
