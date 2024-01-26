from app.repository.islands import Islands as IslandsRepository


class Islands:
    def __init__(self, repository: IslandsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_island(self, seed: int):
        return self.__repository.get_island(seed)

    def get_random(self):
        return self.__repository.get_random()