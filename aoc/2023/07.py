from collections import Counter
from itertools import product

card_map1 = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}
card_map2 = {
    'T': 10,
    'J': 1,
    'Q': 11,
    'K': 12,
    'A': 13,
}
all_cards = list(map(str, range(2, 10))) + list(card_map1.keys())


counts_to_type_map = {
    (5,): 6,  # Five of a kind
    (1, 4): 5,  # Four of a kind
    (2, 3): 4,  # Full house
    (1, 1, 3): 3,  # Three of a kind
    (1, 2, 2): 2,  # Two pair
    (1, 1, 1, 2): 1,  # One pair
    (1, 1, 1, 1, 1): 0,  # High card
}


def hand_values(hand, card_map):
    return tuple(card_map.get(card) if card in card_map else int(card) for card in hand)


def hand_type(values):
    return counts_to_type_map[tuple(sorted(Counter(values).values()))]


def hand_key1(hand):
    values = hand_values(hand, card_map1)
    return hand_type(values), values


def hand_key2(hand):
    max_type = max(
        hand_type(hand_values(new_hand, card_map2))
        for new_hand in product(
            *[all_cards if card == 'J' else [card] for card in hand]
        )
    )
    return max_type, hand_values(hand, card_map2)


def part1(text):
    hands = [line.split() for line in text.splitlines()]
    hands = sorted(hands, key=lambda x: hand_key1(x[0]))
    return sum((index + 1) * int(bit) for index, (_hand, bit) in enumerate(hands))


def part2(text):
    hands = [line.split() for line in text.splitlines()]
    hands = sorted(hands, key=lambda x: hand_key2(x[0]))
    return sum((index + 1) * int(bit) for index, (_hand, bit) in enumerate(hands))
