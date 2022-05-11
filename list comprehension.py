x = int(input())
y = int(input())
z = int(input())
n = int(input())
print('[', end="")
for i in range (x+1):
    for j in range (y+1):
        for k in range (z+1):
            if(i+j+k!=n):
                if(i==x and j==y and k==z):
                    print("["+str(i)+", "+str(j)+", "+str(k)+"]", end="")
                    break
                print("["+str(i)+", "+str(j)+", "+str(k)+"], ", end="")
print(']')