from app import create_app, ACTIVE_GAMES
from webtest import TestApp
from pytest import fixture


@fixture(scope="module")
def webapp():
   yield TestApp(create_app())
   global ACTIVE_GAMES
   ACTIVE_GAMES = []


@fixture
def prepared_game(webapp):
   result = webapp.get('/game/create')
   id = result.text.replace('Game created, id: ', '')
   webapp.get(f'/game/{id}/join/mario')
   webapp.get(f'/game/{id}/join/luigi')
   return id, webapp


def test_app_hello(webapp):
   result = webapp.get('/hello')
   assert result.status_code == 200
   assert result.text == "Hello World!"


def test_app_create_game(webapp):
   assert len(ACTIVE_GAMES) == 0
   result = webapp.get('/game/create')
   assert result.status_code == 200
   assert result.text == "Game created, id: 0"
   assert len(ACTIVE_GAMES) == 1


def test_app_join_game(webapp):
   result = webapp.get('/game/0/join/mario')
   assert result.status_code == 200
   assert result.text == "success"
   

def test_app_start_game(prepared_game):
   id, game = prepared_game
   status1 = game.get(f'/game/{id}/status')
   expected1 = "A nice game of onehundredandfour with players: ['mario', 'luigi']. Game is currently GameState.PENDING."
   assert status1.status_code == 200
   assert status1.text == expected1
   game.get(f'/game/{id}/start')
   result = game.get(f'/game/{id}/start')
   assert result.status_code == 200
   assert result.text == "success"
   status2 = game.get(f'/game/{id}/status')
   expected2 = "A nice game of onehundredandfour with players: ['mario', 'luigi']. Game is currently GameState.ACTIVE."
   assert status2.status_code == 200
   assert status2.text == expected2


def test_app_end_game(prepared_game):
   id, game = prepared_game
   status1 = game.get(f'/game/{id}/status')
   expected1 = "A nice game of onehundredandfour with players: ['mario', 'luigi']. Game is currently GameState.PENDING."
   assert status1.status_code == 200
   assert status1.text == expected1
   game.get(f'/game/{id}/start')
   result = game.get(f'/game/{id}/stop')
   assert result.status_code == 200
   assert result.text == "success"
   status2 = game.get(f'/game/{id}/status')
   expected = "A nice game of onehundredandfour with players: ['mario', 'luigi']. Game is currently GameState.FINISHED."
   assert status2.status_code == 200
   assert status2.text == expected
