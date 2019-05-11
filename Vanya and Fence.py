width = 0
friends = []
n, h = map(int, input().split())
friends = input().split()
for i in friends:
    if int(i) > h:
        width += 2
    else:
        width += 1
print(width)
