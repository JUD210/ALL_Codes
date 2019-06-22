"""
loop repeats an unknown number of times and ends when some condition is met.
"""

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)
