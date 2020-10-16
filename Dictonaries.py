#Rohan Rao
#1 Write a Python script to sort (ascending and descending) a dictionary by value.
dic1 = {0:10,2:30,1:20,3:40}
sorted_dic1= sorted(dic1.items())
print(sorted_dic1)
reversesorted_dic1= sorted(dic1.items(), reverse=True)
print(reversesorted_dic1)
#2 Write a Python script to add a key to a dictionary.
key = {3:4}
dic1.update(key)
print(dic1)
#3 Write a Python script to concatenate the following dictionaries to create a new one.
dic2={1:10, 2:20}
dic3={3:30, 4:40}
dic4={5:50,6:60}
dic2.update(dic3)
dic2.update(dic4)
print(dic2)
#4 Write a Python script to check whether a given key already exists in a dictionary.
dic5 = {"1: 10", "2: 20", "3: 30"}
y = "1: 10"
if y in dic5:
    print("It is present")
else:
    print("It is not present")
#5 Write a Python program to iterate over dictionaries using for loops.
dic6 = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in dic6.items():
     print(color_key, 'corresponds to ', dic6[color_key])
#6 Write a Python script to generate and print a dictionary that contains a number n=int(input("Input a number "))
dic7 = {1:10, 2:20, 3:30, 4:40}
n= 5
for x in range(1,n):
    dic7[x]=x*x
print(dic7)
#7 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
dic8= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
for x in range(1,16):
    dic8[x]=x**2
print(dic8)
#8 Write a Python script to merge two Python dictionaries.
dic9 = {1:10, 2:20}
dic10 = {3:30, 4:40}
dic9.update(dic10)
print(dic9)
#9 Write a Python program to iterate over dictionaries using for loops.
#Already did on number 5
#10 Write a Python program to sum all the items in a dictionary.
dict = {'a': 100, 'b':200, 'c':300}
def returnSum(myDict):

    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum

print("The sum is", returnSum(dict))
