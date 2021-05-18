##################### Problem Statement ##########################

# todo **Write a program to reverse the string using recursion.**

def reverse(str):
    if len(str)==0:
        return str
    else:
        return reverse(str[1:]) + str[0]
    
name = input("Enter the name that you want to reverse: ")

print("The Given String is:" , name)

print("Reversed string is:", reverse(name)) 

