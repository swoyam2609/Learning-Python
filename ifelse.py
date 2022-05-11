n = int(input())
if(n%2==1 or (n%2==0 and n>=6 and n<=20)):
    print("Wierd")
elif((n%2==0 and n>=2 and n<=5) or n>20):
    print("Not Wierd")