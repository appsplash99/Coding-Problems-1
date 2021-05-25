x = "jack"
print(x)

# We can store only one value in a variable
#If we try to add one more value than last value will be overridden now value will be krish
x = "Krish"
print(x)

#If we want to store multiple values in single variable for that we use List Datatype

db = [1, "Nitesh", "Ok"] #indexing start from zero
print(db)
print(type(db)) #list

#To add item to list we use append()
db.append(1111)
print(db)

#Slicing Operartion -> it is done to manupulate the list
print(db[1:3]) #start from 1 index till second index as last index is excluded 
#output-> ['Nitesh','Ok']

print(db[1:4])
#output->['Nitesh', 'Ok', 1111]

print(db[2:]) #starting from 2 to till last
#output->['Ok', 1111]

print(db[ : 3]) #from 0 to 3
#output->[1, 'Nitesh', 'Ok'] 

print(db[-1]) #last element, in tis case indexing starts from 1
#output-> 1111

print(db[-3:]) #last 3 and indexing starts from 1 as it is indexing from backward
#output->['Nitesh', 'Ok', 1111]

#List with multiple records
db = [ [1, "Nitesh", 1111, "good"], [2, "rahul",2222, "Ok" ], [3,"raj",3333, "Ok"] ]
print(db)
print(type(db))

print(db[1]) #record at 1 index will get printed
#output-> [2, 'rahul', 2222, 'Ok']

print(db[1:3]) #record at 1 index and 2nd index will get printed
#output-> [[2, 'rahul', 2222, 'Ok'], [3, 'raj', 3333, 'Ok']]

print(db[2][2]) #prints 2nd index records 2nd element
#output-> 3333

# Can we retrrive all columns in List?
# -> Not possible, Because list is note meant for columnwise operations

#If we want to work columnwise for that we use numpy array

import numpy
a = numpy.array(db) #converted list into numpy array
print(a)
#output-> [['1' 'Nitesh' '1111' 'good']
#          ['2' 'rahul' '2222' 'Ok']
#          ['3' 'raj' '3333' 'Ok']]
print(type(a)) 
#<class 'numpy.ndarray'>

print(a[0]) #prints first list
#output-> ['1' 'Nitesh' '1111' 'good']

#coloumn wise operation
print(a[ : , 1]) #prints column indexed at postion 1  ( indexing start from 0)
#output-> ['Nitesh' 'rahul' 'raj'] 

print(a[ : , 1:3]) #retreive column 1 and 2 as last number is excluded
#output->[['Nitesh' '1111']
#         ['rahul' '2222']
#         ['raj' '3333']]


#One Dimentional array
a1 = numpy.array( [ 1,2,3,4,5,6,7,8]) #if numpy array has only one row than only one sq bracket comes up
print(a1.shape) # it shows the total element
#output-> (8,) 1d array

print(a1[2:5]) 
#output-> [3 4 5]

print(a1.reshape(2,4)) #convert array into 2 rows and 4 columns 
#output-> [[1 2 3 4]
#         [5 6 7 8]]

print(a1.reshape(4,2).shape) #converts into 4 rows and 2 coloumns ans shows number of rows and col
#output-> (4, 2)

print(a1.reshape(1,8).shape)
#output-> (1, 8)
print(a1.reshape(-1,1).shape)
#output-> (8, 1)


