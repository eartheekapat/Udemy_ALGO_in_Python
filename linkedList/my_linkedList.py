import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, new_data):
        self.count = self.count + 1
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, new_data):
        self.count = self.count + 1
        new_node = Node(new_data)

        temp = self.head
        # loop to the last node of the list
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # remove node which contains data
    def remove(self, key):
        # in case 0 node in the list
        if self.head is None:
            return

        # store head node
        temp = self.head

        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                self.count = self.count - 1
                return
        
        #serach for the key to be deleted, keep track of the 
        #previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # search fail
        if temp == None: 
            return

        # unlink the node from linked list
        self.count = self.count - 1
        prev.next = temp.next
        temp = None

    def list_size(self):
        return self.count

    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next

    def find_mid(self):
        # checd # node
        if self.count % 2 == 0:
            temp_count = int(self.count / 2)
        else:
            temp_count = int(math.floor(self.count/2) + 1)

        temp_node = self.head
        for i in range(1, temp_count):
            temp_node = temp_node.next

        print(temp_node.data)

    def reverse(self):
        prev = None
        curr = self.head
        next = self.head.next
        # temp = self.head
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = next
            if next is None:
                break 
            next = next.next

        self.head = prev
        


llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(2)
llist.push(3)

print("Created Linked List: ")
llist.printList()

print("reverse list is:")
llist.reverse()
llist.printList()