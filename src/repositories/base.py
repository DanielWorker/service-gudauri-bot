from src.repositories.massage_repo import MassageRepository
from src.repositories.users_repo import UsersRepository


class BaseRepository(UsersRepository, MassageRepository):
    def __init__(self, session):
        super().__init__(session)
