class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

   class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def question5(self, m):
        p1 = self.head
        p2 = self.head


        for i in range(m):
            if (p1 == None):
                return None
            p1 = p1.next
        while (p1 != None):
            p1 = p1.next
            p2 = p2.next

        return p2.data



ll = LinkedList()
ll.push("A")
ll.push("B")
ll.push("C")
ll.push("D")
ll.push("E")
ll.push("F")

def main():

    print (LinkedList.question5(ll, 3))

if __name__ == "__main__":
    main()
