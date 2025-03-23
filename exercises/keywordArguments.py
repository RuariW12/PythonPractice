# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments dont matter
#1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr.", first="Spongebob", last="Squarepants") #can rearrange and it doens't matter if identified

for x in range(1, 11):
    print(x, end=" ") #end is a keyword argument

print()
print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=123,first=456,last=7890)
print(phone_num)


