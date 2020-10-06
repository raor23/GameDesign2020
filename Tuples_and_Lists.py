#Rohan Rao
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
def convertTuple(tup):
    str =  ''.join(tup)
    return str

tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)
#7 Write a Python program to get the 4th element and 4th element from the last of a tuple

#8 Write a Python program to create the colon of a tuple
from copy import deepcopy

tuplex = ("HELLO", 5, [], True)
print(tuplex)

tuplex_clone = deepcopy(tuplex)
tuplex_clone[2].append(50)
print(tuplex_clone)
print(tuplex)
#9 Write a Python program to find the repeated items of a tuple.

#10 Write a Python program to check whether an element exists within a tuple.
if 3 in myList:
    print("The element is there")
#11 Write a Python program to convert a list to a tuple.
def convert(list):
    return (*list, )

list = [1, 2, 3, 4]
print(convert(list)
#12 Write a Python program to remove an item from a .
#Not Possible
#13 Write a Python program to slice a tuple.
print(myList(2:5))
#14 Write a Python program to find the index of an item of a tuple.
print(myList.index(10))
print()
#15 Write a Python program to find the length of a tuple.
print(len(myList))
#16 Write a Python program to convert a tuple to a dictionary.
#Skip
#17 Write a Python program to unzip a list of tuples into individual lists.

#18 Write a Python program to reverse a tuple.
ReversedTuple= Reversed(myList)
print(ReversedTuple)
#19 Write a Python program to convert a list of tuples into a dictionary.
#Skip
#20 Write a Python program to print a tuple with string formatting.Sample tuple : (100, 200, 300)Output :This is a tuple (100, 200, 300)
#Skip
