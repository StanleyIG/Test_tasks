from collections import Counter

def diversity(a, b):
    """
    Повторяющиеся карточки подсчитываю с помощью Counter
    Функция для вычисления разнообразия коллекций
    """
    a_counter = Counter(a)
    b_counter = Counter(b)
    remaining_cards = sum((a_counter - b_counter).values()) + sum((b_counter - a_counter).values())
    return remaining_cards


def update_cards(q):
    """добавить / удалить из коллекции и вычислить оставшиеся карточки"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = []
    for _ in range(q):
        change, player, card = input().split()
        card = int(card)
    
        if change == "1":
            if player == "A":
                a.append(card)
            else:
                b.append(card)
        else:
            if player == "A":
                a.remove(card)
            else:
                b.remove(card)

        res.append(diversity(a, b))
    return res
    
n, m, q = map(int, input().split()) # для n и m не нашёл применения
result = update_cards(q)
print(*result) 


# Способ 2, хранение и счёт кол-ва карт с помощью словаря
def diversity(a, b):
    """
    Функция для вычисления разнообразия коллекций
    """
    a_counter = {}
    b_counter = {}

    for card in a:
        a_counter[card] = a_counter.get(card, 0) + 1

    for card in b:
        b_counter[card] = b_counter.get(card, 0) + 1

    remaining_cards = sum(max(a_counter.get(card, 0) - b_counter.get(card, 0), 0) for card in a_counter)\
        + sum(max(b_counter.get(card, 0) - a_counter.get(card, 0), 0) for card in b_counter)
    return remaining_cards


def update_cards(q):
    """добавить / удалить из коллекции и вычислить оставшиеся карточки"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = []
    for _ in range(q):
        change, player, card = input().split()
        card = int(card)
    
        if change == "1":
            if player == "A":
                a.append(card)
            else:
                b.append(card)
        else:
            if player == "A":
                a.remove(card)
            else:
                b.remove(card)

        res.append(diversity(a, b))
    return res
    
# n, m, q = map(int, input().split())
# result = update_cards(q)
# print(*result)

