![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
[![Python Unit Tests](https://github.com/yesenaer/onehundredandfour/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/yesenaer/onehundredandfour/actions/workflows/unit-tests.yml)



# onehundredandfour

Coding a backend functionality in honour of a beloved card game. 
App allows for API interaction to create and play the game.
Main language used in this repository is python. 

## setup
- clone the repo
- (suggested) create a virtual environment
- install the dependencies using `pip install .`
    - or include optional dependencies `pip install .[test]` 

## test
- run `pytest .` from root of repo

## run
- run `py .\onehundredandfour\app.py` from root of repo
- api's can be accessed at `host` localhost `port` 8080

### APIs
`/hello` - Here to greet you

`/game/create` - will create a game and return the id of the game

`/game/<id:int>/join/<name>` - allows a player to join a specific game based on id

`/game/<id:int>/start` - starts the game with that id

`/game/<id:int>/stop` - stops the game with that id

`/game/<id:int>/status` - returns information on the game with that id

## build
- (if needed) `pip install build`
- run `py -m build`

## play
Rules of the game can be found at [`docs/rules.md`](docs/rules.md)

## contribute
### suggestions
- report bugs or suggest features using the issues section of github

### code
- create a branch 
- add your suggested feature or fix
- create a pull request
