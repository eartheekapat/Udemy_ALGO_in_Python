class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def insert_head(self, new_data):
        
        self.count = self.count + 1
        new_node = Node(new_data)
        # link is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # in case link not empty
        else:       
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, new_data):
        new_node = Node(new_data)
        self.count = self.count + 1

        # in case list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # in case list is not empty
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def traverse_backward(self):
        temp = self.tail
        while temp is not None:
            print(temp.data)
            temp = temp.prev
            
    def inv_ll(self):
        res = DoublyLinkedList()
        # loop backward
        temp = self.head
        while temp is not None:
            res.insert_head(temp.data)
            temp = temp.next
        return res

if __name__ == '__main__':
    dllist = DoublyLinkedList()
    dllist.insert_head(3)
    dllist.insert_head(2)
    dllist.insert_head(1)
    dllist.insert_tail(4)
    dllist.insert_tail(5)
    dllist.insert_tail(6)

    dllist.traverse_forward()
    print('\n')
    dllist.traverse_backward()

    print("inverse linkedList : ")
    rev_ll = dllist.inv_ll()
    rev_ll.traverse_forward()