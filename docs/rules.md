# onehundredandfour

Is in honor of a beloved existing card game.
This document describes the contents and rules of the game.


## Setting
The game can be played with up to 10 players. The game is played with cards.  
Each player will receive a hand of cards out of the deck, which will be used to play with during the game.
The game is played in rounds. Where each round requires an action of every player.
After completing all rounds, the game ends and the winner is determined.
The goal of the game is to score the least amount of penalty points.


### Cards
The game contains 104 cards - called the deck. Each individual card has a face value and a (penalty) score.
The face value is a number ranging from 1 - 104. The face value is used to determine the sequence in which the cards are used and placed.
The penalty points are either 1, 2, 3, 5 or 7. The penalty points are used to determine who wins (or loses) the game.
At the start of the game, the deck is shuffled to randomize the order of the cards. After that, each player will receive 10 cards as hand. 
In case the game is played with less than 10 players, part of the deck remains unused.


### Playing Field
Next to players, the game contains a playing field. The field simulates 4 rows in which cards can be placed. 
At the start of the game, a random card from the deck is placed in the first position of each row. Over the course of the game, cards are added in these rows.
Each row has a capacity of 5 cards. Once a 6th card is presented to the row, the cards of the row are cleared and the card that came as 6th card is placed at the beginning of the row. The cleared cards' penalty points are given to the player that owned the 6th card. 


### Rounds
The game is played in 10 rounds. Each round has a series of events that take place. 
At the start of each round, all players choose one card out of their hand an put it into play. The chosen card remains hidden for other players until the next event.
Once all players have chosen their card, the cards are reveiled. The cards will be applied to the rows in ascending numerical order of face value.
This means that the player that played the card with lowest face value gets to take first action.
The card needs to be placed at the end of the row where:
- Your card's face value is higher than the last card of that row.
- The least difference between your card's face value and the last card of that row.

In case the placed card would be the 6th card in that row, the player is forced to replace all cards from that row with the played card.
This action will cause the player to receive the penalty points of the replaced cards. 

(only applicable for first player)
In case your card cannot meet this criteria for any of the rows, the player is allowed to replace one full row of cards with the played card.
This action will cause the player to receive the penalty points of the replaced card(s).

Once the action is completed, this procedure is repeated in acending order of face value for all other players.
When all cards are processed, the round completes and a new round can be started until all 10 rounds complete.


### Winner
Once all 10 rounds have been completed, the scores can be determined.
All received penalty points are added up per player. 
The player with the least amount of penalty points is the winner of the game!


## Drawn Explanation

### Pending State
- #### Game Creation

![Dealing the cards](/docs/drawings/game_creation.svg)


### Active State
- #### Dealing the cards from deck:
    - 1 per row
    - 10 per player

![Dealing the cards](/docs/drawings/deal_cards.svg)


- #### Play a round 

    - ##### Card fits 
    - ##### Card is too low
    - ##### Row is full


### Finished State
- #### Determine the winner
    - Least amount of penalty points wins!

![Determine the winner](/docs/drawings/determine_winner.svg)