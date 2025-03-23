# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive values
# := = place sign to the leftmost position
# : = insert a space before positive numbers
# :, = comma seperator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price1 is ${price1:+.3f}")
print(f"Price2 is ${price2:010}")
print(f"Price3 is ${price3:.1f}")

#if you want to add multiple you dont have to separate it with anything just continuously add
# for example: {price:,+.3f}
