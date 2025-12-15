for i in range(5):
    for space in range(5-i):
        print(" ", end="")
    for star in range(i+1):
        print("*" , end="")
    for star in range(i):
        print("*" , end="")
    print("")

for i in range(5):
    for space in range(i+1):
        print(" ", end="")
    for star in range(5-i):
        print("*" , end="")
    for star in range(5-i-1):
        print("*" , end="")
    print("")