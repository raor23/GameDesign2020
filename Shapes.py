#Rohan Rao
#Shapes

#In-Class Attempt:

size= 8
for line in range(size):
    print()
    for number in range(line+1):
        print("*", end = '')
    for space in range(size-line-1):
        print(' ', end = '')
    for number in range(size-line):
        print("*", end = '')
    for space in range(size-line-1):
        print(' ', end = '')


#1st Attempt:
rows = 14
rows2= 7

for j in range(1, rows2+1):
    print("*" * j)
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print(" " * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2

rows = 7
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print(" *", end="")
    print("")
