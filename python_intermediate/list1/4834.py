T = int(input())
for t in range(T):
    N = int(input())
    cards = input() 
    cards_count = [0] * 10
    for card in cards:
        cards_count[int(card)] += 1

    most_count = max(cards_count)
    cards_count.reverse()
    print(f'#{t + 1} {9 - cards_count.index(most_count)} {most_count}')
