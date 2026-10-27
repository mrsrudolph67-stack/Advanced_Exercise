import math

# Question 1
print ("Question 1")

a = 5.00
b = 10.00
c = 7.00

a += 3
b *= 2
c %= 4

final_result = math.sqrt (a**2 + b**2 + c**2)

print (round(final_result, 2))

# Question 2
print ("Question 2")

x = int(input("Enter your number: "))
y = int(input("Enter your number: "))
z = int(input("Enter your number: "))

is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = (z >= 10 and z <= 50)

final_condition = is_even and is_positive and is_in_range

print (final_condition)

# Question 3
print ("Question 3")

score = int(input("Enter your score (0 - 100): "))

bonus_points = 5
late_penalty = -10

final_score = score + 5 - 10

final_score = max(0,  min(100, final_score))


if final_score >= 80:
    grade = "A"

elif final_score >= 70:
    grade = "B"

elif final_score >= 60:
    grade = "C"

elif final_score >= 50:
    grade = "D"
else:
    grade = "F"

print (final_score)
print (grade)

# Question 4
print("Question 4")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

operation = input("Enter an operation (+, -, *, /, %, **): ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"

elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Cannot calculate modulus by zero"

elif operation == "**":
    result = num1 ** num2

else:
    result = "Invalid operation"

print("Result:", result)