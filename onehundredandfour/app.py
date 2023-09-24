from bottle import Bottle, run
from game.game import Game
from game.player import Player


ACTIVE_GAMES = []


def create_app() -> Bottle:
    """Creates a Bottle app instance with api routes.

    Returns:
        Bottle: A Bottle application instance.
    """
    app = Bottle()

    @app.route('/game/create')
    def create_game() -> str:
        """Creates a game and adds it to the active games.

        Returns:
            str: Creation message with game id.
        """
        game = Game()    
        ACTIVE_GAMES.append(game)
        index = ACTIVE_GAMES.index(game)
        return f"Game created, id: {str(index)}"
    
    @app.route('/game/<id:int>/join/<name>')
    def join_game(id: int, name: str) -> str:
        """Tries to join player to game with given id.

        Args:
            id (int): Game id.
            name (str): Name of player joining.

        Returns:
            str: Message of success or failure of joining game.
        """
        game: Game = ACTIVE_GAMES[id]
        player = Player(name=name)
        if game.add_player(player):
            return "success"
        else: 
            del player
            return "mama mia!"
        
    @app.route('/game/<id:int>/start')
    def start_game(id: int) -> str:
        """Tries to start the game with given id.

        Args:
            id (int): Game id.

        Returns:
            str: Start message.
        """
        game: Game = ACTIVE_GAMES[id]
        game.start()
        return "success"
    
    @app.route('/game/<id:int>/stop')
    def stop_game(id: int) -> str:
        """Tries to stop the game with given id.

        Args:
            id (int): Game id.

        Returns:
            str: End message.
        """
        game: Game = ACTIVE_GAMES[id]
        game.end()
        return "success"
    
    @app.route('/game/<id:int>/status')
    def get_game_status(id: int) -> str:
        """Returns string represention of game with given id.

        Args:
            id (int): Game id.

        Returns:
            str: String representation of game.
        """
        game: Game = ACTIVE_GAMES[id]
        return str(game)
    
    @app.route('/hello')
    def hello() -> str:
        """Well hello to you as well!

        Returns:
            str: Greetings!
        """
        return "Hello World!"
    
    return app


if __name__ == '__main__':
    app = create_app()
    run(app, host='localhost', port=8080)