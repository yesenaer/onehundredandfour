from game.game import Game, GameState, RowIsFullException
from game.deck import Deck, Card
from game.player import Player
from pytest import raises, fixture, mark


@fixture
def game():
   return Game()


def test_game_init_success(game):
   assert game.state == GameState.PENDING
   assert isinstance(game.deck, Deck)
   assert isinstance(game.players, list)
   assert isinstance(game.row0, list)
   assert isinstance(game.row1, list)
   assert isinstance(game.row2, list)
   assert isinstance(game.row3, list)
   assert len(game.players) == 0


def test_add_player_success(game):
   mario = Player(name="Mario")
   result = game.add_player(mario)
   assert result
   assert len(game.players) == 1
   assert mario in game.players


def test_add_player_gamestate_failure(game):
   game.start()
   mario = Player(name="Mario")
   result = game.add_player(mario)
   assert not result
   assert mario not in game.players


def test_add_player_player_count_failure(game):
   mario = Player(name="Mario")
   luigi = Player(name="Luigi")
   [game.add_player(mario) for i in range(10)]  
   result = game.add_player(luigi)
   assert not result
   assert len(game.players) == 10
   assert luigi not in game.players


def test_start_success(game):
   game.start()
   assert game.state == GameState.ACTIVE


def test_end_success(game):
   game.end()
   assert game.state == GameState.FINISHED

@mark.parametrize("input", [-100, -2, -1, 4, 5, 100])
def test_retrieve_target_row_failures(game, input):
   with raises(ValueError):
      game.retrieve_target_row(row_number=input)


@mark.parametrize("input", [0, 1, 2, 3])
def test_retrieve_target_row_success(game, input):
   rows = [game.row0, game.row1, game.row2, game.row3]
   actual = game.retrieve_target_row(row_number=input)
   assert actual == rows[input]


def test_add_card_to_row_is_full_failure(game):
   # adding up to a full row
   for i in range(5):
      game.add_card_to_row(row_number=0, card=Card(i, 1))
   assert len(game.row0) == 5
   
   with raises(RowIsFullException):
      game.add_card_to_row(row_number=0, card=Card(55, 7))
   
   assert len(game.row0) == 5


def test_add_card_to_row_lower_value_failure(game):
   higher_card = Card(104, 1)
   lower_card = Card(4, 1)
   game.add_card_to_row(row_number=0, card=higher_card)
   assert len(game.row0) == 1
   
   with raises(ValueError):
      game.add_card_to_row(row_number=0, card=lower_card)
   
   assert len(game.row0) == 1
   assert game.row0[-1] == higher_card


def test_add_card_to_row_empty_success(game):
   expected = Card(1,2)
   assert len(game.row1) == 0
   game.add_card_to_row(row_number=1, card=expected)
   assert len(game.row1) == 1


def test_add_card_to_row_non_empty_success(game):
   first_card = Card(55, 7)
   expected = Card(80, 3)
   game.add_card_to_row(row_number=1, card=first_card)
   assert len(game.row1) == 1
   assert game.row1[-1] == first_card
   game.add_card_to_row(row_number=1, card=expected)
   assert len(game.row1) == 2
   assert game.row1[-1] == expected


def test_replace_row_success(game):
   first_card = Card(55, 7)
   second_card = Card(100, 3)
   game.add_card_to_row(row_number=1, card=first_card)
   game.add_card_to_row(row_number=1, card=second_card)
   assert len(game.row1) == 2
   assert game.row1[-1] == second_card

   replacing_card = Card(1, 1)
   replaced = game.replace_row(row_number=1, card=replacing_card)
   assert replaced == [first_card, second_card]
   assert len(game.row1) == 1
   assert game.row1[-1] == replacing_card   


def test_repr_success(game):
   opening_message = "A nice game of onehundredandfour with players:"
   empty_game = f"{opening_message} []. Game is currently {GameState.PENDING}."
   assert repr(game) == empty_game

   player1 = Player(name="Mario")
   player2 = Player(name="Luigi")
   player_names = f"'Mario', 'Luigi'"
   player1_in = f"{opening_message} ['{player1.name}']. Game is currently {GameState.PENDING}."
   game.add_player(player1)
   assert repr(game) == player1_in

   player2_in = f"{opening_message} [{player_names}]. Game is currently {GameState.PENDING}."
   game.add_player(player2)
   assert repr(game) == player2_in

   active = f"{opening_message} [{player_names}]. Game is currently {GameState.ACTIVE}."
   game.start()
   assert repr(game) == active

   ended = f"{opening_message} [{player_names}]. Game is currently {GameState.FINISHED}."
   game.end()
   assert repr(game) == ended
