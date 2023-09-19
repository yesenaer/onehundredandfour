from game.player import Player


def test_player_init_success():
   name = "Mario"
   player = Player(name=name)
   assert player.name == name
   assert isinstance(player.hand, list)
   assert len(player.hand) == 0
   assert player.score == 0
   assert len(player.penalty_cards) == 0
