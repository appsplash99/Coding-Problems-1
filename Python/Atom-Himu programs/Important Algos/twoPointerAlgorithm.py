# //so the two pointer algo is used where you want to find sum of two number in a sorted array equals to third number
# Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
# Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair
# of elements (A[i], A[j]) such that their sum is equal to X.
# it solves these types of problem o(n)


def  twoPointerSum(arr,x):  # function
    arr.sort()  # firstly the array or list should be sorted
    # so here i and j are working as two pointers so that's  why we call this algo two pointer algo.
    i=0   # initializing i with =0
    j = len(arr)-1 # and j with last index of array

    while i<j:  # now here checking the while will only run if i less than j other wise it will return false
        # so now here we have increase and decrease the value of i and j with help of following conditions
        if arr[i]+arr[j]>x:  # like here if the element at arr[i] and arr[j]  sums up and the sum is greater then the number we entered(like in our example 8)
            j=j-1 # so we have to decrease the value of j by 1 to come close equal to our number
        elif arr[i]+arr[j]<x: # same here if the sum of arr[i] and arr[j] is less than the number we entered
            i=i+1 # so then we have have to increase value of i by 1 to come come close to our number
        else:
            return True  # and whenever we will find the sum of arr[i] and arr[j] then we will return True
    return False  # as i above mentioned if the value of i will greater than the j then it will retuen false


t = list(map(int,input("Enter your Numbers :-").split(" "))) #  here you are taking input from user in a list form
# for example :
#     [1 4 2 6 8 5]
#      number is := 8
# so you can clearly see that in list 6 and 2 are the number which sum is equal to number 8(so the twoSumPointer will return True)
# why we are using this algo ?
# it takes o(n) time other brute force will take o(n)2 to solve same question
k = int(input("Enter the number you want to find equal to  : ")) # this is the number which equal to you want to find pair in the above list exists or not
print(twoPointerSum(t,k)) # calling the twoPointerSum function

