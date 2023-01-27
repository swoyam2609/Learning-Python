a=int(input("Enter Number: "))
b=0
while(a>0):
    b=b*10+a%10
    a=int(a/10)
print(b)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(7)