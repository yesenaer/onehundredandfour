from bottle import Bottle, run
from game.game import Game
from game.player import Player


ACTIVE_GAMES = []


def create_app() -> Bottle:
    app = Bottle()

    @app.route('/game/create')
    def create_game() -> str:
        game = Game()    
        ACTIVE_GAMES.append(game)
        index = ACTIVE_GAMES.index(game)
        return f"Game created, id: {str(index)}"
    
    @app.route('/game/<id:int>/join/<name>')
    def join_game(id: int, name: str) -> str:
        game: Game = ACTIVE_GAMES[id]
        player = Player(name=name)
        if game.add_player(player):
            return "success"
        else: 
            return "mama mia!"
        
    @app.route('/game/<id:int>/start')
    def start_game(id: int) -> str:
        game: Game = ACTIVE_GAMES[id]
        game.start_game()
        return "success"
    
    @app.route('/game/<id:int>/stop')
    def start_game(id: int) -> str:
        game: Game = ACTIVE_GAMES[id]
        game.end_game()
        return "success"
    
    @app.route('/game/<id:int>/status')
    def get_game_status(id: int) -> str:
        game: Game = ACTIVE_GAMES[id]
        return repr(game)
    
    @app.route('/hello')
    def hello() -> str:
        return "hello world!"
    
    return app


if __name__ == '__main__':
    app = create_app()
    run(app, host='localhost', port=8080)