from Week_2.Chapter_11.section_5_9.Cardgame_class import Cardgame
from Week_2.Chapter_11.section_5_9.OldMaidHand_class import OldMaidHand
from Week_2.Chapter_11.section_5_9.Oldmaidgame_class import OldMaidGame


game = Cardgame()
hand = OldMaidHand("frank")
game.deck.deal([hand], 13)
