from game.deck import Deck, Card
from game.player import Player
from typing import List
from enum import Enum


class GameState(Enum):
    """Enum representing all possible states a game is in. Guarding actions permitted per state."""
    PENDING = 1
    ACTIVE = 2
    FINISHED = 3


class RowIsFullException(Exception):
    """Raised when trying to add an additional card to full row."""
    pass


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
        """Adds player to game as long as there is still room for another player.

        Args:
            player (Player): Player that wants to be added to the game.

        Returns:
            bool: representing if player was successfully added to the game.
        """
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
    
    def start(self):
        """Starts the game. Causing the GameState to change to Active."""
        self.state = GameState.ACTIVE
        # shuffle cards 
        # give each player a hand of cards 
        # populate rows 

    def end(self):
        """Ends the game. Causing the GameState to change to Finished."""
        self.state = GameState.FINISHED
        # mention if not all rounds are done?
        # calculate and return loser / winner

    def retrieve_target_row(self, row_number: int) -> list:
        """Retrieves target row based on received integer.

        Args:
            row_number (int): The targeted row, where possible values are 0, 1, 2 or 3.

        Raises:
            ValueError: upon receiving an invalid row number argument.

        Returns:
            list: the target row.
        """
        if 0 > row_number or row_number > 3: 
            print(f"Row number invalid. Please provide valid row number.")
            raise ValueError("Row number invalid.")
        
        row_index = [self.row0, self.row1, self.row2, self.row3]
        return row_index[row_number]
    
    def add_card_to_row(self, row_number: int, card: Card):
        """Tries to add given card to row. Will fail in case of wrong values or full row.

        Args:
            row_number (int): The targeted row, where possible values are 0, 1, 2 or 3.
            card (Card): The card that needs to be added to the row.

        Raises:
            ValueError: upon receiving an invalid row number argument.
            RowIsFullException: upon trying to add a card to a row with length of 5.
        """
        target_row = self.retrieve_target_row(row_number)
        
        if len(target_row) > 0:
            if target_row[-1].value >= card.value:
                raise ValueError("Card does not meet requirements to be added.")

        if len(target_row) < 5:
            target_row.append(card)
        else:
            raise RowIsFullException()
 
    def replace_row(self, row_number: int, card: Card) -> list:
        """Replaces the current cards in row for the given card.

        Args:
            row_number (int): The targeted row, where possible values are 0, 1, 2 or 3.
            card (Card): The card that replaces other cards for the row.

        Raises:
            ValueError: upon receiving an invalid row number argument.

        Returns:
            list: the list of cards that were replaced.
        """
        target_row = self.retrieve_target_row(row_number)
        penalty_row = target_row.copy()
        target_row.clear()
        target_row.append(card)
        return penalty_row

    def __repr__(self) -> str:
        """Generates a string with details of this game instance."""
        names = [player.name for player in self.players]
        return f"A nice game of onehundredandfour with players: {names}. Game is currently {self.state}."
