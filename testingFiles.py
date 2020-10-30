# Rohan Rao
# 10-28-20
# Learning about files:
# open/create
# close
# write       "w"
# append      "a"
# read        "r"
# create a fileVariablename= open("fileName.txt", function)
# To be able to remove a file we need to use the os module
import os
import time
myFile = open("newFile.txt", "w" ) # open file if exists, if not it will create it
myFile.write("I am adding some new stuff")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
# When you use "w" it will overwrite
myFile = open("newFile.txt", "w" ) # open file if exists, if not it will create it
myFile.write("Oops, I deleted my stuff\n")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
# I am going to add more info to myFile
myFile = open("newFile.txt", "a" ) # open file if exists, if not it will create it
myFile.write("I add more stuff\n")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
time.sleep(2)
if os.path.exists("Mygame.py"):
    print("yes")
else:
    print("no")
myFile=open("lineFile.txt", "w")
for i in range(10):
    word = "this is line number  " + str(i+1) + "\r"
    myFile.write(word)
myFile.close()
myFile=open("lineFile.txt", "r")
print(myFile.read())
myFile.close()
# to remove the file: os.remove("newFile.txt")
