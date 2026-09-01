

#Square Pattern
'''numi = int(input("enter the numi"))
mumj = int(input("enter the mumj"))
for i in range(1,numi+1):
    for j in range(1,mumj+1):
        print("*", end=" ")
    print()

#numi = int(input("enter the numi"))
#numj = int(input("enter the numj"))
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()'''


#print piramid pattern
numi = int(input("enter the numi")) 
for i in range(1, numi + 1):
    for j in range(numi - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
        