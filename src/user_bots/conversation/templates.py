from src.bot import utils


def select_language_text():
    return ("Цифрой/словом выберите язык\n"
            "Write number/word to choose language\n"
            "1 `Русский`\n"
            "2 `English`\n")


def select_language_error():
    return ("Пожалуйста попробуйте еще раз\n"
            "Please try again")


def all_services_text(lang):
    if lang == "english":
        text = """Write number/word in English, what do you want?

1. 🎿Rent Ski & Board 
2. ⛷Instructor    
3. 🍔Food & Coffee
4. 💆Massage                
5. 🚕Transfer & Taxi
6. 🪂Paragliding
7. 🏍Snowbike tour     
8. 💵Exchange       
9. 🛠Ski-service
11. 📹 Photo/Video  
12. 🧹Cleaning           
13. 🏠RentFlat

Ski-lift Open/Closed 🟢🔴 
Road status 🟢🔴
[Check](https://t.me/ASG_Status)
"""
    else:
        text = """Здравствуйте, напишите цифру/слово на русском

1. 🎿Прокат лыж & Сноубордов
2. ⛷Инструктор    
3. 🍔Еда & Кофе
4. 💆Массаж
5. 🚕Трансфер & Такси
6. 🪂Полет на параплане
7. 🏍Тур на снегоходе
8. 💵Обмен валют       
9. 🛠Ремонт снаряжения
11. 📹Фото & Видео  
12. 🧹Уборка           
13. 🏠Аренда Квартир

Статус подъемников 🟢🔴
Статус авто дорог из-за снега 🟢🔴
[Проверить](https://t.me/ASG_Status)
"""

    return text


def service_info_text(lang):
    if lang == "english":
        return """From 9:00 AM to 6:00 PM
New Gudauri
Suites Building
Enter through any door
Go to floor -1 (take the elevator)
Exit the elevator, go straight, and then right (follow the signs)
to the rental @AllServiceGudauri"""
    else:
        return """С 9.00 до 18.00
Нью-Гудаури
Здание Suites
Вход с любой двери во внутрь
-1 этаж, обязательно спуститься на лифте 
Из лифта вперед (и направо дальше по указателям)
к прокату @AllServiceGudauri"""


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
• Skis, poles, boots, helmet
• Snowboard, boots, helmet
• Jacket, pants, goggles

**Additional items:**
• Skis + poles / snowboard: **39₾/day**
• Goggles: **10₾/day**
• Helmet: **10₾/day**
• Gloves: **10₾/day**
• Protective shorts: **10₾/day**
• Jacket: **20₾/day**
• Pants: **20₾/day**"""
    else:
        return """
**🏂 Прокат @AllServiceGudauri**
🕒 9.00 - 18.30 🕒
1-3 дня подряд: **47,5₾ (18$)/сутки** комплект
4-6 дней подряд: **42₾/сутки** комплект
От 7 дней подряд: **35₾/сутки** комплект

**🎿 Комплект включает:**
• Лыжи, палки, ботинки, шлем
• Сноуборд, ботинки, шлем
• Куртка, штаны, маска

**🧩 Дополнительные предметы:**
• Лыжи + палки / сноуборд: **39₾/1 сутки**
• Маска: **10₾/сутки**
• Шлем: **10₾/сутки**
• Перчатки: **10₾/сутки**
• Защитные шорты: **10₾/сутки**
• Куртка: **20₾/сутки**
• Штаны: **20₾/сутки**"""


def rent_equipment_questions_text(lang):
    if lang == "english":
        return "What equipment or clothing would you like to rent?"
    else:
        return "Что вы хотите взять из снаряжения, одежды?"


def rent_equipment_error(lang):
    if lang == 'english':
        return "Error: You must choose at least one equipment"
    else:
        return "Ошибка: Вы должны выбрать хотя бы один снаряд"


def rent_equipment_confirmation_text(lang, user_answers):
    user_list = ''
    for n, answer in enumerate(user_answers, start=1):
        user_list += f"{n}. {answer}\n"

    if lang == "english":
        return (f"**Confirm your booking by replying with “yes”/“ok”**\n"
                f"After that, we will connect you with an operator.\n"
                f"**You can also add equipment or clothing by writing below.**\n"
                f"To cancel the rental, type 'Cancel'.\n\n"
                f"{user_list}")
    else:
        return (f"**Подтвердите ваше бронирование, написав “да”/“ага”**\n"
                f"После этого мы свяжем вас с оператором\n"
                f"**Вы также можете добавить снаряжение, одежду написав ниже**\n"
                f"Для отмены аренды напишите 'Отмена'\n\n"
                f"{user_list}")


def new_equipment_booking_text(user, user_answers):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    user_list = ''
    for n, answer in enumerate(user_answers, start=1):
        user_list += f"{n}. {answer}\n"

    return (f"🆕 Заявка на аренду снаряжения\n\n"
            f"👤 {user_mention}{username}\n"
            f"{user_list}")


def equipment_booking_confirmed_text(lang):
    if lang == "english":
        return ("**🎉 Your equipment rental is confirmed!**\n"
                "New Gudauri, the building closest to the lift.\n"
                "Use any of the 3 entrances, go to the elevator, floor -1.\n"
                "We’ll be waiting for you!")
    else:
        return ("**🎉 Ваша бронирование снаряжения подтверждено!**\n"
                "Нью-Гудаури, дом ближний к подъемнику"
                "Любой вход из 3х, проходите к лифту, -1 этаж"
                "Будем ждать вас!")
# ======== Rent Equipment ========


# ======== Hire Instructor ========
def hire_instructor_info_text(lang):
    if lang == "english":
        return """**🗻 Ski and Snowboard Lessons in Gudauri with a Certified Instructor**
For beginners and those looking to improve their skills.

**Lesson Prices:**
• Starting from 105₾ (40$) per hour for a minimum of 2 hours.

┌───────┐
    **👥 For Adults**
└───────┘
🕘 10:10 – 12:10 🕒
- **250₾ (89$)** 2h for 1 person
- **360₾ (128$)** 2h for a group of 2 people
- **440₾ (157$)** 2h for a group of 3 people

🕘 12:30 – 14:30 🕒
- **230₾ (82$)** 2h for 1 person
- **350₾ (124$)** 2h for a group of 2 people
- **420₾ (149$)** 2h for a group of 3 people

🕘 15:00 – 17:00 🕒
- **210₾ (75$)** 2h for 1 person
- **310₾ (110$)** 2h for a group of 2 people
- **400₾ (142$)** 2h for a group of 3 people

┌────────┐
    **👨‍👩‍👦 For Children**
└────────┘
**Under 6 years old**: 1h lessons, individual only
**Children 7+**: 2h lessons

🕘 10:10 – 12:10 🕒
- **250₾ (89$)** 2h for 1 child
- **350₾ (124$)** 2h for a group of 2 children

🕘 12:30 – 14:30 🕒
- **240₾ (86$)** 2h for 1 child
- **350₾ (124$)** 2h for a group of 2 children

🕘 15:00 – 17:00 🕒
- **240₾ (86$)** 2h for 1 child
- **350₾ (124$)** 2h for a group of 2 children
"""
    else:
        return """**🗻 Обучение катанию в Гудаури на лыжах и сноуборде с сертифицированным инструктором**
Для новичков и тех, кто хочет повысить свой уровень.

**Стоимость занятий:**
• От 105₾ (40$) за час при минимальной продолжительности в 2 часа.

┌─────────┐
    **👥 Для взрослых**
└─────────┘
🕘 10:10 – 12:10 🕒
- **250₾ (89$)** 2 часа 1 человек
- **360₾ (128$)** 2ч группа 2 человека
- **440₾ (157$)** 2ч группа 3 человека

🕘 12:30 – 14:30 🕒
- **230₾ (82$)** 2 часа 1 человек
- **350₾ (124$)** 2ч группа 2 человека
- **420₾ (149$)** 2ч группа 3 человека

🕘 15:00 – 17:00 🕒
- **210₾ (75$)** 2 часа 1 человек
- **310₾ (110$)** 2ч группа 2 человека
- **400₾ (142$)** 2ч группа 3 человека

┌───────┐
    **👨‍👩‍👦 Для детей**
└───────┘ 
**До 6 лет** занимаются 1ч и только индивидуально
**Дети 7+** занимаются 2ч
🕘 10:10 – 12:10 🕒
- **250₾ (89$)** 2ч за 1 ребенка
- **350₾ (124$)** 2ч за группу из 2 детей

🕘 12:30 – 14:30 🕒
- **240₾ (86$)** 2ч за 1 ребенка
- **350₾ (124$)** 2ч за группу из 2 детей

🕘 15:00 – 17:00 🕒
- **240₾ (86$)** 2ч за 1 ребенка
- **350₾ (124$)** 2ч за группу из 2 детей
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
25-50 years old"""
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
25-50 лет"""


def instructor_booking_error(lang, state_data):
    texts = {
        'english': {
            'dates': 'What dates should we book for you?',
            'time': 'What time should the lesson start?',
            'equipment': 'Skis or snowboard?',
            'participants': 'How many people?',
            'age': 'Please specify the approximate age.',
            'error_text': 'Oops! Something was filled in incorrectly, please try again:'
        },
        'russian': {
            'dates': 'На какие даты вас записать?',
            'time': 'Время начала занятия?',
            'equipment': 'Лыжи или сноуборд?',
            'participants': 'Сколько людей?',
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

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
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
        text = ('**Great! Just answer the following questions:**\n'
                '1. What is your name?\n'
                '2. What is your phone number?\n'
                '3. Where do you live or where will you stay?\n'
                'This is needed for the instructor to know,\n'
                'where it will be more convenient to start and meet you')
    else:
        text = ('**Отлично! Осталось ответить на следующие вопросы:**\n'
                '1. Как вас зовут?\n'
                '2. Какой у вас номер телефона?\n'
                '3. Где вы живете или будете жить?\n'
                'Это нужно инструктору, чтобы знать,\n'
                'где вам будет ближе начать и встретить вас')

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

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def instructor_booking_confirmation_text(lang, dates, time, equipment, participants, age, name, phone_number, place):
    if lang == "english":
        return (
            f"**Confirm your booking by replying with 'yes'/'ok'**\n"
            f"After that, we will connect you with an instructor.\n"
            f"To cancel the rental, type 'cancel'.\n\n"
            f"📅 {dates} | {time}\n"
            f"👥 {participants} | {age}\n"
            f"🎿 {equipment}\n\n"
            f"👤 {name}\n"
            f"📞 {phone_number}\n"
            f"📍 {place}\n"
        )
    else:
        return (
            f"**Подтвердите вашу запись, написав “да”/“ага”**\n"
            f"После этого мы свяжем вас с инструктором\n"
            f"Для отмены аренды напишите 'отмена'\n\n"
            f"📅 {dates} | {time}\n"
            f"👥 {participants} | {age}\n"
            f"🎿 {equipment}\n\n"
            f"👤 {name}\n"
            f"📞 {phone_number}\n"
            f"📍 {place}\n"
        )


def new_instructor_booking_text(user, dates, time, equipment, participants, age, name, phone_number, place):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    return (f"🆕 Заявка на инструктора\n"
            f"👤 {user_mention}{username}\n\n"
            f"📅 {dates} | {time}\n"
            f"👥 {participants} | {age}\n"
            f"🎿 {equipment}\n\n"
            f"👤 {name}\n"
            f"📞 {phone_number}\n"
            f"📍 {place}\n")


def instructor_booking_confirmed_text(lang):
    if lang == "english":
        return ("🎉 Your booking is confirmed!\n\n"
                "**Please pay in cash (₾/$)**\n"
                "Your contact information has been shared with the instructor.")
    else:
        return ("🎉 Ваша запись подтверждена!\n\n"
                "**Пожалуйста, оплатите наличными (₾/$)**\n"
                "Ваш контакт передан инструктору")
# ======== Hire Instructor ========


# ======== Food & Coffee ========
def food_order_info_text(lang):
    if lang == "english":
        text = """**🍔 Food & Coffee at New-Gudauri Loft 2**
**🛍️ Pickup Only**

Make your choice using numbers or letters:  

**🍴Main Dishes**  
**1.** Syrniki + sour cream (3 pcs) — **10₾**  
**2.** Pancakes + sour cream (3 pcs) — **10₾**  
**3.** Rice-milk porridge + jam — **10₾**  
**4.** “FastTrack” Sandwich (2 pcs) — **5₾**  
**5.** Borscht soup (beef) — **10₾**  
**6.** “Junior” Burger (beef) — **15₾**  
**7.** “KurCheese” Burger — **20₾**  
**8.** “BeefCheese” Burger (beef) — **25₾**  

**🍝 Hot Dishes & Wok**  
**9.**  Spaghetti Carbonara — **15₾**  
**10.** Chicken Wok — **15₾**  
**11.** Vegetable Wok — **15₾**  
**12.** Rice Wok with beef — **20₾**  

**🥤 Drinks**  
**13.** Water 0.5 L — **2.5₾**  
**14.** Cola 0.5 L — **5₾**  
**15.** Quince juice 1 L — **10₾**  
**16.** 100% Grape juice 1 L — **15₾**  
**17.** Freshly squeezed apple juice 0.5 L — **20₾**  

**☕ Coffee**  
**18.** Americano (350 ml) — **5₾**  
**19.** Cappuccino (350 ml) — **7.5₾**  
**20.** Latte (350 ml) — **10₾**  
**21.** Glace (350 ml) — **10₾**"""
    else:
        text = """**🍔 Еда & Кофе в New-Gudauri Loft 2**
**🛍️ Только самовывоз**

Сделайте свой выбор, цифрами или буквами:

**🍴Основные блюда**
**1.** Сырники + сметана (3 шт) — **10₾**
**2.** Блинчики + сметана (3 шт) — **10₾**
**3.** Каша рисо-молочная + варенье — **10₾**
**4.** Сэндвич “ФастТрэк” (2 шт) — **5₾**
**5.** Суп борщ (говядина) — **10₾**
**6.** Бургер “Джуниор” (говяжий) — **15₾**
**7.** Бургер “КурЧиз” — **20₾**
**8.** Бургер “БифЧиз” (говяжий) — **25₾**

**🍝 Горячее и Wok**
**9.**  Спагетти Карбонара — **15₾**
**10.** Вок с курицей — **15₾**
**11.** Вок с овощами — **15₾**
**12.** Рис-вок с говядиной — **20₾**

**🥤 Напитки**
**13.** Вода 0.5 л — **2.5₾**
**14.** Вода “Кола” 0.5 л — **5₾**
**15.** Сок айва 1 л — 10₾
**16.** Сок 100% виноград 1 л — **15₾**
**17.** Свежевыжатый сок яблоко 0.5 л — **20₾**

**☕ Кофе**
**18.** Американо (350 мл) — **5₾**
**19.** Капучино (350 мл) — **7.5₾**
**20.** Латте (350 мл) — **10₾**
**21.** Гляссе (350 мл) — **10₾**"""

    return text


def food_order_text(lang, selected_items):
    if lang == 'english':
        title = '📝 Your order'
        payment_info = ('Please pay in cash in GEL or USD (₾/$).\n'
                        'Currently, only pickup is available.\n\n'
                        'Confirm your booking by replying with “yes” or “okay”.')
    else:
        title = '📝 Ваш заказ'
        payment_info = ('Пожалуйста, оплатите наличными (₾/$).\n'
                        '**На данный момент доступен только самовывоз.**\n\n'
                        '**Подтвердите ваше бронирование, написав “да”/“ага”**')

    order_text = get_order_text(selected_items, lang)
    text = (f"**{title}:**\n"
            f"{order_text}\n\n"
            f"{payment_info}")

    return text


def get_order_text(selected_items, lang='russian'):
    total_text = 'Total' if lang == 'english' else 'Итого'
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

    text += f"\n{total_text}: {total_price}₾"

    return text


def calculate_total_price(selected_items):
    total_price = float()

    for item in selected_items:
        quantity = item['quantity']
        price = food_coffee_dict['russian'][item['number']]['price']
        total_price += quantity * price

    return total_price


def food_order_confirmed_text(lang, order_num):
    if lang == 'english':
        text = (f'**🛍️ Your order ({order_num}) is being prepared**\n'
                '⏳ In about **20 minutes** it will be ready for pickup!\n'
                '📍 **Loft 2**, any entrance to the elevator, 2nd floor, **№227**\n\n'
                '**The operator will contact you soon and confirm your order. Thank you!**')
    else:
        text = (f'**🛍️ Ваш заказ ({order_num}) готовится**\n'
                '⏳ Примерно через **20 минут** он будет готов для самовывоза!\n'
                '📍 **Loft 2**, любой вход к лифту, 2 этаж, **№227**\n\n'
                '**Оператор скоро свяжется с вами и подтвердит заказ, спасибо!**')

    return text


def new_food_order_text(user, selected_items):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    order_text = get_order_text(selected_items)

    return (f"🆕 Заявка на еду\n\n"
            f"👤 {user_mention}{username}\n"
            f"{order_text}")


def no_food_selected_error(lang):
    if lang == 'english':
        return "Oops! You haven't selected any food or coffee yet. Please choose something before placing your order."
    else:
        return "Ой! Вы еще не выбрали ни одно блюдо или кофе. Пожалуйста, выберите что-нибудь перед тем, как сделать заказ."
# ======== Food & Coffee =======


# ======== Massage =======
def massage_service_info_text(lang):
    if lang == "english":
        text = """**💆 Massage**

🕒 9:00 AM - 9:00 PM 🕒  
**1.** Relaxing Massage  1hr/1.5hrs  99₾/138 GEL  
**2.** Classic Massage   1hr/1.5hrs  110₾/150₾  
**3.** Sports Massage    1hr/1.5hrs  120₾/169₾  
**4.** Therapeutic Session 1.5hrs/2hrs 195₾/245₾  
**5.** Balinese Massage  1hr/1.5hrs  120₾/169₾  
**6.** Anti-cellulite Massage 1hr/1.5hrs 110₾/150₾  
**7.** Head + Face Massage 1hr/1.5hrs 110₾/150₾

Please choose the type of massage and its duration.

**Example:**  
Therapeutic 2hrs  
Relaxing 1hr"""
    else:
        text = """**💆Массаж**

🕒 9.00 - 21.00 🕒
**1.** Расслабляющий  1ч/1.5ч  99/138 лари 
**2.** Классический     1ч/1.5ч 110/150₾
**3.** Спортивный       1ч/1.5ч 120/169₾
**4.** Лечебный сеанс   1.5ч/2ч 195/245₾
**5.** Балийский массаж 1ч/1.5ч 120/169₾
**6.** Антицеллюлитный  1ч/1.5ч 110/150₾
**7.** Голова + лицо    1ч/1.5ч 110/150₾

Выберите, какой будет вид массажа и длительность 

**Пример:**
Лечебный 2 ч
Расслабляющий 1"""

    return text


def massage_type_request_text(lang):
    if lang == "english":
        return ("What date and time would you like to book?\n\n"
                "**Example:**\n"
                "January 4th, 12:00\n"
                "January 8th at 10:00")
    else:
        return ("На какую дату и время вас записать?\n\n"
                "**Пример:**\n"
                "4 января, 12 00\n"
                "8 января в 10")


def massage_booking_error(lang):
    if lang == 'english':
        return 'Oops! Something was filled in incorrectly, please try again'
    else:
        return 'Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова'


def massage_booking_confirmation_request_text(lang, dates, time, massage_type, duration):
    if lang == "english":
        return (f"**Confirm your booking by replying 'yes'/'ok'**\n"
                f"After that, we will connect you with an operator\n"
                "To cancel your booking, type 'cancel'.\n\n"
                f"📅 {dates} {time}\n"
                f"💆 {massage_type} {duration}")
    else:
        return (f"**Подтвердите вашу запись, написав “да”/“ага”**\n"
                f"После этого мы свяжем вас с оператором\n"
                "Для отмены записи напишите 'отмена'.\n\n"
                f"📅 {dates} {time}\n"
                f"💆 {massage_type} {duration}")


def massage_booking_confirmed_text(lang):
    if lang == "english":
        return (f"**🎉 Your booking is confirmed!**\n"
                f"📍 Come to Loft 2, any entrance to the elevator, 2nd floor, #228\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"📍 Приходите Loft 2, любой вход к лифту, 2 этаж, №228\n"
                f"Пожалуйста, оплатите наличными (₾/$)")


def massage_booking_text(user, dates, time, massage_type, duration):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    return (f"🆕 Заявка на массаж\n\n"
            f"👤 {user_mention}{username}\n"
            f"📅 {dates} {time}\n"
            f"💆 {massage_type} {duration}")
# ======== Massage =======


# ======== Templates ========
def service_unavailable_error(lang):
    if lang == "english":
        return "🏗 This service is unavailable"
    else:
        return "🏗 Этот сервис временно недоступен"


service_types = [
    "rent_equipment", "instructor", "food_coffee", "massage", "transfer_taxi", "paragliding",
    "snowbike_tour", "exchange", "ski_service", "photo_video", "cleaning", "rent_flat", "undefined"
]


SERVICES = {
    "1": ["rent_equipment", "Rent Ski/Board", "Прокат"],
    "2": ["instructor", "Instructor", "Инструктор"],
    "3": ["food_coffee", "Food/Coffee", "Еда/Кофе"],
    "4": ["massage", "Massage", "Массаж"],
    "5": ["transfer_taxi", "Transfer/Taxi", "Трансфер/Такси"],
    "6": ["paragliding", "Paragliding", "Полет на параплане"],
    "7": ["snowbike_tour", "Snowbike tour", "Снегоход"],
    "8": ["exchange", "Exchange", "Обмен валют"],
    "9": ["ski_service", "Ski-service", "Ремонт снаряжения"],
    "10": ["photo_video", "Photo/Video", "Фото/Видео"],
    "11": ["cleaning", "Cleaning", "Уборка"],
    "12": ["rent_flat", "RentFlat", "Аренда Квартир"]
}


food_coffee_dict = {
    "english": {
        1: {"name": "Syrniki with sour cream (3 pcs) — **10₾**", "price": 10},
        2: {"name": "Pancakes with sour cream (3 pcs) — **10₾**", "price": 10},
        3: {"name": "Rice-milk porridge + jam — **10₾**", "price": 10},
        4: {"name": "“FastTrack” Sandwich (2 pcs) — **5₾**", "price": 5},
        5: {"name": "Borscht soup (beef) — **10₾**", "price": 10},
        6: {"name": "“Junior” Burger (beef) — **15₾**", "price": 15},
        7: {"name": "“KurCheese” Burger — **20₾**", "price": 20},
        8: {"name": "“BeefCheese” Burger (beef) — **25₾**", "price": 25},
        9: {"name": "Spaghetti Carbonara — **15₾**", "price": 15},
        10: {"name": "Chicken Wok — **15₾**", "price": 15},
        11: {"name": "Vegetable Wok — **15₾**", "price": 15},
        12: {"name": "Rice Wok with beef — **20₾**", "price": 20},
        13: {"name": "Water 0.5 L — **2.5₾**", "price": 2.5},
        14: {"name": "Cola 0.5 L — **5₾**", "price": 5},
        15: {"name": "Quince juice 1 L — **10₾**", "price": 10},
        16: {"name": "100% Grape juice 1 L — **15₾**", "price": 15},
        17: {"name": "Freshly squeezed apple juice 0.5 L — **20₾**", "price": 20},
        18: {"name": "Americano (350 ml) — **5₾**", "price": 5},
        19: {"name": "Cappuccino (350 ml) — **7.5₾**", "price": 7.5},
        20: {"name": "Latte (350 ml) — **10₾**", "price": 10},
        21: {"name": "Glace (350 ml) — **10₾**", "price": 10},
    },
    "russian": {
        1: {"name": "Сырники с сметаной (3 шт) — **10₾**", "price": 10},
        2: {"name": "Блинчики с сметаной (3 шт) — **10₾**", "price": 10},
        3: {"name": "Каша рисо-молочная + варенье — **10₾**", "price": 10},
        4: {"name": "Сэндвич “ФастТрэк” (2 шт) — **5₾**", "price": 5},
        5: {"name": "Суп борщ (говядина) — **10₾**", "price": 10},
        6: {"name": "Бургер “Джуниор” (говяжий) — **15₾**", "price": 15},
        7: {"name": "Бургер “КурЧиз” — **20₾**", "price": 20},
        8: {"name": "Бургер “БифЧиз” (говяжий) — **25₾**", "price": 25},
        9: {"name": "Спагетти Карбонара — **15₾**", "price": 15},
        10: {"name": "Вок с курицей — **15₾**", "price": 15},
        11: {"name": "Вок с овощами — **15₾**", "price": 15},
        12: {"name": "Рис-вок с говядиной — **20₾**", "price": 20},
        13: {"name": "Вода 0.5 л — **2.5₾**", "price": 2.5},
        14: {"name": "Вода “Кола” 0.5 л — **5₾**", "price": 5},
        15: {"name": "Сок айва 1 л — 10₾", "price": 10},
        16: {"name": "Сок 100% виноград 1 л — **15₾**", "price": 15},
        17: {"name": "Свежевыжатый сок яблоко 0.5 л — **20₾**", "price": 20},
        18: {"name": "Американо (350 мл) — **5₾**", "price": 5},
        19: {"name": "Капучино (350 мл) — **7.5₾**", "price": 7.5},
        20: {"name": "Латте (350 мл) — **10₾**", "price": 10},
        21: {"name": "Гляссе (350 мл) — **10₾**", "price": 10},
    }

}
# ======== Templates ========
