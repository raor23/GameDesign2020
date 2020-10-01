strDriver= """Here are the instructions to install Drivers
1. After the download is completed go to where you saved the folder.
(By default everything you download from the Internet is saved to the Downloads folder)
2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.
3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.
4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:
*setup application
*Asussetup
*pnpinstal64
*pnputil
*Igxpin
5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."""

#Find how many times the word Drivers is used

subStr="Drivers"
print("The number of the word 'Drivers' is", strDriver.count(subStr))
#Length of string
print("The length of the string is",len(strDriver))
#Replace extract with EXTRACT
print(strDriver.replace('Extract','EXTRACT'))
#Replace setup with SETUP
print(strDriver.replace('Setup','SETUP'))
#Find  ‘4’
print("The number '4' is character", strDriver.find('4'))
#The first \n
#?
#Find the 1 and print until you find the end of the statement
strDriver.find('1')
print("""After the download is completed go to where you saved the folder.
By default everything you download from the Internet is saved to the Downloads folder""")
#Find the 2 and print until you find the end of the statement
strDriver.find('2')
print("Right click on the folder and choose Extract All and then choose Extract again.")
#Find the 3 and print until you find the end of the statement
strDriver.find('3')
print("Once all the contents have been extracted you may delete/disregard the folder with the zip icon.")
#Find the 4 and print until you find the end of the statement
strDriver.find('4')
print("""Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:
*setup application
*Asussetup
*pnpinstal64
*pnputil
*Igxpin""")
#Find the 5 and print until you find the end of the statement
print("Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.")
