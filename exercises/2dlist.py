#2d list - list made up of lists

fruits =     ["apple", "orange", "banana", "coconut"] #row 1
vegetables = ["celery", "carrots", "potatoes"] #row 2
meats =      ["chicken", "fish", "turkey"] #row 3

groceries = [fruits, vegetables, meats]

print(groceries[0][0]) #first [] is row, second [] is column

for collection in groceries:
    for food in collection:
        print(food)

#above code prints everything in groceries, can format any way you want as well as getting rid of commas and brackets

