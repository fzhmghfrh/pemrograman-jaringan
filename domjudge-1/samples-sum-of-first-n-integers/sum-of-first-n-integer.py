num = int(input())

result = 0

if num > 0:
    for i in range(1, num+1):
        result += i
else:
    for i in range(num, 1):
        result += i

print(result)