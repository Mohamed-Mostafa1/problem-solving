result = []
name = input()
for s in name:
    while s not in result:
        result.append(s)
if len(result) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
