from typing import List 
from game.deck import Card

class Player:
    """Represents the details of a player participating in a game."""
    name: str
    hand: List[Card]
    score: int = 0
    penalty_cards = List[Card]

    def __init__(self, name: str) -> None:
        self.name = name.strip()
        self.hand = []
        self.penalty_cards = []