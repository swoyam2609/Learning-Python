n=int(input())
max=0
smax=0
str=input()
lst=str.split()
lst=[int(i) for i in lst]
lst.sort(reverse=True)
for i in lst:
    if(i!=lst[0]):
        print(i)
        break