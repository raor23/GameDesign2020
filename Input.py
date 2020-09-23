#Rohan Rao
#Having fun with ForLoops
#Learn to resize our program
#Asking the user for values
# is requesting via console for something the default is a string
# type casting
begin =int(input("Number of lines\n"))
lines=begin
for line in range(lines):
    for number in range(begin-line,0,-1):
        print(number, end=' ')
    print()
