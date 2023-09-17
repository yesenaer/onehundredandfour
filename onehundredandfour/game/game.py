from game.deck import Deck, Card
from game.player import Player
from typing import List
from enum import Enum


class GameState(Enum):
    """Enum representing all possible states a game is in. Guarding actions permitted per state."""
    PENDING = 1
    ACTIVE = 2
    FINISHED = 3


class Game:
    """Contains all elements of the game."""
    deck: Deck
    players: List[Player]
    row0: List[Card]
    row1: List[Card]
    row2: List[Card]
    row3: List[Card]
    state: GameState

    def __init__(self) -> None:
        self.state = GameState.PENDING
        self.deck = Deck()
        self.players = []
        self.row0 = []
        self.row1 = []
        self.row2 = []
        self.row3 = []

    def add_player(self, player: Player) -> bool:
        if self.state != GameState.PENDING:
            print(f"Game is no longer in pending state, unable to add player.")
            return False
        
        if len(self.players) >= 10:
            print(f"Maximum amount of players reached, unable to add player.")
            return False
        
        print(f"adding player {player.name} to game")
        self.players.append(player)
        print(f"current amount of players: {len(self.players)}")
        return True
    
    def start_game(self):
        self.state = GameState.ACTIVE
        # shuffle cards 
        # give each player a hand of cards 
        # populate rows 

    def end_game(self):
        self.state = GameState.FINISHED
        # mention if not all rounds are done?
        # calculate and return loser / winner

    def __repr__(self) -> str:
        names = [player.name for player in self.players]
        return f"A nice game of onehundredandfour with players: {names}. Game is currently {self.state}."




