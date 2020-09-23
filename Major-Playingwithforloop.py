#Rohan Rao
#This program contains ForLoops Program, Prime Numbers, and the Fibonacci sequence



#Forloops
for line in range(5):
    print()
    for number in range(5-line,0,-1):
        print(number, end =' ')

#Prime Numbers Program
start = 25  #First Value of finding prime number
end = 50    #Last Value of finding prime number

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#Fibonacci Sequence Program
def fib(number_of_terms):
    a=0

    x= 0
    y= 1
    z= 0

    while a <= number_of_terms:
        print(x)
        z= x + y
        x = y
        y = z
        a= a + 1
fib(10)
