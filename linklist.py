#Link List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head=None


    def SearchinLinkedList(self,data):
        current = self.head

        if current == None:
            print("NO element in List.")
        else:
            while current != None:
                if current.data == data:
                    return True
                current = current.next
            return False



    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data,end=" ")
            tmp = tmp.next
        print("\n")

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.printlist()
    ele = int(input("Enter element needs to be search : "))
    if ll.SearchinLinkedList(ele):
        print("Found")
    else:
        print("Not found")

    
