s = input()
moves, strt = 0, 0
for l in s:
    index = ord(l) - 97
    walk = abs(strt - index)
    if walk < 13:
        moves += walk
    else:
        moves += 26 - walk
    strt = index

print(moves)
