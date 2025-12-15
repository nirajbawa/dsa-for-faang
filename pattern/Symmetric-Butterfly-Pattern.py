for i in range(5):
    for star in range(i+1):
        print("*", end="")
        
    for space in range(4-i):
        print(" ", end="")
        
    for space in range(4-i):
        print(" ", end="")
        
    for star in range(i+1):
        print("*", end="")
    
    print()
    
for i in range(4):
    for star in range(4-i):
        print("*", end="")
        
    for space in range(i+1):
        print(" ", end="")
        
    for space in range(i+1):
        print(" ", end="")
        
    for star in range(4-i):
        print("*", end="")
    
    print()