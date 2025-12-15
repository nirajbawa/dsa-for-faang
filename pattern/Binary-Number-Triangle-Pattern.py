for i in range(5):
    flag = i+1
    for j in range(i+1):
        if (i)%2!=0:
            print("1", end="")
        else:
            print("0", end="")
        i+=1
    print("") 
            