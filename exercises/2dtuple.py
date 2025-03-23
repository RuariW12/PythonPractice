
#this is a 2d tuple

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

#declare "row" as the tuples in num pad
#declare "num" as values in each tuple
#print each value, and add a space after
#print() adds a new line and is added in the original loop, as to create a new line after each tuple or row
#   is made
