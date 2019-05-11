n = input()
cubes = list(map(int,input().split()))
cubes.sort()
for i in cubes:
    print(i, sep='', end= ' ')
