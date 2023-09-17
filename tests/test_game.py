from game.game import Game, GameState
from game.deck import Deck
from game.player import Player


def test_game_init():
   game = Game()
   assert game.state == GameState.PENDING
   assert isinstance(game.deck, Deck)
   assert isinstance(game.players, list)
   assert isinstance(game.row0, list)
   assert isinstance(game.row1, list)
   assert isinstance(game.row2, list)
   assert isinstance(game.row3, list)
   assert len(game.players) == 0


def test_add_player_success():
   game = Game()
   mario = Player(name="Mario")
   result = game.add_player(mario)
   assert result
   assert len(game.players) == 1
   assert mario in game.players


def test_add_player_failed_gamestate():
   game = Game()
   game.start_game()
   mario = Player(name="Mario")
   result = game.add_player(mario)
   assert not result
   assert mario not in game.players


def test_add_player_failed_player_count():
   game = Game()
   mario = Player(name="Mario")
   luigi = Player(name="Luigi")
   [game.add_player(mario) for i in range(10)]  
   result = game.add_player(luigi)
   assert not result
   assert len(game.players) == 10
   assert luigi not in game.players


def test_start_game():
   game = Game()
   game.start_game()
   assert game.state == GameState.ACTIVE


def test_end_game():
   game = Game()
   game.end_game()
   assert game.state == GameState.FINISHED