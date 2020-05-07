from Week_2.Chapter_11.section_4_10.Deck1_class import Deck


class Cardgame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()