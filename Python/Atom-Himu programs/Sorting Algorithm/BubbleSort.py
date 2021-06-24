def bubble_sort(data): # this is bubble_sort function
    swap=False # here we have taken a swap variable by which we will decide the array we are passing is already sorted or not.
    for i in range(len(data)-1): # here using the first for loop for the number of rounds like in the given array you can calculate the length which is 6
        # so the array will sort in (total length of array -1) here in this 5 round.(in each round one value will be sort and the last value
        # automatically sort)
        for j in range(len(data)-1-i): # this is the loop in which we are comparing the actual value
            if data[j] > data [j+1]: # here using if statement to compare the value so if the current value will be greater than the next value in the array.
                data[j], data[j+1] = data[j+1], data[j] # then we will swap these two values .
                # for example if we will see in the array you will the first value we are getting which is greater than the next value is
                # 8 because it's next value is 4 so we will swap these two values. and this process will go on.
                # at last you will get your desired output
                # remember the average time complexity of bubble sort is O(n)2
                swap=True # change the value of swap variable  false to true
            if not swap: # here checking if the array is already sorted or not if
                return "Already sorted" # then this will be returned.
    return data

data=[1,5,8,4,7]  # This the data which we want to sort
print(bubble_sort(data)) # Here calling and printing the bubble_sort function which is defined above and remember we are
                    # passing the data inside the function.
                
                    