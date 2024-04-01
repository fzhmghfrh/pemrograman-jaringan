n = int(input())

positive_sum = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        positive_sum += num

print(positive_sum)
