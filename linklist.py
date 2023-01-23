#Link List
class Node:
    def __init__(self,data):
        self.data = data
        self.address = None


class Linklist:
    def __init__(self):
        self.head = None


    def createNodeatFirstPos(self, data):
        new_node  = Node(data)
        new_node.address = self.head
        self.head = new_node
    
    def insertNodeatLastPos(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            tmp = self.head



    def display(self):
        print("here is our LinkList : ",end= "\n")
        tmp = self.head
        while tmp!= None:
            print(tmp.data, end = "-->")
            tmp = tmp.address

    

if __name__ == "__main__" :
    list = Linklist()
    list.createNodeatFirstPos(2)
    list.createNodeatFirstPos(3)
    list.createNodeatFirstPos(4)
    list.display()

    
