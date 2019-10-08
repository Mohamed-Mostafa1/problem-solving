anton, danik = 0, 0
n = input()
string = input()
for s in string:
    if s == 'A':
        anton += 1
    elif s == 'D':
        danik += 1
if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')