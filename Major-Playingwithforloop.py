for line in range(5):
    print()
    for number in range(5-line,0,-1):
        print(number, end =' ')


start = 25
end = 50

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


def fib_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0',a,b,end=' ')
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total,end=' ')
        print()
        return b

fib_iter(10)
