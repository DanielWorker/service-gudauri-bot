from datetime import datetime

from src import utils
from src.user_bots.conversation.templates import massage_dict


def calendar_menu_text():
    return "**📅 Календарь бронирования массажа**"


def selected_date_booking_text(due_date, bookings):
    due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    date_str = utils.convert_date_to_str(due_date.strftime('%d/%m'))

    text = f"**🗓 {date_str}**\n\n"

    for n, booking in enumerate(bookings, start=1):
        user = booking.user

        user_mention = utils.get_user_mention(user.user_id, user.full_name)
        username = f' | @{user.username}' if user.username else ''

        localized_dt = utils.get_localized_datetime(booking.due_date)
        massage_str = massage_dict['russian'][booking.massage_type]
        time_str = localized_dt.strftime("%H:%M")

        text += (f"👤 {user_mention}{username}\n"
                 f"🕒 {time_str}\n"
                 f"💆 {massage_str} | {booking.duration}ч\n\n")

    return text
