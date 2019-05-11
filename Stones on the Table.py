result = 0
n = int(input())
s = input()
for i in range(n-1):
    if s[i] == s[i+1]:
        result += 1

print(result)