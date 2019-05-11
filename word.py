upper, lower = [0, 0]
string = input()
for s in string:
    if s.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())
    