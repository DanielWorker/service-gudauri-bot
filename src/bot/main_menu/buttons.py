from telethon import Button


def main_menu_btn():
    bots_btn = Button.inline("🤖 Боты", 'mm/bots_menu')
    mentors_btn = Button.inline("🎯 Лиды", 'mm/leads_menu')

    buttons = [[bots_btn], [mentors_btn]]

    return buttons

# ------- Bots --------


def bots_menu_btn(bots):
    buttons = []

    for bot in bots:
        bot_name = bot.user.full_name
        text = f'🤖 {bot_name}'
        buttons.append([Button.inline(text, f'mm/bot_menu/{bot.bot_id}')])

    add_bot_btn = Button.inline("➕ Добавить бота", 'mm/add_bot')
    back_btn = Button.inline("👈🏻 Назад", f'mm/main_menu')
    buttons.append([back_btn, add_bot_btn])

    return buttons


def bot_menu_btn(is_auth):
    buttons = []

    if not is_auth:
        login_btn = Button.inline("🔄 Перезайти в аккаунт", "mm/add_bot")
        buttons.append(login_btn)

    back_btn = Button.inline("👈🏻 Назад", 'mm/bots_menu')
    buttons.append(back_btn)

    return buttons


def cancel_btn():
    return [[Button.text('⭕️ Отмена', resize=True, single_use=True)]]


def leads_menu_btn(leads):
    buttons = []

    for lead in leads:
        lead_name = lead.user.full_name
        created_at_str = lead.created_at.strftime('%Y-%m-%d')
        buttons.append([Button.inline(f'{lead_name} | {created_at_str}', f'mm/lead_menu/{lead.id}')])

    back_btn = Button.inline("👈🏻 Назад", f'mm/main_menu')
    buttons.append([back_btn])

    return buttons


def lead_menu_btn():  # add delete button
    return Button.inline("👈🏻 Назад", f'mm/leads_menu')
