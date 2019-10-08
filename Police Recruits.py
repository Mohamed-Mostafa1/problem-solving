avlCops, result  = 0, 0
n = input()
crimes = list(map(int, input().split()))
for crime in crimes:
    if crime > 0 :
        avlCops += crime
    else:
        if avlCops:
            avlCops += crime
        else:
            result += 1
print(result)

