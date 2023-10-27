

cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    line[0] = int(line[0])
    if line[0] % 2 == 0:
        print("EVEN")

    else:
        print("ODD")




   
   


