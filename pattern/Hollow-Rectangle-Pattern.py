for i in range(4):
    if i==0 or i==3:
        for star in range(4):
            print("*", end=" ")
    else:
        for star in range(4):
            if star == 0 or star == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()