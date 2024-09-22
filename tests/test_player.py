from uuid import UUID
from game.player import Player
from game.deck import Deck, Card
from pytest import raises, fixture


@fixture
def mario():
   return Player(name="Mario")
   

def test_player_init():
   name = "Mario"
   player = Player(name=name)
   assert isinstance(player.id, UUID) 
   assert player.name == name
   assert isinstance(player.hand, list)
   assert len(player.hand) == 0
   assert player.score == 0
   assert len(player.penalty_cards) == 0
   assert player.card_to_play is None


def test_player_set_card_to_play_empty(mario):
   expected = Card(104, 1)
   deck = Deck()
   for i in range(10):
      mario.hand.append(deck.cards.pop())
   assert expected in mario.hand
   mario.set_card_to_play(expected)
   assert mario.card_to_play == expected
   assert expected not in mario.hand


def test_player_set_card_to_play_occupied(mario):
   deck = Deck()
   for i in range(10):
      mario.hand.append(deck.cards.pop())

   existing = Card(103, 1)
   mario.set_card_to_play(existing)
   assert mario.card_to_play == existing
   assert existing not in mario.hand

   expected = Card(104, 1)
   assert expected in mario.hand
   mario.set_card_to_play(expected)
   assert mario.card_to_play == expected
   assert expected not in mario.hand
   assert existing in mario.hand


def test_player_set_card_to_play_failure(mario):
   deck = Deck()
   for i in range(10):
      mario.hand.append(deck.cards.pop())
   expected = Card(1, 1)  # card is not in hand
   with raises(Exception):
      mario.set_card_to_play(expected)


def test_player_add_penalty_cards(mario):
   card_1 = Card(1, 1)
   card_55 = Card(55, 7)
   cards = [card_1, card_55]
   
   assert mario.score == 0
   assert len(mario.penalty_cards) == 0
   mario.add_penalty_cards(cards=cards)
   assert mario.score == 8
   assert mario.penalty_cards == cards
   assert card_1 in mario.penalty_cards and card_55 in mario.penalty_cards


def test_player_add_penalty_cards_empty(mario):
   cards = []
   assert mario.score == 0
   assert len(mario.penalty_cards) == 0
   mario.add_penalty_cards(cards=cards)
   assert mario.score == 0
   assert len(mario.penalty_cards) == 0


def test_player_str(mario):
   assert str(mario) == "Mario"
