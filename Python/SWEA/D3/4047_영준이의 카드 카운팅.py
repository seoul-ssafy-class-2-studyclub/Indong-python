case_size = int(input())
for case in range(1, case_size + 1):
    cards = input()
    stack = []
    is_error = False
    deck = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    for i in range(0, len(cards) - 2, 3):
        card = (cards[i], cards[i+1:i+3])
        if card in stack:
            is_error = True
            break
        else:
            stack.append(card)
    
    if not is_error:
        for i in range(len(stack)):
            deck[stack.pop()[0]] -= 1
        print(f'#{case} {deck["S"]} {deck["D"]} {deck["H"]} {deck["C"]}')
    else:
        print(f'#{case} ERROR')
        