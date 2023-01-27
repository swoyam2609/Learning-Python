def is_armstrong(n):
    num = n
    len_num = len(str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** len_num
        num //= 10
    if n == sum:
        return True
    else:
        return False

a=int(input("Enter number:"))
if(is_armstrong(a)):
    print("Armstrong")
else:
    print("Not Armstrong")