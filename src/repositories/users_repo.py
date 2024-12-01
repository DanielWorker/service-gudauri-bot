from sqlalchemy import update
from sqlalchemy.orm import selectinload

import src.settings as stg
from src.model.users import User, Bot, RootUser, LeadUser


class UsersRepository:
    def __init__(self, session):
        self.session = session

    def add_user(self, user_id, first_name, last_name=None, username=None):
        user = User(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        self.session.add(user)
        self.commit()
        self.session.refresh(user)

        return user

    def find_user(self, user_id):
        return self.session.query(User).options(
            selectinload(User.root),
            selectinload(User.bot),
        ).filter_by(user_id=user_id).first()

    def update_user(self, user_id: int, **values):
        stmt = update(User).where(User.user_id == user_id).values(**values)
        self.session.execute(stmt)
        self.session.commit()

    def add_root(self, user_id):
        root = RootUser(user_id=user_id)
        self.session.add(root)
        self.commit()
        self.session.refresh(root)

        return root

    def find_root_by_user_id(self, user_id):
        return self.session.query(RootUser).filter_by(user_id=user_id).first()

    def add_bot(self, user_id, phone_number):
        bot = Bot(user_id=user_id, phone_number=phone_number)
        self.session.add(bot)
        self.commit()
        self.session.refresh(bot)

        return bot

    def update_bot(self, bot_id, **values):
        stmt = update(Bot).where(Bot.bot_id == bot_id).values(**values)
        self.session.execute(stmt)
        self.commit()

    def find_bot(self, **values):
        return self.session.query(Bot).options(
            selectinload(Bot.user),
        ).filter_by(**values).first()

    def find_all_bots(self):
        return self.session.query(Bot).options(
            selectinload(Bot.user),
        ).all()

    def add_lead(self, user_id):
        lead_user = LeadUser(
            user_id=user_id,
        )
        self.session.add(lead_user)
        self.session.flush()
        self.commit()

        return lead_user

    def update_lead(self, user_id, **values):
        stmt = update(LeadUser).where(LeadUser.user_id == user_id).values(**values)
        self.session.execute(stmt)
        self.commit()

    def find_lead(self, **values):
        return self.session.query(LeadUser).filter_by(**values).first()

    def find_all_leads(self):
        return self.session.query(LeadUser).order_by(LeadUser.id.desc()).all()

    def commit(self):
        try:
            self.session.commit()
        except Exception:
            stg.logger.exception('')
            self.session.rollback()
