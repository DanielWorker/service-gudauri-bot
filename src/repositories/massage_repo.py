from datetime import timedelta, datetime

from sqlalchemy import or_, and_, func

from src.model.users import MassageBooking
import src.settings as stg


class MassageRepository:
    def __init__(self, session):
        self.session = session

    def add_massage_booking(self, user_id, due_date, massage_type, duration):
        massage_booking = MassageBooking(
            user_id=user_id,
            due_date=due_date,
            massage_type=massage_type,
            duration=duration,
        )
        self.session.add(massage_booking)
        self.commit()
        return massage_booking

    def get_massage_booking(self, booking_id):
        return self.session.query(MassageBooking).filter_by(id=booking_id).first()

    def get_massage_booking_for_selected_date(self, due_date):
        if isinstance(due_date, str):
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            due_date = due_date.date()

        return self.session.query(MassageBooking).filter(
            func.date(MassageBooking.due_date) == due_date
        ).order_by(
            MassageBooking.due_date.asc()
        ).all()

    def is_massage_booking_time_available(self, due_date, duration):
        if 1 < duration < 2:
            duration = 2

        due_date = due_date.replace(tzinfo=None)
        end_time = due_date + timedelta(hours=duration)

        overlapping_booking = self.session.query(MassageBooking).filter(
            func.date(MassageBooking.due_date) == due_date.date()
        ).all()

        for booking in overlapping_booking:
            booking_duration = booking.duration
            booking_end_time = booking.due_date + timedelta(hours=booking_duration)

            # Проверяем перекрывает ли новая запись существующую
            if due_date < booking_end_time and end_time > booking.due_date:
                return False  # Время занято

            # Проверяем пересекается ли новая запись с окончанием существующей
            if due_date < booking_end_time < end_time:
                return False  # Время занято

        return True  # Время свободно

    def commit(self):
        try:
            self.session.commit()
        except Exception:
            stg.logger.exception('')
            self.session.rollback()
