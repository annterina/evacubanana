from app.domain.islands import Islands
from app.domain.models.game import Game

MAX_ISLAND_NOTES = 50


def update_island_from_game(islands: Islands, game: Game):
    island = islands.get_island(game.island_seed)
    if not island:
        print(f'Island {game.island_seed} not found')
        return

    island['top_scores'].append({'user': game.username, 'score': game.score})
    island['top_scores'] = sorted(island['top_scores'], key=lambda user_score: user_score['score'], reverse=True)[:3]

    island['notes'].extend(list(map(lambda note: note.model_dump(), game.notes)))

    island['playable'] = len(island['notes']) < MAX_ISLAND_NOTES

    islands.update_island(island)
