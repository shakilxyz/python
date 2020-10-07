# creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linking the nodes serially
class Linked:
    def __init__(self):
        self.head = None

    # insert a node at the tail of linked list
    def insert_last(self, newNode):
        currentNode = self.head
        if self.head is None:
            self.head = newNode
        else:
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    # insert a node at the head of a linked list
    def insert_first(self, newNode):
        newNode.next = self.head
        self.head = newNode

    # delete the last node
    def del_last(self):
        targetNode = self.head
        if targetNode is None:
            print(" Linked list is empty")
            return
        while targetNode.next is not None:
            previousNode = targetNode
            targetNode = targetNode.next
        previousNode.next = None

    # deleting first node
    def del_first(self):
        if self.head is None:
            print(" Linked list is empty")
            return
        self.head = self.head.next

    # insert a node at any desired position in the linked list
    def insert_pos(self, pos, newNode):
        if pos == 0:
            self.insert_first(newNode)
            return
        elif pos > 0 and self.head is None:
            print(" Linked list is empty!")
            return
        currentPos = 1
        currentNode = self.head
        while currentPos < pos:
            currentNode = currentNode.next
            if currentNode is None:
                print(" Insertion position out of range")
                return
            currentPos += 1
        tempNode = currentNode.next
        newNode.next = tempNode
        currentNode.next = newNode

    # delete a node from any desired position
    def del_pos(self, pos):
        if pos == 0:
            self.del_first()
            return
        elif pos > 0 and self.head is None:
            print(" Linked list is empty!")
            return
        currentPos = 1
        currentNode = self.head
        while currentPos <= pos:
            previousNode = currentNode
            currentNode = currentNode.next
            if currentNode is None:
                print(" Position is out of range")
                return
            currentPos += 1
        print(" Node deleted at position {} with data \"{}\"".format(pos, currentNode.data))
        previousNode.next = currentNode.next

    # searching data by value
    def search_data(self, searched_data):
        match = False
        currentNode = self.head
        pos = 0
        while currentNode is not None:
            if currentNode.data == searched_data:
                match = True
                break
            pos += 1
            currentNode = currentNode.next
        if match:
            print(" Found \"{}\" at node {}".format(searched_data, pos))
        else:
            print(" No data found as \"{}\"".format(searched_data))

    # searching data by the position of the node
    def search_by_pos(self, pos):
        currentNode = self.head
        currentPos = 0
        if currentNode is None:
            print(" Linked list is empty !")
            return
        while currentPos < pos:
            currentNode = currentNode.next
            if currentNode is None:
                print(" Out of range")
                return
            currentPos += 1
        print(" Data at node {} is \"{}\"".format(pos, currentNode.data))

    # counting the length of the linked list
    def linked_list_len(self):
        currentNode = self.head
        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        print(" Total nodes in linked list =", count)

    # showing the full linked list
    def show(self):
        currentNode = self.head
        if currentNode is None:
            print(" Linked list is empty")
            return
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


linked = Linked()

while True:
    print("\n 1 -> insert last\n 2 -> insert first\n 3 -> insert any position\n 4 -> delete last\n 5 -> delete first\n"
          " 6 -> delete by position\n 7 -> search by data\n 8 -> search by node position\n 9 -> total nodes\n 10 -> "
          "show\n")
    try:
        s = int(input(" select an option : "))
    except:
        print(" invalid input")
        continue

    if s == 1:
        linked.insert_last(Node(input(" Data : ")))
    elif s == 2:
        linked.insert_first(Node(input(" Data : ")))
    elif s == 3:
        try:
            linked.insert_pos(int(input(" Position : ")), Node(input(" Data : ")))
        except:
            print(" wrong input")
    elif s == 4:
        linked.del_last()
    elif s == 5:
        linked.del_first()
    elif s == 6:
        try:
            linked.del_pos(int(input(" Node Position")))
        except:
            print(" wrong input")
    elif s == 7:
        linked.search_data(input(" Data : "))
    elif s == 8:
        try:
            linked.search_by_pos(int(input(" Position : ")))
        except:
            print(" wrong input")
    elif s == 9:
        linked.linked_list_len()
    elif s == 10:
        linked.show()
