from datetime import datetime, timedelta

from src import utils


def select_language_text():
    return ("Выберите язык напишите цифру/слово\n"
            "Choose language with number/word\n"
            "1 `Русский`\n"
            "2 `English`\n")


def select_language_error():
    return ("Пожалуйста попробуйте еще раз\n"
            "Please try again")

def all_services_text(lang):  # removed 6. 🚕Transfer
    if lang == "english":
        text = """Write number/word, what do you want?

1. 🎿Equipment sale 
2. ⛷Instructor    
3. 💆Massage                
4. 💵Exchange
5. 🪂Paragliding      

Ski-lift Open/Closed 🟢🔴 
Road status 🟢🔴
[Check](https://t.me/ASG_Status)
"""
    else:  # removed 4. 🚕Трансфер
        text = """Здравствуйте, напишите цифру/слово
1. 🎿Распродажа снаряжения
2. ⛷Инструктор    
3. 💆Массаж
4. 💵Обмен валют      
5. 🪂Полет на параплане

Статус подъемников 🟢🔴
Статус авто дорог из-за снега 🟢🔴
[Проверить](https://t.me/ASG_Status)
"""

    return text


# ======== Sale Equipment ========
def sale_equipment_info_text(lang):
    texts = {
        'english': """Gudauri Sale
Follow the link and select your equipment:
https://t.me/Ski_equipment_sale_used

To purchase, write to:
https://t.me/kolsonov

__To return to the menu, type 'menu' / 'cancel' / 'no'__""",
        "russian": """Распродажа Гудаури
Перейдите по ссылке и выберите снаряжение:
https://t.me/Ski_equipment_sale_used

Для покупки, напишите:
https://t.me/kolsonov

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__""",
    }
    return texts.get(lang)


# ======== Rent Equipment ========
def rent_equipment_info_text(lang):
    if lang == "english":
        return """
**🏂 Rental @AllServiceGudauri**
🕒 9.00 - 18.30 🕒
1-3 consecutive days: **47.5₾ (18$)/day** per set
4-6 consecutive days: **42₾/day** per set
7 or more consecutive days: **35₾/day** per set

**🎿 Set includes:**
1. Skis, poles, boots, helmet
2. Snowboard, boots, helmet
3. Jacket, pants, goggles

**Additional items:**
4. Skis + poles / snowboard: **39₾/day**
5. Goggles: **10₾/day**
6. Helmet: **10₾/day**
7. Gloves: **10₾/day**
8. Protective shorts: **10₾/day**
9. Jacket: **20₾/day**
10. Pants: **20₾/day**"""
    else:
        return """
**🏂 Прокат @AllServiceGudauri**
🕒 9.00 - 18.30 🕒
1-3 дня подряд: **47,5₾ (18$)/сутки** комплект
4-6 дней подряд: **42₾/сутки** комплект
От 7 дней подряд: **35₾/сутки** комплект

**🎿 Комплект включает:**
1. Лыжи, палки, ботинки, шлем
2. Сноуборд, ботинки, шлем
3. Куртка, штаны, маска

**🧩 Дополнительные предметы:**
4. Лыжи + палки / сноуборд: **39₾/1 сутки**
5. Маска: **10₾/сутки**
6. Шлем: **10₾/сутки**
7. Перчатки: **10₾/сутки**
8. Защитные шорты: **10₾/сутки**
9. Куртка: **20₾/сутки**
10. Штаны: **20₾/сутки**"""


def rent_equipment_questions_text(lang):
    if lang == "english":
        return ("1. What equipment or clothing would you like to rent?\n"
                "2.	For how long? / For what dates?\n\n"
                "**Example:**\n"
                "1 3 5\n"
                "2 days / 16.01 - 18.01\n\n"
                "__To return to the menu, type 'menu' / 'cancel' / 'no'__")
    else:
        return ("1. Что вы хотите взять из снаряжения, одежды?\n"
                "2. На какой срок? / На какие даты?\n\n"
                "**Пример:**\n"
                "1 3 5\n"
                "2 суток / 16.01 - 18.01\n\n"
                "__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__")


def no_equipment_selected_error(lang):
    if lang == 'english':
        return ("Oops! You haven't selected any equipment yet. Please choose something before placing your order.\n"
                "**Example:**\n"
                "1 3 4\n"
                "3 days  16.01 - 19.01")
    else:
        return ("Ой! Вы еще не выбрали ни одно снаряжение или одежду. Пожалуйста, выберите что-нибудь."
                "**Пример:**\n"
                "3 суток 16.01 - 19.01")


def rent_equipment_error(lang):
    if lang == 'english':
        return "Error: You must choose at least one equipment"
    else:
        return "Ошибка: Вы должны выбрать хотя бы один снаряд"


def rent_equipment_confirmation_text(lang, selected_items, rental_period):

    equipment_text = get_equipment_order_text(selected_items, lang)

    if lang == "english":
        confirm_text = (f"**Confirm your booking by replying with “yes”/“ok”**\n"
                        f"After that, we will connect you with an operator.\n") if rental_period != 'None' else ""
        rp_text = rental_period if rental_period != 'None' else '**Please specify rental period!**'
        return (f"{confirm_text}"
                f"**You can still add equipment or clothing by writing below.**\n"
                f"To cancel the rental, type 'Cancel'.\n\n"
                f"🕒 {rp_text}\n———\n"
                f"{equipment_text}\n")
    else:
        rp_text = rental_period if rental_period != 'None' else '**Пожалуйста укажите период аренды!**'
        confirm_text = (f"**Подтвердите ваше бронирование, написав “да”/“ага”**\n"
                        f"После этого мы свяжем вас с оператором\n") if rental_period != 'None' else ""
        return (f"{confirm_text}"
                f"**Вы все ещё можете добавить снаряжение, одежду написав ниже**\n"
                f"Для отмены аренды напишите 'Отмена'\n\n"
                f"🕒 {rp_text}\n———\n"
                f"{equipment_text}\n")


def get_equipment_order_text(selected_items, lang='russian'):
    text = ''
    n = 1

    for item in selected_items:
        number = item['number']
        quantity = item['quantity']
        position_name = equipment_dict[lang][number]['name']

        for _ in range(quantity):
            text += f'{n}. {position_name}\n'
            n += 1

    return text


def new_equipment_booking_text(user, selected_items, rental_period):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    equipment_text = get_equipment_order_text(selected_items)

    return (f"🆕 Заявка на аренду снаряжения\n\n"
            f"👤 {user_mention}{username}\n"
            f"🕒 {rental_period}\n"
            f"{equipment_text}")


def equipment_booking_confirmed_text(lang):
    l_text = 'Link' if lang == "english" else 'Ссылка'
    link = f'[{l_text}](https://yandex.com/maps/-/CHEKYI5W)'

    if lang == "english":
        return ("**🎉 Your equipment booking is confirmed!**\n"
                "📍 New Gudauri, `42.469758, 44.491701`\n"
                f"Underground parking, under the outdoor pool ({link})\n"
                f"Behind the Gudauri Casino building (La suite)\n"
                "We will be waiting for you!\n"
                "**Please pay in cash (₾/$).**")
    else:
        return ("**🎉 Ваша бронирование снаряжения подтверждено!**\n"
                "📍 Нью-Гудаури, `42.469758, 44.491701`\n"
                f"Подземная парковка, под открытым бассейном ({link})\n"
                f"За зданием Gudauri Casino (La suite)\n"
                "Будем ждать вас!\n"
                "**Пожалуйста, оплатите наличными (₾/$).**")
# ======== Rent Equipment ========


# ======== Hire Instructor ========
def hire_instructor_info_text(lang):
    if lang == "english":
        return """
**🗻 Ski and snowboard lessons in Gudauri with a certified instructor**
For beginners and those who want to improve their skills.

**Cost of lessons:**
• From **115₾ (42$)** per hour, minimum 2 hours per lesson.
┌───────┐
    **👥 For Adults**
└───────┘
🕘 10:00 – 12:00 🕒
- **250₾ (89$)** 2h for 1 person
- **400₾ (149$)** 2h for a group of 2 people
- **500₾ (186$)** 2h for a group of 3 people

🕘 12:30 – 14:30 🕒
- **240₾ (85$)** 2h for 1 person
- **390₾ (146$)** 2h for a group of 2 people
- **490₾ (183$)** 2h for a group of 3 people

🕘 14:00 – 16:00 🕒
- **230₾ (83$)** 2h for 1 person
- **370₾ (138$)** 2h for a group of 2 people
- **470₾ (175$)** 2h for a group of 3 people
"""
    else:
        return """
**🗻 Обучение катанию в Гудаури на лыжах и сноуборде с сертифицированным инструктором**
Для новичков и тех, кто хочет повысить свой уровень.

**Стоимость занятий:**
• От **115₾ (42$)** за час, занятие от 2х часов.

🕘 9:10 – 11:10 🕒
- **250₾ (89$)** 2 часа 1 человек
- **400₾ (149$)** 2ч группа 2 человека
- **500₾ (186$)** 2ч группа 3 человека

🕘 11:30 – 13:30 🕒
- **240₾ (85$)** 2 часа 1 человек
- **390₾ (146$)** 2ч группа 2 человека
- **490₾ (183$)** 2ч группа 3 человека

🕘 14:00 – 16:00 🕒
- **230₾ (83$)** 2 часа 1 человек
- **370₾ (138$)** 2ч группа 2 человека
- **470₾ (175$)** 2ч группа 3 человека
"""


def hire_instructor_questions_text(lang):
    if lang == "english":
        return """
1. What dates should we book for you?
2. What time should the lesson start?
3. Skis or snowboard?
4. How many people?
5. Please specify the approximate age.

**Examples (write in a column format):**
January 8
10:10
Skis
1 child
10 years old

January 4
12:30
Snowboard
2 adults
25-50 years old

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """
1. На какие даты вас записать?
2. Время начала занятия?
3. Лыжи или сноуборд?
4. Сколько людей?
5. Укажите примерный возраст.

**Примеры (пишите в столбик):**
8 января
10 10
Лыжи
1 ребенок
10 лет

4 января
12 30
Сноуборд
2 взр
25-50 лет

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""


def instructor_booking_error(lang, state_data):
    texts = {
        'english': {
            'dates': 'What dates should we book for you?',
            'time': 'What time should the lesson start?',
            'equipment': 'Skis or snowboard?',
            'participants_count': 'How many people?',
            'age': 'Please specify the approximate age.',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'dates': 'На какие даты вас записать?',
            'time': 'Время начала занятия?',
            'equipment': 'Лыжи или сноуборд?',
            'participants_count': 'Сколько людей?',
            'age': 'Укажите примерный возраст.',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }

    }

    title = texts[lang]['error_text']
    text = f'{title}\n\n'
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f'{n}. {key_text}\n'
        n += 1

    return text


def tracks_info_text(lang):
    if lang == 'english':
        text = """**🗻 For New Gudauri**  
Start at the meadow next to the snowpark slope.  
1. Take the Goodaura gondola lift up.  
2. After exiting, move forward 10 meters — the meeting point will be right there.  
[Link to map](https://yandex.com.ge/maps/-/CDhy7C-e)

**🗻 For Upper Gudauri**  
If you’re in Upper Gudauri and taking the Shino lift:  
1. The meeting point will be at the snowpark meadow.  
2. Take the chairlift up and exit.  
3. Move forward 10 meters — the meeting point will be right there.  
[Link to map](https://yandex.com.ge/maps/-/CHAXnRlC)

**🗻 For Lower Gudauri (Marco Polo and nearby houses)**  
1. Take the chairlift to Pirveli (2155m).  
2. We will meet you at the top, you can hold your skis in your hands.  
[Link to map](https://yandex.com.ge/maps/-/CDhy7XLP)

**🗻 For Club 2100, Gudauri Lodge, Hills, Roshka, Gogi**  
If you're staying here and it's your first time on the slopes or you can’t ski,  
walk to the Pirveli slope — the meeting point will be right there.  
[Link to map](https://yandex.com.ge/maps/-/CDh5AIOw)"""
    else:
        text = """**🗻 Для Нью-Гудаури**
Если вы живете в Нью-Гудаури, начните с поляны рядом с трассой сноупарка.
1. Поднимитесь вверх на кабинке-гондоле по маршруту Goodaura.
2.После того как выйдете, двигайтесь вперед 10 метров — встреча будет прямо там.
[Ссылка на карту](https://yandex.com.ge/maps/-/CDhy7C-e)

**🗻 Для Верхнего Гудаури**
Если вы находитесь в Верхнем Гудаури и поднимаетесь на подъемнике Shino:
1. Встреча будет на поляне сноупарка.
2. Поднимитесь на кресельном подъемнике и выйдите.
3. Двигайтесь вперед 10 метров — встреча прямо там.
[Ссылка на карту](https://yandex.com.ge/maps/-/CHAXnRlC)

**🗻 Для Нижнего Гудаури (Marco Polo и соседние дома)**
1. Поднимитесь на кресельном подъемнике до Pirveli (2155 м).
2. Встретим вас на вершине, лыжи можно взять в руки.
[Ссылка на карту](https://yandex.com.ge/maps/-/CDhy7XLP)

**🗻 Для Club 2100, Gudauri Lodge, Hills, Roshka, Gogi**
Если вы живете в этих местах и это ваш первый раз на склонах, а также если вы не умеете кататься,
пройдите пешком до трассы Pirveli — встреча будет прямо там.
[Ссылка на карту](https://yandex.com.ge/maps/-/CDh5AIOw)"""

    return text


def instructor_booking_user_data_request_text(lang):
    if lang == "english":
        return """**Great! Now, please answer the following questions:**
1. What is your name?
2. What is your phone number?
3. Where do you live or will be staying?
This is needed for the instructor to know,
where it will be more convenient to start and meet you.

**Examples (please write in a column):**
Daniil
+995574253556
New Gudauri

Maria
+995 57 425 3556
Club 2100

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """"**Отлично! Осталось ответить на следующие вопросы:**
1. Как вас зовут?
2. Какой у вас номер телефона?
3. Где вы живете или будете жить?
Это нужно инструктору, чтобы знать,
где вам будет ближе начать и встретить вас

**Примеры (пишите в столбик):**
Даниил
+995574253556
Нью Гудаури

Мария
+995 57 425 3556
Club 2100

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""

    return text


def instructor_booking_user_data_request_error(lang, state_data):
    texts = {
        'english': {
            'name': 'What is your name?',
            'phone_number': 'What is your phone number?',
            'place': 'Where do you live or where will you stay?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'name': 'Как вас зовут?',
            'phone_number': 'Какой у вас номер телефона?',
            'place': 'Где вы живете или будете жить?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f"{title}\n\n"
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def new_instructor_booking_text(user, dates, start_time, equipment, participants_count, participants_type, age, name, phone_number, place):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    participants_type_text = get_participants_type_text(int(participants_count), participants_type)
    price = get_instructor_booking_price(start_time, participants_type, participants_count)
    finish_time = add_hours(start_time, 2)

    return (f"🆕 Заявка на инструктора\n"
            f"👤 {user_mention}{username}\n\n"
            f"📅 {dates} | {start_time} - {finish_time}\n"
            f"👥 {participants_type_text} | {age}\n"
            f"🎿 {equipment}\n"
            f"💵 {price}\n\n"
            f"👤 {name}\n"
            f"📞 {phone_number}\n"
            f"📍 {place}\n")


def get_participants_type_text(participants_count, participants_type, lang='russian'):
    if lang == "english":
        if participants_count == 1:
            return "1 adult" if participants_type == "adult" else "1 child"
        else:
            return f"{participants_count} adults" if participants_type == "adult" else f"{participants_count} children"
    else:  # Русский язык
        if participants_count == 1:
            return "1 взрослый" if participants_type == "adult" else "1 ребенок"
        else:
            return f"{participants_count} взрослых" if participants_type == "adult" else f"{participants_count} детей"


def get_instructor_booking_price(start_time, participants_type, people_count):
    price_list = {
        "adult": {
            "9:10": {1: 250, 2: 380, 3: 460},
            "11:30": {1: 240, 2: 360, 3: 440},
            "14:00": {1: 220, 2: 330, 3: 400},
        },
        "child": {
            "10:10": {1: 250, 2: 380},
            "12:30": {1: 250, 2: 380},
            "15:00": {1: 240, 2: 360},
        },
    }

    default_text = 'Ошибка расчета цены'

    if participants_type in price_list and start_time in price_list[participants_type]:
        price = price_list[participants_type].get(start_time, {}).get(people_count, default_text)
    else:
        price = default_text

    if price != default_text:
        return f"{price} лари"

    return default_text


def add_hours(time_str, hours):
    time_obj = datetime.strptime(time_str, "%H:%M")  # Преобразуем строку во время
    new_time_obj = time_obj + timedelta(hours=hours)  # Добавляем часы
    return new_time_obj.strftime("%H:%M")


def instructor_booking_confirmed_text(lang):
    if lang == "english":
        return ("**🎉 Your booking is confirmed!**\n\n"
                "**Please pay in cash (₾/$)**\n"
                "Your contact information has been shared with the instructor.")
    else:
        return ("**🎉 Ваша запись подтверждена!**\n\n"
                "**Пожалуйста, оплатите наличными (₾/$)**\n"
                "Ваш контакт передан инструктору\n")
# ======== Hire Instructor ========


# ======== Food & Coffee ========
def food_order_info_text(lang):
    if lang == "english":
        text = """**🍔 Food by New-Gudauri**

**🛍 Delivery within ~30-55 minutes**
🆓 Free delivery for orders over 60₾ (lari), otherwise 10₾

Make your selection, by number or letter:

**🥞 Breakfast**🕒 9.00 - 12.00 🕒
**1.** Syrniki + sour cream (3 pcs) — **10₾**
**2.** Pancakes + sour cream (3 pcs) — **10₾**
**3.** Rice-milk porridge + jam — **10₾**

**🍴Main dishes**
**4.** "FastTrack" sandwich (2 pcs) — **5₾**
**5.** Borscht soup (beef) — **10₾**
**6.** Kebab (Chicken) — **15₾**
**7.** "KurChiz" burger — **20₾**
**8.** "BifChiz" burger (beef) — **25₾**
**9.** Vegetable wok — **15₾**
**10.** Chicken wok — **15₾**

**🥗 Salads**
**11.** Georgian with walnuts — **10₾**
**12.** Caesar with chicken — **15₾**

**🥤 Drinks**
**13.** Water 0.7L — **2.5₾**
**14.** "Coca-Cola" water 0.5L — **5₾**
**15.** Quince juice 1L — **10₾**
**16.** Cherry juice 1L — **10₾**
**17.** 100% Apple juice 1L — **15₾**
**18.** 100% Grape juice 1L — **15₾**
**19.** Freshly squeezed pomegranate 0.5L — **20₾**
**20.** Freshly squeezed orange + mandarin 0.5L — **20₾**

**Order example:**
4 5 8 11 15"""
    else:
        text = """**🍔 Еда по New-Gudauri**
🕒 9.00 - 19.30 🕒
**🛍 Доставка в течении ~30-55 минут**
🆓 Бесплатно от 60₾(лари) иначе 10₾

Сделайте свой выбор, цифрами или буквами:

**🥞 Завтрак**🕒 9.00 - 12.00 🕒
**1.** Сырники + сметана (3 шт) — **10₾**
**2.** Блинчики + сметана (3 шт) — **10₾**
**3.** Каша рисо-молочная + варенье — **10₾**

**🍴Основные блюда**
**4.** Сэндвич “ФастТрэк” (2 шт) — **5₾**
**5.** Суп борщ (говядина) — **10₾**
**6.** Шаурма (куриная) — **15₾**
**7.** Бургер “КурЧиз” — **20₾**
**8.** Бургер “БифЧиз” (говяжий) — **25₾**
**9.** Вок с овощами — **15₾**
**10.** Вок с курицей — **15₾**

**🥗 Салаты**
**11.** Грузинский с грец. орехом — **10₾**
**12.** Цезарь с курицей — **15₾**

**🥤 Напитки**
**13.** Вода 0.7л — **2.5₾**
**14.** Вода “Кола” 0.5л — **5₾**
**15.** Сок айва 1л — **10₾**
**16.** Сок вишня 1л — **10₾**
**17.** Сок 100% яблоко 1л — **15₾**
**18.** Сок 100% виноград 1л — **15₾**
**19.** Свежевыжатый гранат 0.5л — **20₾**
**20.** Свежевыж. апельс.+мандарин 0.5л — **20₾**

**Пример заказа:**
4 5 8 11 15"""

    return text


def food_order_text(lang, selected_items, order_type):
    if lang == 'english':
        title = '📝 Your order'
        payment_info = ('**— You can still add more items to your order by writing below!**\n'
                        '— Pickup temporary unavailable\n\n'
                        # '— To change the order type, write: "`pickup`"/"`delivery`"\n\n'
                        '**Confirm your booking by replying with “yes” or “okay”**\n'
                        f"To cancel the order, type 'Cancel'")
    else:
        title = '📝 Ваш заказ'
        payment_info = ('**— Вы все еще можете дополнить заказ написав ниже!**\n'
                        '— Самовывоз временно недоступен\n\n'
                        # '— Что бы изменить тип заказа напишите: "`самовывоз`"/"`доставка`"\n\n'
                        '**Подтвердите ваше бронирование, написав “да”/“ага”**\n'
                        f"Для отмены заказа напишите 'отмена'")

    order_text = get_order_text(selected_items, order_type, lang)
    text = (f"**{title}:**\n"
            f"{order_text}\n\n"
            f"{payment_info}")

    return text


def get_order_text(selected_items, order_type, lang='russian'):
    if lang == 'english':
        total_text = 'Total'
        delivery_text = "Delivery"
        order_type_text = 'Order type: Delivery' if order_type == 'delivery' else 'Order type: Pickup'
    else:
        total_text = 'Итого'
        delivery_text = "Доставка"
        order_type_text = 'Тип заказа: Доставка' if order_type == 'delivery' else 'Тип заказа: Самовывоз'

    total_price = calculate_total_price(selected_items)
    text = ''

    n = 1
    for item in selected_items:
        number = item['number']
        quantity = item['quantity']
        position_name = food_coffee_dict[lang][number]['name']

        for _ in range(quantity):
            text += f'{n}. {position_name}\n'
            n += 1

    if total_price < 60 and order_type == 'delivery':
        text += f"{n}. {delivery_text} — **10₾**\n"
        total_price += 10

    text += (f"——————\n"
             f"🧾{total_text}: {total_price}₾\n"
             f"🛍{order_type_text}")

    return text


def calculate_total_price(selected_items):
    total_price = float()

    for item in selected_items:
        quantity = item['quantity']
        price = food_coffee_dict['russian'][item['number']]['price']
        total_price += quantity * price

    return total_price


def food_order_confirmed_text(lang, order_num, order_type):
    if lang == 'english':
        delivery_text = '📍 **Loft 2**, any entrance to the elevator, 2nd floor, **№238**' if order_type == 'pickup' else ''
        text = (f'**🛍️ Your order ({order_num}) is being prepared**\n'
                '⏳ In about **20-55 minutes** it will be ready for delivery!\n'
                f'{delivery_text}\n'
                '**The operator will contact you soon and confirm your order. Thank you!**\n'
                '')
    else:
        delivery_text = '📍 **Loft 2**, любой вход к лифту, 2 этаж, **№238**' if order_type == 'pickup' else ''
        text = (f'**🛍️ Ваш заказ ({order_num}) готовится**\n'
                '⏳ Примерно через **20-55 минут** он будет готов для доставки!\n'
                f'{delivery_text}\n'
                '**Оператор скоро свяжется с вами и подтвердит заказ, спасибо!**\n'
                f"Пожалуйста, оплатите наличными (₾/$)")

    return text


def new_food_order_text(user, selected_items, order_type, delivery_details=None):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    order_text = get_order_text(selected_items, order_type)

    text = (f"🆕 Заявка на еду\n\n"
            f"👤 {user_mention}{username}\n"
            f"{order_text}")

    if delivery_details:
        text += (f"\n\n**🛵 Доставка**\n"
                 f"1. Дом: {delivery_details['house_name']}\n"
                 f"2. Апартаменты: {delivery_details['apartment']}\n"
                 f"3. Номер телефона: {delivery_details['phone_number']}\n")

        return text


def no_food_selected_error(lang):
    if lang == 'english':
        return ("Oops! You haven't selected any food or coffee yet. Please choose something before placing your order.\n"
                "__Order example: 1 1 2 4__")
    else:
        return ("Ой! Вы еще не выбрали ни одно блюдо или кофе. Пожалуйста, выберите что-нибудь перед тем, как сделать заказ.\n"
                "__Пример заказа: 1 1 2 4__")


def food_order_invalid_error(lang):
    if lang == 'english':
        return "The item number is incorrect. Please use the format ‘1 2 3 4’, separating each selected item with a space."
    else:
        return "Номер товара указан некорректно. Пожалуйста, используйте формат '1 2 3 4', разделяя пробелами каждую выбранную позицию."


def food_order_delivery_details_text(lang):
    if lang == 'english':
        return ("1. What is your house name? Check the map.\n"
                "2. What is your apartment number?\n"
                "3. What is your phone number?")
    else:
        return ("1. Какой у вас дом? посмотрите карту\n"
                "2. Номер апартамента?\n"
                "3. Ваш номер телефона?")


def food_order_delivery_details_request_error(lang, state_data):
    texts = {
        'english': {
            'house_name': 'What is your house name? Check the map.',
            'apartment': 'What is your apartment number?',
            'phone_number': 'What is your phone number?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'house_name': 'Какой у вас дом? посмотрите карту',
            'apartment': 'Номер апартамента?',
            'phone_number': 'Ваш номер телефона?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f"{title}\n\n"
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def food_order_delivery_details_confirmation_text(lang, state_data):
    selected_items = state_data.get('selected_items')
    order_type = state_data.get('order_type')
    house_name = state_data.get('house_name')
    apartment = state_data.get('apartment')
    phone_number = state_data.get('phone_number')

    texts = {
        'english': {
            'title': '📝 Your order',
            'house_name': 'House name:',
            'apartment': 'Apartment:',
            'phone_number': 'Phone number:',
            'delivery': 'Delivery',
            'confirm': ('**Confirm your booking by replying with “yes” or “okay”**\n'
                        f"To cancel the order, type 'Cancel'")
        },
        'russian': {
            'title': '📝 Ваш заказ',
            'house_name': 'Дом:',
            'apartment': 'Апартаменты:',
            'phone_number': 'Номер телефона:',
            'delivery': 'Доставка',
            'confirm': ('**Подтвердите ваше бронирование, написав “да”/“ага”**\n'
                        f"Для отмены заказа напишите 'отмена'")
        }
    }

    order_text = get_order_text(selected_items, order_type, lang)
    lang_texts = texts[lang]

    text = (f"**{lang_texts['title']}**\n"
            f"{order_text}\n\n"
            f"**🛵 {lang_texts['delivery']}**\n"
            f"1. {lang_texts['house_name']} {house_name}\n"
            f"2. {lang_texts['apartment']} {apartment}\n"
            f"3. {lang_texts['phone_number']} {phone_number}\n\n"
            f"{lang_texts['confirm']}")

    return text


# ======== Food & Coffee =======


# ======== Massage =======
def massage_service_info_text(lang):
    if lang == "english":
        text = """**💆 Massage**

🕒 5:00 PM - 8:00 PM 🕒  
Relaxing                     ⏰ 1h — 110₾ / 1.5h — 160₾  
Classic                        ⏰ 1h — 130₾ / 1.5h — 180₾  
Sports                         ⏰ 1h — 150₾ / 1.5h — 220₾  
Balinese                      ⏰ 1h — 120₾ / 1.5h —  169₾  
Cupping Therapy   ⏰ 1h — 110₾ / 1.5h — 150₾
Back + legs                  ⏰ 1h — 110₾ / 1.5h — 150₾

1. What type of massage will it be?
2. Duration?

**Example:**
Classic
1.5 hours

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        text = """**💆Массаж**

🕒 17.00 - 20.00 🕒
Расслабляющий    1 час ⏰ 110₾ / 1.5⏰  160₾
Классический         1 час ⏰ 130₾ / 1.5⏰  180₾
Спортивный            1 час ⏰ 150₾ / 1.5⏰  220₾
Балийский                1 час ⏰ 120₾ / 1.5⏰  169₾
Банки (лечебный) 1 час ⏰ 110₾ / 1.5⏰  150₾
Спина + ноги            1 час ⏰ 110₾ / 1.5⏰  150₾

1. Какой будет вид массажа?
2. Длительность?

**Пример:**
Классический
1.5 часа

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""

    return text


def massage_type_request_text(lang):
    if lang == "english":
        return ("1. Choose a date?\n"
                "2. Time?\n\n"
                "**Example:**\n"
                "January 4\n"
                "11 00\n\n"
                "__To return to the menu, type 'menu' / 'cancel' / 'no'__")
    else:
        return ("1. Выберите дату?\n"
                "2. Время?\n\n"
                "**Пример:**\n"
                "4 января\n"
                "11 00\n\n"
                "__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__")


def booking_error(lang):
    if lang == 'english':
        return 'Oops! Something was filled in incorrectly, please try again'
    else:
        return 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова'


def massage_booking_confirmation_request_text(lang, date, time, massage_type, duration):
    date_str = utils.convert_date_to_str(date, lang)
    massage_str = massage_dict[lang][massage_type]
    if lang == "english":
        return (f"**Confirm your booking by replying 'yes'/'ok'**\n"
                f"After that, we will connect you with an operator\n"
                "To cancel your booking, type 'cancel'.\n\n"
                f"📅 {date_str} {time}\n"
                f"💆 {massage_str} {duration}h")
    else:
        return (f"**Подтвердите вашу запись, написав “да”/“ага”**\n"
                f"После этого мы свяжем вас с оператором\n"
                "Для отмены записи напишите 'отмена'.\n\n"
                f"📅 {date_str} {time}\n"
                f"💆 {massage_str} {duration}ч")


def massage_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                "**Please pay in cash (₾/$)**"
                f"Your contact details have been forwarded to the operator,"
                f"who will contact you as soon as they are available.\n")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Ваш контакт передан оператором,\n"
                f"он свяжется с вами, как освободится")


def massage_booking_text(user, date, time, massage_type, duration):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)
    massage_str = massage_dict['russian'][massage_type]

    return (f"🆕 Заявка на массаж\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str} {time}\n"
            f"💆 {massage_str} {duration}ч")


def invalid_massage_booking_time_error(lang):
    if lang == "english":
        return "Invalid booking time. Please choose a time that is within 9:00 - 20:00"
    else:
        return "Неверное время бронирования. Пожалуйста, выберите время, которое находится в пределах 9:00 - 20:00"


def unavailable_time_error(lang):
    if lang == "english":
        return "This time slot is **unavailable**. Please choose a different time"
    else:
        return "Это время **занято**, пожалуйста, укажите другое время."
# ======== Massage =======


# ======== Paragliding =======
def paragliding_plan_info_text(lang):
    texts = {
        "english": "**🪂 Paragliding Flight**\n\n"
                   "Choose a tandem with a pilot:\n"
                   "1. Standard 15-20 minutes 350₾\n"
                   "2. Levitation Pro 35-40 minutes 500₾\n\n"
                   "__To return to the menu, type 'menu' / 'cancel' / 'no'__",

        "russian": "**🪂 Полет на параплане**\n\n"
                   "Выберите тандем с пилотом:\n"
                   "1. Стандартный 15-20 минут 350₾\n"
                   "2. Левитация Про 35-40 минут 500₾\n\n"
                   "__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__",
    }

    return texts[lang]


def user_details_collecting_text(lang):
    texts = {
        "english": """
1. What date should we book you for?
2. Time?
3. What is your name?
4. What is your phone number?

**This is needed for the pilot to contact you.**

Example (please write in separate lines):
January 4
10:00
Sasha
+9955513437122

__To return to the menu, type 'menu' / 'cancel' / 'no'__""",
        "russian": """
1. На какую дату вас записать?
2. Время?
3. Как вас зовут?
4. Какой у вас номер телефона?

**Это нужно пилоту, чтобы связаться с вами.**

Пример (пишите в столбик):
4 января
10.00
Саша
+9955513437122

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""
    }

    return texts[lang]


def user_details_collecting_error(lang, state_data):
    texts = {
        'english': {
            'date': 'What date should we book you for?',
            'time': 'Time? 10:00 - 17:00',
            'name': 'What is your name?',
            'phone_number': 'What is your phone number?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'date': 'На какую дату вас записать?',
            'time': 'Время? 10.00 - 17.00',
            'name': 'Как вас зовут?',
            'phone_number': 'Какой у вас номер телефона?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f"{title}\n\n"
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        if key == 'date' and value != 'None':
            value = utils.convert_date_to_str(value, lang)

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def booking_confirmation_request_text(lang):
    if lang == "english":
        return (f"**Confirm your booking by replying 'yes'/'ok'**\n"
                f"After that, we will connect you with an operator\n"
                "To cancel your booking, type 'cancel'.")
    else:
        return (f"**Подтвердите вашу запись, написав “да”/“ага”**\n"
                f"После этого мы свяжем вас с оператором\n"
                "Для отмены записи напишите 'отмена'.")


def paragliding_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"The contact details have been sent to the pilot. They will contact you to confirm the details.\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Контакты отправлены пилоту, он свяжется с вами и уточнит детали.\n"
                f"Пожалуйста, оплатите наличными (₾/$)")


def paragliding_booking_text(user, date, time, name, phone_number, selected_plan):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)

    return (f"🆕 Заявка на параплан\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str} {time}\n"
            f"🪂 {selected_plan}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")


def invalid_paragliding_booking_time_error(lang):
    if lang == "english":
        return "Invalid booking time. Please choose a time that is within 10:00 - 17:00"
    else:
        return "Неверное время бронирования. Пожалуйста, выберите время, которое находится в пределах 10:00 - 17:00"
# ======== Paragliding =======


# ======== Snowbike =======
def snowbike_tour_info_text(lang):
    texts = {
        "english": "**🏍 Snowmobile Tour**\n\n"
                   "Choose your tour (you drive):\n"
                   "1. 1 person (4 km loop) - 150₾\n"
                   "2. 2 people (4 km loop) - 250₾\n\n"
                   "**⏰ Before 10:00 or after 17:00:**\n"
                   "1 person 30 minutes - 200₾\n\n"
                   "__To return to the menu, type 'menu' / 'cancel' / 'no'__",

        "russian": "**🏍Тур на снегоходе**\n\n"
                   "Выберите тур (вы за рулем):\n"
                   "1. 1 человек (4 км круг) - 150₾\n"
                   "2. 2 человека (4 км круг) - 250₾\n\n"
                   "**⏰ До 10:00 или после 17:00:**\n"
                   "1 чел 30 минут - 200₾\n\n"
                   "__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__",
    }

    return texts[lang]


def snowbike_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"Contacts have been sent, please wait, we will contact you and clarify the details.\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Контакты отправлены, ожидайте, мы свяжемся с вами и уточним детали.\n"
                f"Пожалуйста, оплатите наличными (₾/$)")


def snowbike_booking_text(user, date, time, name, phone_number, selected_tour):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)

    return (f"🆕 Заявка: Тур на снегоходе\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str} {time}\n"
            f"🏍 {selected_tour}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")
# ======== Snowbike =======


# ======== Currency Exchange =======
def currency_exchange_info_text(lang):
    current_rate = utils.get_currency_rate()

    if lang == "english":
        text = f"""**🗻 We are located in New Gudauri**
💱 Exchange only from $100 to GEL ₾
💵 Today's rate: $1 = ₾{current_rate}
💶 Today's rate: €1 = ₾3

1. Specify the amount in $ for exchange
2. Date
3. Time of visit? ([Map link](https://g.co/kgs/LxLVUAf))
3. What is your name?
4. What is your phone number?

**Example (write in a column):**
400
January 4
12:56
Yaroslav
+9955513437122

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        text = f"""**🗻 Мы находимся в Нью-Гудаури**
💱 Обмен только от 100$ на лари ₾
💵 Курс сегодня $1 = ₾{current_rate}
💶 Курс сегодня €1 = ₾3

1. Укажите сумму $ для обмена
2. Дата
3. Время визита? ([Ссылка на карту](https://g.co/kgs/LxLVUAf))
3. Как вас зовут?
4. Какой у вас номер телефона?

**Пример (пишите в столбик):**
400
4 января
12 56
Ярослав
+9955513437122

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""

    return text


def exchange_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"Your contact details have been sent to the operator, who will contact you before the transaction.")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Контакты отправлены, операционисту, до операции он свяжется с вами.")


def exchange_booking_error(lang, state_data):
    texts = {
        'english': {
            'amount': 'Specify the amount in $ for exchange',
            'date': 'What date should we book you for?',
            'time': 'Time?',
            'name': 'What is your name?',
            'phone_number': 'What is your phone number?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'amount': 'Укажите сумму $ для обмена',
            'date': 'На какую дату вас записать?',
            'time': 'Время?',
            'name': 'Как вас зовут?',
            'phone_number': 'Какой у вас номер телефона?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f'{title}\n\n'
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f'{n}. {key_text}\n'
        n += 1

    return text


def exchange_booking_text(user, amount, date, time, name, phone_number):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)

    return (f"🆕 Заявка: Обмен валюты\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str} {time}\n\n"
            f"💵 ${amount}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")
# ======== Currency Exchange =======


# ======== Ski Service =======
def ski_service_info_text(lang):
    if lang == 'english':
        return """**🛠Equipment Repair**
🕒 9:00 AM - 6:30 PM 🕒

Choose a service:

1. Edge sharpening + waxing - 30₾
2. Sliding surface repair - 40₾

We are located at:
📍 New Gudauri, 42.469758, 44.491701  
Underground parking, beneath the open pool ([Link](https://yandex.com/maps/-/CHEKYI5W))

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """**🛠Ремонт снаряжения**
🕒 9.00 - 18.30 🕒

Выберите услугу

1. Заточка кантов + парафин - 30₾
2. Ремонт скользящей поверхности - 40₾

Мы находимся:
📍 Нью-Гудаури, 42.469758, 44.491701
Подземная парковка, под открытым бассейном ([Ссылка](https://yandex.com/maps/-/CHEKYI5W))

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""


def ski_service_booking_info_text(lang):
    if lang == "english":
        return "Choose a service for booking:"
    else:
        return """
1. Укажите дату
2. Время визита
3. Как вас зовут?

Пример (пишите в столбик):
4 января
17 00
Ярослав"""


def invalid_ski_service_booking_time_error(lang):
    if lang == "english":
        return "Invalid booking time. Please choose a time that is within 10:00 - 17:00"
    else:
        return "Неверное время бронирования. Пожалуйста, выберите время, которое находится в пределах 10:00 - 17:00"


def ski_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Пожалуйста, оплатите наличными (₾/$)")


def ski_booking_text(user, date, time, name, phone_number, selected_service):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)

    return (f"🆕 Заявка: Ремонт Снаряжения\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str} {time}\n\n"
            f"🎿 {selected_service}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")
# ======== Ski Service =======


# ======== Cleaning =======
def cleaning_service_info_text(lang):
    if lang == "english":
        return """
**🧹 Cleaning Services in New Gudauri**

Choose a service:

1. Studio - 100₾  
2. Studio (Deep Cleaning) - 200₾  
3. Apartment over 30m² - 150₾  
4. Apartment over 30m² (Deep Cleaning) - 250₾  
5. Apartment over 60m² - 200₾  
6. Apartment over 60m² (Deep Cleaning) - 300₾  

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """
**🧹 Уборка по Нью-Гудаури**

Выберите услугу:

1. Студия - 100₾
2. Студия генеральная - 200₾
3. Квартира больше 30м2 - 150₾
4. Квартира > 30м2 генеральная - 250₾
5. Квартира больше 60м2 - 200₾
6. Квартира > 60м2 генеральная - 300₾

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""


def cleaning_details_collecting_text(lang):
    if lang == 'english':
        return """
1. What date should we book you for?
2. Building/Block?
3. Apartment number?
4. What is your name?
5. What is your phone number?

**Example (write in a column):**
January 4
F4
323
Sasha
+9955513437122

"__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """
1. На какую дату вас записать?
2. Дом/корпус?
3. Номер апартаментов?
4. Как вас зовут?
5. Какой у вас номер телефона?

**Пример (пишите в столбик):**
4 января
F4
323
Саша
+9955513437122

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""


def cleaning_details_collecting_error(lang, state_data):
    texts = {
        'english': {
            'date': 'What date should we book you for?',
            'building': 'Building/Block?',
            'apartment': 'Apartment number?',
            'name': 'What is your name?',
            'phone_number': 'What is your phone number?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'date': 'На какую дату вас записать?',
            'building': '2. Дом/корпус?',
            'apartment': '3. Номер апартаментов?',
            'name': 'Как вас зовут?',
            'phone_number': 'Какой у вас номер телефона?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f"{title}\n\n"
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        if key == 'date' and value != 'None':
            value = utils.convert_date_to_str(value, lang)

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def cleaning_booking_text(user, date, building, apartment, name, phone_number, selected_service):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    date_str = utils.convert_date_to_str(date)

    return (f"🆕 Заявка: Уборка\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {date_str}\n\n"
            f"🧹 {selected_service}\n"
            f"🏘 {building} {apartment}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")


def cleaning_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"Пожалуйста, оплатите наличными (₾/$)")

# ======== Cleaning =======


# ======== Rent Flat =======
def rent_flat_service_info_text(lang):
    if lang == "english":
        return """**🏠 Apartments in New Gudauri**
Leave a request:

1. What is your name?  
2. What is your phone number?  

**Example (write in separate lines):**  
Sasha  
+9955513437122"""
    else:
        return """**🏠 Апартаменты в Нью-Гудаури**
Оставьте заявку:

1. Как вас зовут?
2. Какой у вас номер телефона?

**Пример (пишите в столбик):**
Саша
+9955513437122"""


def rent_flat_booking_text(user, name, phone_number):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    return (f"🆕 Заявка: Аренда квартиры\n\n"
            f"👤 {user_mention}{username}\n"
            f"🧍 {name}\n"
            f"📞 {phone_number}")


def rent_flat_booking_confirmed_text(lang):
    if lang == "english":
        return (
            f"🎉Contacts have been sent. Please wait, we will contact you to find suitable apartments in New Gudauri.\n"
            f"**Please pay in cash (₾/$)**")
    else:
        return (f"🎉Контакты отправлены, ожидайте, мы свяжемся с вами и подберем вам апартаменты в Нью-Гудаури.\n"
                f"**Пожалуйста, оплатите наличными (₾/$)**")
# ======== Rent Flat =======


# ======== Transfer =======
def transfer_service_info_text(lang):
    if lang == "english":
        return """
1. Select the route number
   1. Gudauri - Tbilisi Airport 🚕 250₾
   2. Gudauri - Tbilisi               🚕 200₾
   3. Gudauri - Vladikavkaz    🚕 10,000 RUB
   4. Tbilisi Airport - Gudauri 🚕 250₾
   5. Tbilisi - Gudauri               🚕 200₾
   6. Vladikavkaz - Gudauri     🚕 10,000 RUB
   7. Any other route

2. Number of passengers?
3. How many equipment bags do you have?
4. How many luggage bags?
5. What time should the car arrive?
6. Your phone number?

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        return """
1. Выберите цифру маршрута
   1. Гудаури - Тбилиси аэропорт 🚕 250₾
   2. Гудаури - Тбилиси                     🚕 200₾
   3. Гудаури - Владикавказ             🚕 10.000 руб
   4. Тбилиси аэропорт - Гудаури 🚕 250₾
   5. Тбилиси - Гудаури                     🚕 200₾
   6. Владикавказ - Гудаури             🚕 10.000 руб
   7. Любой другой

2. Количество человек?
3. Сколько у вас сумок экипировки?
4. Сколько сумок багажа?
5. Время подачи машины?
6. Ваш номер телефона?

__Для возврата в меню напишите 'меню' / 'отмена' / 'нет'__"""


def transfer_details_collecting_error(lang, state_data):
    texts = {
        'english': {
            'route_number': 'Route number?',
            'people_count': 'Number of passengers?',
            'equipment_bags': 'How many equipment bags do you have?',
            'luggage_bags': 'How many luggage bags?',
            'car_ready_time': 'What time should the car arrive?',
            'phone_number': 'Your phone number?',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'route_number': 'Цифра маршрута?',
            'people_count': 'Количество человек?',
            'equipment_bags': 'Сколько у вас сумок экипировки?',
            'luggage_bags': 'Сколько сумок багажа?',
            'car_ready_time': 'Время подачи машины?',
            'phone_number': 'Ваш номер телефона?',
            'error_text': 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:'
        }
    }

    title = texts[lang]['error_text']
    text = f"{title}\n\n"
    n = 1
    for key, value in state_data.items():
        if key not in texts[lang]:
            continue

        if key == 'date' and value != 'None':
            value = utils.convert_date_to_str(value, lang)

        key_text = str(value) + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def transfer_booking_text(user, route_number, people_count, equipment_bags, luggage_bags, car_ready_time, phone_number):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    route_name = transfer_price_dict['russian'].get(route_number, {}).get('name', 'Неизвестный маршрут')
    route_price = transfer_price_dict['russian'].get(route_number, {}).get('price', 0)
    currency = transfer_price_dict['russian'].get(route_number, {}).get('currency', '')
    if not route_price:
        route_price = 'Неизвестно'

    return (f"🆕 Заявка: Трансфер\n\n"
            f"👤 {user_mention}{username}\n"
            f"📍 {route_name}\n"
            f"💵 {route_price} {currency}\n\n"
            f"🧍 Кол-во человек: {people_count}\n"
            f"🎿 Экипировка: {equipment_bags}\n"
            f"🎒 Багаж: {luggage_bags}\n"
            f"🕒 Время подачи: {car_ready_time}\n"
            f"📞 {phone_number}")


def transfer_booking_confirmed_text(lang):
    if lang == "english":
        return (
            f"🎉Contacts have been sent. Please wait, we will contact you to find suitable transfer.\n"
            f"**Please pay in cash (₾/$)**")
    else:
        return (f"🎉Контакты отправлены, ожидайте, мы свяжемся с вами и подберем вам трансфер.\n"
                f"**Пожалуйста, оплатите наличными (₾/$)**")

# ======== Utils =======

# ======== Transfer =======


# ======== Utils =======
def has_invalid_items(selected_items, items_dict):
    selected_item_ids = [item['number'] for item in selected_items]
    return any(_id not in items_dict['english'].keys() for _id in selected_item_ids)
# ======== Utils =======


# ======== Templates ========
def service_unavailable_error(lang):
    if lang == "english":
        return "🏗 This service is unavailable"
    else:
        return "🏗 Этот сервис временно недоступен"


service_types = [
    "rent_equipment", "instructor", "food_coffee", "massage", "transfer", "paragliding",
    "snowbike_tour", "exchange", "ski_service", "photo_video", "cleaning", "rent_flat", "undefined"
]


massage_dict = {
    "english": {
        "relaxing": "Relaxing",
        "classic": "Classic",
        "sports": "Sports",
        "therapeutic_session": "Therapeutic Session",
        "balinese": "Balinese",
        "anti_cellulite": "Anti-cellulite",
        "back_and_legs": "Back + legs",
    },
    "russian": {
        "relaxing": "Расслабляющий",
        "classic": "Классический",
        "sports": "Спортивный",
        "therapeutic_session": "Лечебный",
        "balinese": "Балийский массаж",
        "anti_cellulite": "Антицеллюлитный",
        "back_and_legs": "Спина + ноги",
    }
}


food_coffee_dict = {
    "english": {
        1: {"name": "Syrniki with sour cream (3 pcs) — **10₾**", "price": 10},
        2: {"name": "Pancakes with sour cream (3 pcs) — **10₾**", "price": 10},
        3: {"name": "Rice-milk porridge + jam — **10₾**", "price": 10},
        4: {"name": "“FastTrack” Sandwich (2 pcs) — **5₾**", "price": 5},
        5: {"name": "Borscht soup (beef) — **10₾**", "price": 10},
        6: {"name": "Kebab (chicken) — **15₾**", "price": 15},
        7: {"name": "“KurCheese” Burger — **20₾**", "price": 20},
        8: {"name": "“BeefCheese” Burger (beef) — **25₾**", "price": 25},
        9: {"name": "Vegetable Wok — **15₾**", "price": 15},
        10: {"name": "Chicken Wok — **20₾**", "price": 20},
        11: {"name": "Georgian with walnuts — **10₾**", "price": 10},
        12: {"name": "Caesar with chicken — **15₾**", "price": 15},
        13: {"name": "Water 0.7 L — **2.5₾**", "price": 2.5},
        14: {"name": "Cola 0.5 L — **5₾**", "price": 5},
        15: {"name": "Quince juice 1L — **10₾**", "price": 10},
        16: {"name": "Cherry juice 1L — 10₾", "price": 10},
        17: {"name": "100% Apple juice 1L — 15₾", "price": 15},
        18: {"name": "100% Grape juice 1L — **15₾**", "price": 15},
        19: {"name": "Freshly squeezed pomegranate 0.5L — **20₾**", "price": 20},
        20: {"name": "Freshly squeezed orange + mandarin 0.5L — **20₾**", "price": 20},
    },
    "russian": {
        1: {"name": "Сырники с сметаной (3 шт) — **10₾**", "price": 10},
        2: {"name": "Блинчики с сметаной (3 шт) — **10₾**", "price": 10},
        3: {"name": "Каша рисо-молочная + варенье — **10₾**", "price": 10},
        4: {"name": "Сэндвич “ФастТрэк” (2 шт) — **5₾**", "price": 5},
        5: {"name": "Суп борщ (говядина) — **10₾**", "price": 10},
        6: {"name": "Шаурма (куриная) — **15₾**", "price": 15},
        7: {"name": "Бургер “КурЧиз” — **20₾**", "price": 20},
        8: {"name": "Бургер “БифЧиз” (говяжий) — **25₾**", "price": 25},
        9: {"name": "Вок с овощами — **15₾**", "price": 15},
        10: {"name": "Вок с курицей — **20₾**", "price": 20},
        11: {"name": "Грузинский с грец. орехом — **10₾**", "price": 10},
        12: {"name": "Цезарь с курицей — **15₾**", "price": 15},
        13: {"name": "Вода 0.7л — **2.5₾**", "price": 2.5},
        14: {"name": "“Кола” 0.5л — **5₾**", "price": 5},
        15: {"name": "Сок айва 1л — **10₾**", "price": 10},
        16: {"name": "Сок вишня 1л — 10₾", "price": 10},
        17: {"name": "Сок 100% яблоко 1л — 15₾", "price": 15},
        18: {"name": "Сок 100% виноград 1л — **15₾**", "price": 15},
        19: {"name": "Свежевыжатый гранат 0.5л — **20₾**", "price": 20},
        20: {"name": "Свежевыж. апельс.+мандарин 0.5л — **20₾**", "price": 20},
    }
}


equipment_dict = {
    "english": {
        1: {"name": "Ski set: Skis, poles, boots, helmet", "price": 5},
        2: {"name": "Snowboard set: Snowboard, boots, helmet", "price": 15},
        3: {"name": "Clothes set: Jacket, pants, goggles", "price": 10},
        4: {"name": "Skis + poles / snowboard", "price": 3},
        5: {"name": "Goggles", "price": 12},
        6: {"name": "Helmet", "price": 10},
        7: {"name": "Gloves", "price": 5},
        8: {"name": "Protective shorts", "price": 18},
        9: {"name": "Jacket", "price": 10},
        10: {"name": "Pants"}
    },
    "russian": {
        1: {"name": "Комплект лыж: Лыжи, палки, ботинки, шлем", "price": 5},
        2: {"name": "Комплект сноуборда: Сноуборд, ботинки, шлем", "price": 15},
        3: {"name": "Комплект одежды: Куртка, штаны, маска", "price": 10},
        4: {"name": "Лыжи + палки / сноуборд", "price": 3},
        5: {"name": "Маска", "price": 8},
        6: {"name": "Шлем", "price": 12},
        7: {"name": "Перчатки", "price": 10},
        8: {"name": "Защитные шорты", "price": 5},
        9: {"name": "Куртка", "price": 18},
        10: {"name": "Штаны", "price": 10},
    }
}


transfer_price_dict = {
    "english": {
        1: {"name": "Gudauri - Tbilisi Airport", "price": 250, 'currency': 'GEL'},
        2: {"name": "Gudauri - Tbilisi", "price": 200, 'currency': 'GEL'},
        3: {"name": "Gudauri - Vladikavkaz", "price": 10000, 'currency': 'RUB'},
        4: {"name": "Tbilisi Airport - Gudauri", "price": 250, 'currency': 'GEL'},
        5: {"name": "Tbilisi - Gudauri", "price": 200, 'currency': 'GEL'},
        6: {"name": "Vladikavkaz - Gudauri", "price": 10000, 'currency': 'RUB'},
        7: {"name": "Any other route", "price": None, 'currency': ''},
    },
    "russian": {
        1: {"name": "Гудаури - Тбилиси аэропорт", "price": 250, 'currency': 'GEL'},
        2: {"name": "Гудаури - Тбилиси", "price": 200, 'currency': 'GEL'},
        3: {"name": "Гудаури - Владикавказ", "price": 10000, 'currency': 'RUB'},
        4: {"name": "Тбилиси аэропорт - Гудаури", "price": 250, 'currency': 'GEL'},
        5: {"name": "Тбилиси - Гудаури", "price": 200, 'currency': 'GEL'},
        6: {"name": "Владикавказ - Гудаури", "price": 10000, 'currency': 'RUB'},
        7: {"name": "Любой другой", "price": None, 'currency': ''},
    }
}

# ======== Templates ========
