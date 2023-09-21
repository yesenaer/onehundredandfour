from game.deck import Deck, Card
from pytest import fixture


@fixture
def deck():
   return Deck()


def test_card_init():
   card = Card(value=5, score=1)
   assert card.value == 5
   assert card.score == 1


def test_deck_count(deck):
   assert isinstance(deck.cards, list)
   assert len(deck.cards) == 104


def test_deck_cards_for_game_values(deck):
   for card in deck.cards:
      assert 0 < card.value < 105
      assert card.score in (1, 2, 3, 5, 7)


def test_deck_shuffle(deck):
   before = deck.cards.copy()
   deck.shuffle()
   after = deck.cards
   assert before != after
   for card in before:
      assert card in after 


def test_deck_shake(deck):
   assert "dad joke" in deck.shake()


def test_deck_deal_one_card_no_shuffle(deck):
   last_card = Card(104, 1)
   assert deck.cards[103] == last_card
   card = deck.deal_one_card() 
   assert card == last_card
     