# collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#LISTS

fruits = ["apple", "orange", "banana", "coconut"]
print(len(fruits))

print("apple" in fruits)

fruits[1] = "pineapple"
for fruit in fruits:
   print(fruit)

fruits.append("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.insert(0, "pineapple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse() # reversed in order which placed not alphabetical
print(fruits)

fruits.sort() # doing both of these at the same time reverses them in alphabetical order
fruits.reverse()
print(fruits)

print(fruits.index("coconut"))

print(fruits.count("banana"))

fruits.clear()
print(fruits)

#print(fruits[0])

#for fruit in fruits:
#   print(fruit)





