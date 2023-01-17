def check(year):
    if(year%4==0):
        if (year%100==0 and year%400!=0):
            return False
        return True
    else:
        return False

n=int(input())
print(check(n))