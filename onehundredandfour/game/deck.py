from typing import List
from dataclasses import dataclass
from random import shuffle

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


class Deck: 
    """Contains all possible cards that belong to a game."""
    cards: List

    def __init__(self) -> None:
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

    def shuffle(self) -> None:
        """Randomizes order of the cards list belonging to the instance."""
        shuffle(self.cards)

    def shake(self) -> str:
        """Every dad-like person. Every card game.
        
        Returns:
            str: Try and you will found out!
        """
        water_chicken = "\n(o< QUACK! \n<_)\t\tDad joke found!\n\n"
        return f"{water_chicken}Insert dad joke about waving cards around without randomizing order."
    
    def deal_one_card(self) -> Card:
        """Removes one card from cards list and returns that card.

        Returns:
            Card: The card that was removed from the cards list.
        """
        return self.cards.pop()
