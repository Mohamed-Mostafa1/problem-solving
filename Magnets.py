magnets = []
result = 1
n = int(input())
for i in range(n):
    magnets.append(input())

for i in range(n-1):
    if magnets[i] != magnets[i + 1]:
        result += 1
print(result)
