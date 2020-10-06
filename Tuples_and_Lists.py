#1 Write a Python Program to create a tuple
myList=[1,3,6,8,10]
print(myList)
#2 Write a Python program to create a tuple with different data types
myFruitNumbers=["Banana","Orange",1]
print(myFruitNumbers)
#3 Write a Python program to create a tuple with numbers and print one item.
myNumbers=[1,3,7,9]
print(myNumbers[0])
#4 Write a Python program to unpack a tuple in several variables.
n1, n2, n3, n4, n5 = myList
print(n1 + n2 + n3 + n4 + n5)
#5 Write a Python program to add an item in a tuple.
myFruitNumbers.append("Strawberry")
print(myFruitNumbers)
#6 Write a Python program to convert a tuple to a string.

#7 Write a Python program to get the 4th element and 4th element from the last of a tuple

#8 Write a Python program to create the colon of a tuple

#9 Write a Python program to find the repeated items of a tuple.

#10 Write a Python program to check whether an element exists within a tuple.
if 3 in myList:
    print("The element is there")
#11 Write a Python program to convert a list to a tuple.
def convert(myList):
    return tuple(i for i in myList)
print(convert(myList))
#12 Write a Python program to remove an item from a tuple.
#Not Possible
#13 Write a Python program to slice a tuple.

#14 Write a Python program to find the index of an item of a tuple.

#15 Write a Python program to find the length of a tuple.
print(len(myList))
#16 Write a Python program to convert a tuple to a dictionary.

#17 Write a Python program to unzip a list of tuples into individual lists.

#18 Write a Python program to reverse a tuple.
print(reverse(myList))
#19 Write a Python program to convert a list of tuples into a dictionary.

#20 Write a Python program to print a tuple with string formatting.Sample tuple : (100, 200, 300)Output :This is a tuple (100, 200, 300)
