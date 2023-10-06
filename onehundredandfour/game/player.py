from typing import List 
from uuid import uuid4, UUID
from game.deck import Card

class Player:
    """Represents the details of a player participating in a game."""
    id: UUID
    name: str
    hand: List[Card]
    card_to_play: Card
    score: int = 0
    penalty_cards = List[Card]

    def __init__(self, name: str) -> None:
        self.id = uuid4()
        self.name = name.strip()
        self.hand = []
        self.penalty_cards = []
        self.card_to_play = None

    def set_card_to_play(self, card: Card) -> None:
        """Activates a card that is going to be played in this round.

        Args:
            card (Card): the card that needs to be played.

        Raises:
            Exception: If requested card is not playable for player.
        """
        if card not in self.hand:
            raise Exception("Unable to play card that is not in hand.")
        
        if isinstance(self.card_to_play, Card):
            self.hand.append(self.card_to_play)  # remove existing card

        self.hand.remove(card)
        self.card_to_play = card

    def add_penalty_cards(self, cards: list[Card]) -> None:
        """Processes the penalty cards received by player to both the penalty_cards and score variables.

        Args:
            cards (list[Card]): the penalty cards received by player.
        """
        for card in cards:
            self.penalty_cards.append(card)
            self.score += card.score

    def __str__(self) -> str:
        """Returns player's name as string representation of the instance.

        Returns:
            str: the players name.
        """
        return self.name
