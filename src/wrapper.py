from functools import wraps

from src.database import session_maker
from src.repositories.users_repo import UsersRepository


# def with_session(handler):
#     async def wrapper(event):
#         with session_maker() as session:
#             await handler(event, session)
#     return wrapper
#
#
# def with_users_repo(handler):
#     async def wrapper(event):
#         with session_maker() as session:
#             users_repo = UsersRepository(session)
#             await handler(event, users_repo)
#     return wrapper


def with_session(handler):
    async def wrapper(*args, **kwargs):
        with session_maker() as session:
            await handler(*args, session=session, **kwargs)
    return wrapper


def with_repo(handler):
    async def wrapper(*args, **kwargs):
        with session_maker() as session:
            users_repo = UsersRepository(session)
            await handler(*args, users_repo=users_repo, **kwargs)
    return wrapper
