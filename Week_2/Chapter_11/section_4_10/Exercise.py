from Week_2.Chapter_11.section_4_10.Card_class import Card
from Week_2.Chapter_11.section_4_10.Deck1_class import Deck


test = Card(0, 2)
red_deck = Deck()

print(test)
print(red_deck)

red_deck.shuffle()
print(red_deck)

red_deck.pop()
print(red_deck)

