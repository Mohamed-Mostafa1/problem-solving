def countOfTarget(string, target):
    count = 0
    for s in string:
        if int(s) == target:
            count += 1
    return count



result = 0
values = list(map(int, input().split()))
s = input()
for i in range(1, 5):
    result += countOfTarget(s, i) * values[i-1]
print(result)
