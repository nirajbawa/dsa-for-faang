for i in range(4):
    for space in range(4-i):
        print(" ", end="")
    for star in range(i+1):
        print(chr(ord('A')+star), end="")
    for star in range(i):
        print(chr(ord(chr(65+i-1))-star), end="")
    print("")