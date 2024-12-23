import calendar
from datetime import date

from telethon import Button

cancel_btn = Button.inline('⭕️', "cancel_button")


def calendar_menu_btn(repo, year=None, month=None):
    if year and month:
        date_obj = date(year, month, 1)
    else:
        date_obj = date.today()

    formatted_date = date_obj.strftime("%B")
    # Year button
    today_date = date.today()
    year_diff = date_obj.year + 1 if date_obj.year < today_date.year + 1 else today_date.year
    year_btn = Button.inline(f'{date_obj.year}', f'ms/navigate_calendar/{year_diff}/{date_obj.month}')

    last_row_btn = [
        cancel_btn,
        Button.inline(f'{formatted_date}', f'ms/select_month/{date_obj.year}'),
        year_btn
    ]
    # calendar buttons
    calendar_btn = generate_calendar_markup(date_obj.year, date_obj.month, repo)
    buttons = calendar_btn + [last_row_btn]
    return buttons


def generate_calendar_markup(year, month, repo):
    _, num_days = calendar.monthrange(year, month)

    buttons = [[Button.inline(day[:2], "") for day in calendar.weekheader(2).split()]]

    for week in calendar.monthcalendar(year, month):
        row = []
        for day in week:
            if day == 0 or day > num_days:
                row.append(Button.inline(" ", " "))
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"
                bookings = repo.get_massage_booking_for_selected_date(date_str)

                day_text = f'({str(day)})' if bookings else str(day)

                row.append(Button.inline(day_text, f'ms/select_calendar_date/{date_str}'))
        buttons.append(row)

    return buttons


def select_month_btn(year):
    buttons = [[]]
    for month_num in range(1, 13):
        if len(buttons[-1]) == 4:
            buttons.append([])
        month_name = calendar.month_name[month_num]
        buttons[-1].append(Button.inline(month_name, f'ms/navigate_calendar/{year}/{month_num}'))
    buttons.append([Button.inline('📅', f'ms/calendar_menu')])
    return buttons


def back_to_calendar_menu_btn():
    return Button.inline('📅', f'ms/calendar_menu')

