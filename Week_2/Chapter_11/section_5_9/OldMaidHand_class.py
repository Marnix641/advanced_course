from Week_2.Chapter_11.section_4_10.Card_class import Card
from Week_2.Chapter_11.section_5_9.Hand_class import Hand


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {}: {} matches {}".format(self.name, card, match))
                count += 1
        return count
