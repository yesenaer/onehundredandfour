from typing import List
from dataclasses import dataclass

@dataclass
class Card:
    """Represents a playing card in the game.
    
    Args:
        value (int): the value determines the order in which it corresponds to other cards. 
        score (int): the penalty score this card brings along.
    """
    value: int
    score: int

    def __init__(self, value: int, score: int):
        self.value = value
        self.score = score


class Deck(): 
    """Contains all possible cards that belong to a game."""
    cards: List

    def __init__(self):
        self.cards = []

        for index in range(1, 105):
            if index == 55: 
                self.cards.append(Card(index, 7))
            elif (len(str(index)) == 2 and str(index)[0] == str(index)[1]):
                self.cards.append(Card(index, 5))
            elif index % 10 == 0:
                self.cards.append(Card(index, 3))
            elif index % 5 == 0: 
                self.cards.append(Card(index, 2))
            else:
                self.cards.append(Card(index, 1))
