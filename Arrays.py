#array printing
myList=[2,4,5,7,8,9]
myFruit=["apple","banana","orange"]
yourList=[98,87,65]
newFruit=[]
#myFruit.remove("apple")
myFruit.pop(0)
del myFruit[0]
myFruit.append("mango")
myFruit.insert(1,"kiwi")
#del myFruit will delete the list from the program
print(myFruit)
newFruit.clear()
newFruit.append("strawberries")
print(newFruit)
# print(myList[-2])
print(myList[1:4])
if 4 in myList:
    print("yes")
if "berries" in myFruit:
    print("I love bananas!")
else:
    print("buy some berries")
#for x in myList:
#    print(x)
#ourList= myList + myFruit #creates a new list
#for i in myFruit:
#    myList.append(i)      #changes the original list
myList.extend(myFruit)
#myList.sort() typecast before you sort
print(myList)
myFruit.sort()
print(myFruit)
