from Week_2.Chapter_11.section_4_10.Card_class import Card
from Week_2.Chapter_11.section_5_9.Cardgame_class import Cardgame
from Week_2.Chapter_11.section_5_9.OldMaidHand_class import OldMaidHand
from Week_2.Chapter_11.section_5_9.Hand_class import Hand
from Week_2.Chapter_11.section_4_10.Deck1_class import Deck


class OldMaidGame(Cardgame):
    def play(self, names):
        self.deck.remove(Card(0,12))
        self.hands =[]
        for name in names:
            self.hands.append(OldMaidHand(name))

        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

if __name__ == "__main__":
    game = OldMaidGame()
    game.play(["Marnix", "Bastiaan"])
