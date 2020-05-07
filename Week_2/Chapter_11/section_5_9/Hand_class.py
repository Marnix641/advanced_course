from Week_2.Chapter_11.section_4_10.Deck1_class import Deck


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def __add__(self, card):
        self.cards.append(card)

    def __str__(self):
        s= "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)



