# module = a file containing code you want to include in your program
#       use 'import' to include a module (built in or your own)
#       useful to break up a large program reusable separate files

#import math
#import math as m #can create an alias for module

#print(math.pi)
#print(m.pi)

import exampleModule #can import custom modules

result = exampleModule.pi
result1 = exampleModule.square(3)
result2 = exampleModule.cube(4)

print(result)
print(result1)
print(result2)

