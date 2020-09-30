#Rohan Rao

strVar= "My name is R"
print(strVar)
#You get the length of your string
print(len(strVar))
print(strVar[len(strVar)-1])#You get the last index of your string
indexNum= strVar.find("name")
print(indexNum)
print(strVar[indexNum: indexNum+4])
print(strVar[indexNum:  ])
print(strVar[ :indexNum+1])
print(strVar.replace('name','initial'))
strVar= strVar.replace('name','initial')
print(strVar)
print(strVar.upper())
print(strVar.lower())
print(strVar)
strVar=strVar.upper()
print(strVar)
back = list(strVar)
#back = back.reverse()
#print(' '.join(back))
