#Take input from the user
num = int(input("How many number you want in fibonacci series: "))

#Initialize first and second values of the series
a = 0
b = 1

#print the fibonacci series
print("\n fibonacci series: ")
for i in range(num):
    print(a,end='')
    c = a + b
    a = b
    b = c