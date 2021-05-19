def Linear_Search(data,n, x): #here data is a list that contains all items
     
    for i in range(0, n): #Traversing item in list and here i is index
        if (data[i] == x):#here X is an item that we want to find
            return i #Here if data that we want to find is present in that list then return that items index
    return -1 #Here if item is not present then dont return anything
 
 
#Item in list 
data = [1, 9, 6, 5, 6]
x = 6
n = len(data) 
 
# Function call
result = Linear_Search(data, n, x)
if(result == -1): #if item is not present than print line mentioned below
    print("Element is not present in array")
else:
    print("Element found at index", result)#If item is present then return its index
    
### Time Complexity of Linear Searching algo #####
# Best case: O(1)
# Average Case: O(n) 
# Worst Case: O(n)   