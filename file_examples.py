filename = "numbers.txt"

f = open(filename, "w")

myList = [1,2,3,4,5]

for i in range(0,len(myList)):
    f.write(str(myList[i]) + "\n")
    
f.close()

f = open(filename, "r+")

for line in f:
    print(line)
    
f.close()
    