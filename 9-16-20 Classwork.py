


# Python 3 program to
# print above pattern

# Function definition
def pattern(n) :

    # for loop for rows
    for i in range(1,n+1) :

        # conditional operator
        if(i % 2 != 0) :

            k = i + 1
        else :
            k = i

        # for loop for printing spaces
        for g in range(n ,k,-1) :

            print(" ",end="")

        # according to value of k carry
        # out further operation
        for j in range( 0, k):
            print("* ",end="")
        print()


# Driver Code
n = 6
pattern(n) # Python 3 program to
# print above pattern

# Function definition
def pattern(n) :

    # for loop for rows
    for i in range(1,n+1) :

        # conditional operator
        if(i % 2 != 0) :

            k = i + 1
        else :
            k = i

        # for loop for printing spaces
        for g in range(n ,k,-1) :

            print(" ",end="")

        # according to value of k carry
        # out further operation
        for j in range( 0, k):
            print("* ",end="")
        print()


# Driver Code
n = 6
pattern(n) 
