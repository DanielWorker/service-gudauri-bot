from telethon.utils import resolve_id

from src.bot import utils
import src.settings as stg


def main_menu_text(user, bots):
    role = (
        '🏆 Админ' if user.root else
        '🤖 Бот' if user.bot else ''
    )

    text = (f'Привет, **{user.first_name}!**\n'
            f'**Твоя роль:** {role}\n\n')

    bot_user_ids = [bot.user_id for bot in bots]

    if stg.all_service_gudauri_user_id in bot_user_ids:
        text += '⛷ Бот @AllServiceGudauri подключен\n'
    else:
        text += '⛷ Бот @AllServiceGudauri не подключен\n'

    return text


def access_denied_text():
    return (f'🛑 **Отказано в доступе**\n\n'
            f'Пожалуйста, свяжитесь с администратором для получения доступа к меню')


def invalid_user_text():
    return '🔎 Юзер не найден, попробуйте еще раз'


def bots_menu_text(bots):
    return '**🤖 Боты**'


def bot_menu_text(bot, is_authorized):
    status_text = 'Бот работает' if is_authorized else 'Бот не работает, нужно перезайти в сессию'

    text = (f'**🤖 {bot.user.full_name}**\n\n'
            f'ℹ️ Статус: {status_text}')
    return text


def add_bot_menu_text():
    return ('✍️ Введите номер телефона бот-аккаунта\n'
            '__Формат: +1234567890__')


def leads_menu_text():
    return '**🎯 Лиды**'


def lead_menu_text(lead):
    user_mention = utils.get_user_mention(lead.user_id, lead.user.full_name)
    username = f' | @{lead.user.username}' if lead.user.username else ''

    created_at_str = lead.created_at.strftime('%Y-%m-%d %H:%M')

    return (
        f"👤 {user_mention}{username}\n"
        f"🕒 {created_at_str}"
    )
