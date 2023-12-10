x, y, z = 10, 5, 7
if x > y:
    if y > z:
        result = "A"
    elif x > z:
        result = "B"
    else:
        result = "C"
else:
    if x > z:
        result = "D"
    elif y > z:
        result = "E"
    else:
        result = "F"

if x % 3 == 0:
    result += "1"
elif y % 3 == 0:
    result += "2"
else:
    result += "3"
print(result)