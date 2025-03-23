# Python Temperature Conversion

unit = input("What unit? (F or C): ")
temp = float(input("What temperature?: "))

if unit == "F":
    temp = (temp - 32)*(5/9)
    print(f"The temperature is: {round(temp, 2)} Celsius")
elif unit == "C":
    temp = (temp*(9/5)) + 32
    print(f"The temperature is: {round(temp, 2)} Fahrenheit")
else:
    print("Your unit is not valid")