from onehundredandfour.game.deck import Deck, Card

def test_card_init():
   card = Card(value=5, score=1)
   assert card.value == 5
   assert card.score == 1


def test_deck_count():
   deck = Deck()
   assert isinstance(deck.cards, list)
   assert len(deck.cards) == 104


def test_deck_cards_for_game_values():
   deck = Deck()
   for card in deck.cards:
      assert 0 < card.value < 105
      assert card.score in (1, 2, 3, 5, 7)