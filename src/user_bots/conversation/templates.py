from src import utils


def select_language_text():
    return ("Выберите язык напишите цифру/слово\n"
            "Choose language with number/word\n"
            "1 `Русский`\n"
            "2 `English`\n")


def select_language_error():
    return ("Пожалуйста попробуйте еще раз\n"
            "Please try again")


def all_services_text(lang):
    if lang == "english":
        text = """Write number/word, what do you want?

1. 🎿Rent Ski & Board 
2. ⛷Instructor    
3. 🍔Food & Coffee
4. 💆Massage                
5. 🚕Transfer & Taxi
6. 🪂Paragliding
7. 🏍Snowbike tour     
8. 💵Exchange       
9. 🛠Ski-service
10. 📹 Photo/Video  
11. 🧹Cleaning           
12. 🏠RentFlat

Ski-lift Open/Closed 🟢🔴 
Road status 🟢🔴
[Check](https://t.me/ASG_Status)
"""
    else:
        text = """Здравствуйте, напишите цифру/слово

1. 🎿Прокат лыж & Сноубордов
2. ⛷Инструктор    
3. 🍔Еда & Кофе
4. 💆Массаж
5. 🚕Трансфер & Такси
6. 🪂Полет на параплане
7. 🏍Тур на снегоходе
8. 💵Обмен валют       
9. 🛠Ремонт снаряжения
10. 📹Фото & Видео  
11. 🧹Уборка           
12. 🏠Аренда Квартир

Статус подъемников 🟢🔴
Статус авто дорог из-за снега 🟢🔴
[Проверить](https://t.me/ASG_Status)
"""

    return text


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
                "__Order example: 1 1 2 4__")
    else:
        return ("Ой! Вы еще не выбрали ни одно блюдо или кофе. Пожалуйста, выберите что-нибудь перед тем, как сделать заказ.\n"
                "__Пример заказа: 1 1 2 4__")


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

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
        text += f"{n}. {key_text}\n"
        n += 1

    return text


def instructor_booking_confirmation_text(lang, dates, time, equipment, participants, age, name, phone_number, place):
    if lang == "english":
        return (
            f"**Confirm your booking by replying with 'yes'/'ok'**\n"
            f"After that, we will connect you with an instructor.\n"
            f"To cancel the booking, type 'cancel'.\n\n"
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
            f"Для отмены бронирования напишите 'отмена'\n\n"
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

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
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

🕒 9:00 AM - 9:00 PM 🕒  
**1.** Relaxing  ⏰ 1h — 99₾ / 1.5h — 138₾  
**2.** Classic    ⏰ 1h — 110₾ / 1.5h — 150₾  
**3.** Sports    ⏰ 1h — 120₾ / 1.5h — 169₾  
**4.** Therapeutic Session ⏰ 1.5h — 195₾ / 2h — 249₾  
**5.** Balinese  ⏰ 1h — 120₾ / 1.5h —  169₾  
**6.** Anti-cellulite ⏰ 1h — 110₾ / 1.5h — 150₾
**7.** Back + legs ⏰ 1h — 110₾ / 1.5h — 150₾

1. What type of massage will it be?
2. Duration?

**Example:**
Classic
1.5 hours

__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        text = """**💆Массаж**

🕒 9.00 - 20.00 🕒
1. Расслабляющий    1 час ⏰ 99₾ / 1.5⏰  138₾
2. Классический         1 час ⏰ 110₾ / 1.5⏰  150₾
3. Спортивный            1 час ⏰ 120₾ / 1.5⏰  169₾
4. Лечебный сеанс     1.5     ⏰ 195₾ / 2 ⏰  249₾
5. Балийский                1 час ⏰ 120₾ / 1.5⏰  169₾
6. Антицеллюлитный 1 час ⏰ 110₾ / 1.5⏰  150₾
7. Спина + ноги            1 час ⏰ 110₾ / 1.5⏰  150₾

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
    date_str = utils.convert_date_to_str(date)
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
                f"📍 Come to Loft 2, any entrance to the elevator, 2nd floor, №239\n"
                f"Please pay in cash (₾/$)")
    else:
        return (f"**🎉 Ваша запись подтверждена!**\n"
                f"📍 Приходите Loft 2, любой вход к лифту, 2 этаж, №239\n"
                f"Пожалуйста, оплатите наличными (₾/$)")


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
2.	Time? 10:00 - 17:00
3.	What is your name?
4.	What is your phone number?

**This is needed for the pilot to contact you.**

Example (please write in separate lines):
January 4
10:00
Sasha
+9955513437122

__To return to the menu, type 'menu' / 'cancel' / 'no'__""",
        "russian": """
1. На какую дату вас записать?
2. Время? 10.00 - 17.00
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
            value = utils.convert_date_to_str(value)

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
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

"__To return to the menu, type 'menu' / 'cancel' / 'no'__"""
    else:
        text = f"""**🗻 Мы находимся в Нью-Гудаури**
💱 Обмен только от 100$ на лари ₾
💵 Курс сегодня $1 = ₾{current_rate}

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

        key_text = value + ' ✅' if value != 'None' else texts[lang][key]
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
# ======== Templates ========
