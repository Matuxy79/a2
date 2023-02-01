#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#function to read the text file and count the number of lefts and rights in each line and substract them to find the distance
def readcount(text):
    k = 0
    with open(text,'r') as file:
        lines = file.readlines()
        for line in lines:
            line = lines[k]
            Left = lines[k].count('L')
            Right = lines[k].count('R')
            if Left > Right:
                dist = Left - Right
            else:
                dist = Right - Left
            print(dist)
            k += 1

#Testing with the examples and printing the output
print("Example 1 :  ")
readcount('example1.txt')
print("Example 2 :  ")
readcount('example2.txt')
print("Example 3 :  ")
readcount('example3.txt')