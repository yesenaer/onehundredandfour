from dataclasses import dataclass

@dataclass
class Card:
    """Represents a playing card in the game.
    
    Args:
        value (int): the value determines the order in which it corresponds to other cards. 
                     Value should be between 1 - 104. 
        score (int): the penalty score this card brings along.
                     Score should be one of [1, 2, 3, 5, 7].
    """
    value: int
    score: int

    def __init__(self, value: int, score: int):
        if not(value > 0 and value <= 104):
            raise Exception("Card value should be between 1 and 104.")
        
        score_options = [1, 2, 3, 5, 7]
        if not score in score_options:
            raise Exception(f"Card score should be one of following: {score_options}")
        
        self.value = value
        self.score = score
