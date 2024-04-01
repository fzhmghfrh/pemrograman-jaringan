n = int(input())

key_value_pairs = {}

for _ in range(n):
    key, value = input().split()
    key_value_pairs[key] = int(value)

search_key = input()

print(key_value_pairs[search_key])
