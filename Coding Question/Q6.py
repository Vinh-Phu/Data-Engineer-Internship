class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    def deleteN(self, value):
        #run from head
        currN = self.head
        #if value to be delete at the first element of linked list
        if (currN is not None):
            if(currN.data == value):
                self.head = currN.next
                currN = None
                return
        #search the value to be delete in linked list
        while(currN is not None):
            if currN.data == value:
                break
            previous = currN
            currN = currN.next
        #value not in link list
        if(currN == None):
            return
        #delete node of the value
        previous.next = currN.next
        currN = None
    def sortList(self):
        #Run from head
        currN=self.head
        if(currN is None):
            return
        while(currN is not None): #bubble sort Algorithm
            nextN=currN.next
            while(nextN is not None):
                if(currN.data>nextN.data):
                    currNN=nextN.data
                    nextN.data=currN.data
                    currN.data=currNN
                nextN=nextN.next
            currN=currN.next

    def removeDuplicates(self):
        #run from head
        currN = self.head
        if currN is None:
            return
        while currN.next is not None:
            if currN.data == currN.next.data:
                new = currN.next.next
                currN.next = None
                currN.next = new
            else:
                currN = currN.next
        return self.head   

    def printList(self):
        currN = self.head
        while(currN):
            print(currN.data , end = ' ')
            currN = currN.next
llist = linkList()
 
llist.push(1)
llist.push(1)
llist.push(3)
llist.push(4)
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(6)
llist.sortList()
llist.removeDuplicates()
llist.printList()