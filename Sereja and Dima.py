
sereja, dima = [0, 0]
n = input()
cards = list(map(int, input().split()))
while cards:
    if cards[0] > cards[-1]:
        sereja += cards[0]
        cards.remove(cards[0])
    else:
        sereja += cards[-1]
        cards.remove(cards[-1])
    if not cards:
        break

    if cards[0] > cards[-1]:
        dima += cards[0]
        cards.remove(cards[0])
    else:
        dima += cards[-1]
        cards.remove(cards[-1])


print(sereja, dima)
