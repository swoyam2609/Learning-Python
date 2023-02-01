def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial of negative numbers doesn't exist.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of", num, "is", factorial(num))
