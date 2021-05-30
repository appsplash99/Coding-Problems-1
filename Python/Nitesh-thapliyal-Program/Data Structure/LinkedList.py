""" a=[1,2,3,5,6]
print(type(a))
print (a[0])
print(id(a[0]))#id will tell info about memory id of a[0]
print(hex(id(a[0]))) #as memery address are represented in hexadecimal code so we can convert id into hex code using hex function
 print(hex(id(a[1])))
print(hex(id(a[2])))
print(hex(id(a[3]))) """
#here we can see data is stored in continous form

#traversal and time complexity of traversal is O(n)
#access time is O(1)
""" for i in a:
    print(i)
    print (hex (id(i))) """
#Singly Linked List    
class SLNODE:
    def __init__(self,v): #constructor
        self.value= v
        self.nextnode =None
            
# x1, x2 and x3 are nodes            
x1 = SLNODE("nitesh@gmail.com")
x2 = SLNODE("mini@gmail.com")
x3 = SLNODE("mom@gmail.com")
x1.nextnode = x2 #now x1 contains the address of x2
x2.nextnode = x3# now x2 contaions the eddreass of x3 
""" print(x1.value)
#print(x1.__dict__)#__dict__ will show every value in x1
#print(x2.__dict__)
print(x1.__dict__)#now we can see the address of next node store earlier it was none
print(x2.__dict__)#now we can see the address of next node store earlier it was none
print(x3.__dict__) """#last node does not contain the address of anynode there we can say it is singliLinkedList
# x1(node)->x2(node)->x3(node) everynode is linked with each other therefore it is called linkedlist 

""" print(x1.nextnode.value)#shows the value of next node
print(x1.nextnode.nextnode)#shows the address of next to next  node
print(x1.nextnode.nextnode.nextnode.value) """#it will give errot last node does not contain address as it is last
#so here if we know the address of first node then we can know the address of other nodes as well as all are linked with each other

#Traverse in Linked list, Time complexity is O(n)
while x1 is not None:  #here x1 is head of linked list
    print(x1.value)
    x1 = x1.nextnode
#this will retriece all the value of nodes    

# if we want to create circular linked list for that give te last node the address of the first nocde