for i in range(4):
    for star in range(i+1):
        print(star+1, end="")
    for space in range(4-i-1):
        print(" ", end="")
    for space in range(4-i-1):
        print(" ", end="")
    for star in range(i+1):
        print(i-star+1, end="")
    print("")