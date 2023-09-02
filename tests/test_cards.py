from onehundredandfour.game.card import Card
from onehundredandfour.game.cards import Cards

def test_card_init():
   card = Card(value=5, score=1)
   assert card.value == 5
   assert card.score == 1

def test_cards_count():
   count = 0
   for i in vars(Cards).keys():
      if not i.startswith("_"):
         count+=1
   assert count == 104