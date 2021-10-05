''' def lw(x):
    y = x *x
    return y
print(lw(4)) ''' #Function calling and here 4 is a parameter that is stored in x

''' import dis  #here dis stands for disassemble it disassembles the funtion and tell us behind the scene how on the top of ram they are working 
dis.dis(lw) '''

''' print(list(range (5))) '''# it will create list till 5 and last number is exclude and it start from 0

# If we dont want to start from 0 we can give entry value
''' print(list(range(4,10))) ''' # list will be crated from 4 till 9


''' w = list(range(2,5)) '''
''' print(w)#it will give output in list form
for i in w:
    print (i) '''#it will pick all the item from the list and print it

''' j=1 #stored j=1 in a memory 
for i in w: #her i is [2,3,4]
    j = j*i # first i that is 2 will multiply with j that is 1  ; 1*2 
print(j) '''#it will give multiplication of all number in list that is 2*3*4 = 24

#Factorial program [ iterative approach]
''' def lwf(n):
    x = list(range(2,n+1))#if we want factorial till 5 than we need we need to do factorial till 6 as last number is excluded therefore we use n+1 
    j=1
    for i in x:
        j=j*i
    return(j)
print(lwf(5)) '''
#The approach of this algo is that we fixed the 1 in j and keep in increasing it this is called Iterative approach

#Example of reacursion
''' def a():
    b()
    print("i am a")
    
def b():
    c()
    print("i am b")
    
def c():
    d()
    print("i am c")
    
def d():
    print("i am d")

a()
print("done") '''
#Here a() will only run when b() will be called and b() will only run when c() is called
# and c() will only run when d() is called therefore first d will run then c then b and then a

# Factorial prgram [ Recursion approach]
def lwrf(n):
    if n == 1:# this is to stop the loop here if n reaches to 1 then it will return the n 
        return n
    else:
        return n*lwrf(n-1) #here funtion is callion it self again and again
print(lwrf(4))

