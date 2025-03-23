# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

#fruits = {"apple", "orange", "banana", "coconut"}

#fruits.add("pineapple")
#print(fruits)

#fruits.remove("apple")
#print(fruits)

#fruits.pop() #removes first element but its random
#print(fruits)

#fruits.clear()
#print(fruits)

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index("orange"))
print(fruits.count("coconut"))
