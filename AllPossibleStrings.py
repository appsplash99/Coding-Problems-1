######################## Problem Statement ##############################
# todo Write a program to give all possible of strings when input given as strings.

def string(str, n):
    k = len(str)
    PrintStringLength(str,"",k,n)
    
def PrintStringLength(str,prefix,k,n):
    if (n == 0):
        print(prefix)
        return
    
    for i in range(k):
        newPrefix = prefix + str[i]
        
        PrintStringLength(str,newPrefix,k,n - 1)
        
if __name__=="__main__":
    name = input("Enter the string: ")
    n=3
    print("All Possible Pattern: ")
    string(name,n)     