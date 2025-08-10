# For example, take 153 (3 digits), which is narcissistic(armstrong):
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic(value):
    if value <= 0:
        print("Invalid value")
    
    digits = str(value)
    print("Digits value: ",digits)
    print("Digits type: ",type(digits))
    print("Digits lenght: ",len(digits))
    
    total = 0
    

    for i in range(len(digits)):
        #print(digits[i], end="")
        total += int(digits[i]) ** len(digits)
    
    print(total)

    if total == int(value):
        return True
    else:
        return False

number = 153
result = narcissistic(number)
print(result)

# Another solutions:

"""def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)"""

"""def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))"""

