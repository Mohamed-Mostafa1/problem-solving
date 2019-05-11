result = 0
problems = []
n = int(input())
for i in range(n):
    problems.append(map(int, input().split()))

for i in problems:
    if sum(i) > 1:
        result += 1
print(result)
