
def findItem(theList, item):
    return [(ind+1, theList[ind].index(item)+1) for ind in range(len(theList)) if item in theList[ind]]


matrix = [input().split() for i in range(5)]
matrix2 = []

for mat in matrix:
    matrix2.append(list(map(int, mat)))

for i in findItem(matrix2, 1):
    x, y = i

print(abs(x - 3) + abs(y - 3))
