from typing import List 
from onehundredandfour.game.deck import Card

class Player:
    """Represents the details of a player participating in a game."""
    name: str
    hand: List[Card]
    score: int = 0

    def __init__(self, name: str) -> None:
        self.name = name.strip()
        self.hand = []