# logical operators = evaluate multiple conditions (or, and, not)

# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

#temp = 25
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is cancelled")
#else:
#    print("The outdoor event is still scheduled")

temp = 26
is_sunny = False

if temp > 25 and is_sunny:
    print("It is a hot, sunny day out")
elif temp < 25 and is_sunny:
    print("It is cold outside and it is sunny")
elif temp < 25 and not is_sunny:
    print("It is cold and not sunny out")
elif temp > 25 and not is_sunny:
    print("It is a hot day, but it is not sunny")
else:
    print("It is not a hot or sunny day out")

