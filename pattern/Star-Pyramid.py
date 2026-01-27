for i in range(5):
    for space in range(4-i):
        print(" ", end="")
    for star in range(i+1):
        print("*", end="")
    for star in range(i):
        print("*", end="")
    print("")