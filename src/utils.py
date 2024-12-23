from datetime import datetime
import src.settings as stg

import pytz


def convert_time_to_utc(dt):
    # local_timezone = pytz.timezone('Asia/Tbilisi')
    # localized_dt = local_timezone.localize(dt)
    # localized_dt = dt.replace(tzinfo=None)

    utc_dt = dt.astimezone(pytz.UTC)

    return utc_dt


def get_localized_datetime(datetime_obj=None):
    if not datetime_obj:
        datetime_obj = datetime.utcnow()

    timezone = pytz.timezone('Asia/Tbilisi')
    return pytz.utc.localize(datetime_obj).astimezone(timezone)


def combine_and_localize_datetime(date, time):
    current_year = datetime.now().year

    dt_str = f"{current_year}/{date} {time}"
    dt_obj = datetime.strptime(dt_str, "%Y/%d/%m %H:%M")

    tz = pytz.timezone('Asia/Tbilisi')
    localized_date_time = tz.localize(dt_obj)

    if localized_date_time.month < 12 and localized_date_time.year == 2024:
        localized_date_time = localized_date_time.replace(year=localized_date_time.year + 1)

    return localized_date_time


def convert_date_to_str(date_str):
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]

    # Преобразуем строку в объект datetime
    date_obj = datetime.strptime(date_str, "%d/%m")

    day = int(date_obj.day)
    month = months[date_obj.month - 1]  # Месяцы начинаются с 1, поэтому вычитаем 1

    return f"{day} {month}"


def get_user_mention(user_id, name):
    return f'[{name}](tg://user?id={user_id})'


def get_path_to_asset(image_name):
    return stg.path_to_assets + image_name
