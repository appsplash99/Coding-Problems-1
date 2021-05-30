import array as arr
import sys 
a = arr.array('i', [5,10])#Here "i"stands for integer and it denotes data type and 5 and 10 are data also called elements
print (a[0]) #here 0 is index and we are checking what item is present in index 0
print (a.buffer_info()) #buffer_info() tells physical memory address and number of element in array
a[1] = 15 #Will update the value at 1 position ealier it was 10 now it will be 15
print( a[1])
a.append(20)#append will add item but using append is worst idea as it increases time complexity
print(a)
b=sys.getsizeof(a)#getsizeof will tell how much byte does array use form ram
print(b) 
a.remove(15)#remove() removes element from array
print(a)

 