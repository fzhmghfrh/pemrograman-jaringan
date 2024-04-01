num1 = int(input())
num2 = int(input())
num3 = int(input())

maximum = num1

if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

print(maximum)
