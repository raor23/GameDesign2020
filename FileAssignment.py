# Rohan Rao
# This is the assignment over files
import os
import time

def program():
    menu = input("""*****************************************
*                Hello!                 *
*        Please enter the file name     *
*               you want                *
*****************************************\n""")
    file2 = open(menu, 'w')
    fileInfo = input("Ok, what information would you like to be saved in there?\n ")
    file2.write(fileInfo)
    file2.close()
    file2 = open(menu, "a")
    file2.write("\n I am just adding information to this file :)")
    file2.close()
    file2 =  open(menu, "w")
    fileInfo2 = input("Ok, what other information would you like to write?\n ")
    fileVerify = input("This is a warning that all previous data will be deleted, are you ok with this?\n ")
    if fileVerify == "yes":
        file2.write(fileInfo2)
    file2.close()
    file2 = open(menu, "r")
    fileask = input("Would you like to see what is written in the file?\n ")
    if fileask == "yes":
        print(file2.read())
    fileDelete = input("Would you like to delete the file?\n")
    if fileDelete == "yes":
        os.remove(menu)
    fileMenu = input("Would you like to return to the menu?\n")
    if fileMenu == 'yes':
        while True:
            program()
    elif fileMenu == 'no':
        quit()

program()
