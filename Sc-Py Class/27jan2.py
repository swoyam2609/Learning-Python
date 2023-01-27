list=[]
while(True):
    print("Enter Options:\n1. Append\n2. Delete")
    choice = int(input())
    if(choice==1):
        a=int(input())
        list.append(a)
        print(list)
    elif(choice==2):
        a=int(input())
        list.remove(a)
        print(list)