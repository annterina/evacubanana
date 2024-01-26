from fastapi import APIRouter

from app.domain.games import Games, Game


class GamesRouter:
    def __init__(self, games: Games) -> None:
        self.__games = games

    @property
    def router(self):
        api_router = APIRouter(prefix='/games', tags=['games'])

        @api_router.post('/')
        def create_game(game: Game):
            return self.__games.create_game(game)

        return api_router