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


def test_player_set_card_to_play_occupied():
   player = Player("Mario")
   deck = Deck()
   for i in range(10):
      player.hand.append(deck.cards.pop())

   existing = Card(103, 1)
   player.set_card_to_play(existing)
   assert player.card_to_play == existing
   assert existing not in player.hand

   expected = Card(104, 1)
   assert expected in player.hand
   player.set_card_to_play(expected)
   assert player.card_to_play == expected
   assert expected not in player.hand
   assert existing in player.hand


def test_player_set_card_to_play_failure():
   player = Player("Mario")
   deck = Deck()
   for i in range(10):
      player.hand.append(deck.cards.pop())
   expected = Card(1, 1)  # card is not in hand
   with raises(Exception):
      player.set_card_to_play(expected)


def test_player_str():
   player = Player("Mario")
   assert str(player) == "Mario"
