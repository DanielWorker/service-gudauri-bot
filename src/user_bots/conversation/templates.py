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
14. 🎫Sell Ski-pass

Ski-lift Open/Closed 🟢🔴 
Road status 🟢🔴
[Check]](https://t.me/ASG_Status)
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
14. 🎫Продам Ski-pass

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
• Pants: **20₾/day**

We’ll be waiting for you!"""
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
• Штаны: **20₾/сутки**

Будем ждать вас!"""


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
1. What date and time should we book for you?
2. What equipment will you use?
3. Would you prefer a group lesson for adults or an individual lesson for a child?

**Examples:**
1. January 8th, 10:10
2. Skis
3. 1 child

1. January 4th, 12:30
2. Snowboard
3. 2 adults"""
    else:
        return """
1. На какие даты и время вас записать?
2. Какой снаряд вы будете использовать?
3. Сколько взрослых или индивидуально для ребенка?

Примеры: 
8 января, 10 10
Лыжи
1 ребенок

4 января, 12 30
Сноуборд
2 взрослых"""


def instructor_booking_error(lang, date_time, equipment, lesson_preference):
    if lang == 'english':
        dt_prompt = 'What date and time should we book for you?'
        e_prompt = 'What equipment will you use?'
        lp_prompt = 'Would you prefer a group lesson for adults or an individual lesson for a child?'
        error_text = "Oops! Something was filled in incorrectly, please try again:"
    else:
        dt_prompt = 'На какие даты и время вас записать?'
        e_prompt = 'Какое снаряжение вы будете использовать?'
        lp_prompt = 'Сколько взрослых или индивидуально для ребенка?'
        error_text = "Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:"

    dt_text = date_time + ' ✅' if date_time != 'None' else dt_prompt
    e_text = equipment + ' ✅' if equipment != 'None' else e_prompt
    lp_text = lesson_preference + ' ✅' if lesson_preference != 'None' else lp_prompt

    return (f"**{error_text}**\n\n"
            f"1. {dt_text}\n"
            f"2. {e_text}\n"
            f"3. {lp_text}\n")


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


def instructor_booking_user_data_request_error(lang, name, phone_number, place):
    if lang == 'english':
        n_prompt = 'What is your name?'
        pn_prompt = 'What is your phone number?'
        p_prompt = 'Where do you live or where will you stay?'
        error_text = "Oops! Something was filled in incorrectly, please try again:"
    else:
        n_prompt = 'Как вас зовут?'
        pn_prompt = 'Какой у вас номер телефона?'
        p_prompt = 'Где вы живете или будете жить?'
        error_text = "Ой! Похоже, что-то заполнено неверно. Пожалуйста, попробуйте снова:"

    n_text = name + ' ✅' if name != 'None' else n_prompt
    pn_text = phone_number + ' ✅' if phone_number != 'None' else pn_prompt
    p_text = place + ' ✅' if place != 'None' else p_prompt

    return (f"**{error_text}**\n\n"
            f"1. {n_text}\n"
            f"2. {pn_text}\n"
            f"3. {p_text}\n")


def instructor_booking_confirmation_text(lang, date_time, equipment, lesson_preference, name, phone_number, place):
    if lang == "english":
        return (f"**Confirm your booking by replying with 'yes'/'ok'**\n"
                f"After that, we will connect you with an instructor.\n"
                f"To cancel the rental, type 'cancel'.\n\n"
                f"1. {date_time}\n"
                f"2. {equipment}\n"
                f"3. {lesson_preference}\n"
                f"4. {name}\n"
                f"5. {phone_number}\n"
                f"6. {place}\n")
    else:
        return (f"**Подтвердите вашу запись, написав “да”/“ага”**\n"
                f"После этого мы свяжем вас с инструктором\n"
                f"Для отмены аренды напишите 'отмена'\n\n"
                f"1. {date_time}\n"
                f"2. {equipment}\n"
                f"3. {lesson_preference}\n"
                f"4. {name}\n"
                f"5. {phone_number}\n"
                f"6. {place}\n")


def new_instructor_booking_text(user, date_time, lesson_preference, equipment, name, phone_number, place):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    return (f"🆕 Заявка на инструктора\n\n"
            f"👤 {user_mention}{username}\n"
            f"1. {date_time}\n"
            f"2. {equipment}\n"
            f"3. {lesson_preference}\n"
            f"4. {name}\n"
            f"5. {phone_number}\n"
            f"6. {place}\n")


def instructor_booking_confirmed_text(lang):
    if lang == "english":
        return "🎉 Your equipment booking has been confirmed!"
    else:
        return "🎉 Ваша бронирование снаряжения подтверждено!"
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


def food_order_text(lang, selected_items, total_price):
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

    order_text = get_order_text(selected_items, total_price, lang)
    text = (f"**{title}:**\n"
            f"{order_text}\n\n"
            f"{payment_info}")

    return text


def get_order_text(selected_items, total_price, lang='russian'):
    unit = 'pcs' if lang == 'english' else 'шт'
    total_text = 'Total' if lang == 'english' else 'Итого'
    text = ''

    n = 1
    for item in selected_items:
        number = item['number']
        quantity = item['quantity']
        position_name = food_coffee_dict[lang][number]
        # q_text = f"  x {quantity} ({unit})" if quantity > 1 else ""

        for _ in range(quantity):
            text += f'{n}. {position_name}\n'
            n += 1

    text += f"\n{total_text}: {total_price}₾"

    return text


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


def new_food_order_text(user, selected_items, total_price):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''
    order_text = get_order_text(selected_items, total_price)

    return (f"🆕 Заявка на еду\n\n"
            f"👤 {user_mention}{username}\n"
            f"{order_text}")


def no_food_selected_error(lang):
    if lang == 'english':
        return "Oops! You haven't selected any food or coffee yet. Please choose something before placing your order."
    else:
        return "Ой! Вы еще не выбрали ни одно блюдо или кофе. Пожалуйста, выберите что-нибудь перед тем, как сделать заказ."
# ======== Food & Coffee =======

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
        1: "Syrniki with sour cream (3 pcs) — **10₾**",
        2: "Pancakes with sour cream (3 pcs) — **10₾**",
        3: "Rice-milk porridge + jam — **10₾**",
        4: "“FastTrack” Sandwich (2 pcs) — **5₾**",
        5: "Borscht soup (beef) — **10₾**",
        6: "“Junior” Burger (beef) — **15₾**",
        7: "“KurCheese” Burger — **20₾**",
        8: "“BeefCheese” Burger (beef) — **25₾**",
        9: "Spaghetti Carbonara — **15₾**",
        10: "Chicken Wok — **15₾**",
        11: "Vegetable Wok — **15₾**",
        12: "Rice Wok with beef — **20₾**",
        13: "Water 0.5 L — **2.5₾**",
        14: "Cola 0.5 L — **5₾**",
        15: "Quince juice 1 L — **10₾**",
        16: "100% Grape juice 1 L — **15₾**",
        17: "Freshly squeezed apple juice 0.5 L — **20₾**",
        18: "Americano (350 ml) — **5₾**",
        19: "Cappuccino (350 ml) — **7.5₾**",
        20: "Latte (350 ml) — **10₾**",
        21: "Glace (350 ml) — **10₾**",
    },
    "russian": {
        1: "Сырники с сметаной (3 шт) — **10₾**",
        2: "Блинчики с сметаной (3 шт) — **10₾**",
        3: "Каша рисо-молочная + варенье — **10₾**",
        4: "Сэндвич “ФастТрэк” (2 шт) — **5₾**",
        5: "Суп борщ (говядина) — **10₾**",
        6: "Бургер “Джуниор” (говяжий) — **15₾**",
        7: "Бургер “КурЧиз” — **20₾**",
        8: "Бургер “БифЧиз” (говяжий) — **25₾**",
        9: "Спагетти Карбонара — **15₾**",
        10: "Вок с курицей — **15₾**",
        11: "Вок с овощами — **15₾**",
        12: "Рис-вок с говядиной — **20₾**",
        13: "Вода 0.5 л — **2.5₾**",
        14: "Вода “Кола” 0.5 л — **5₾**",
        15: "Сок айва 1 л — 10₾",
        16: "Сок 100% виноград 1 л — **15₾**",
        17: "Свежевыжатый сок яблоко 0.5 л — **20₾**",
        18: "Американо (350 мл) — **5₾**",
        19: "Капучино (350 мл) — **7.5₾**",
        20: "Латте (350 мл) — **10₾**",
        21: "Гляссе (350 мл) — **10₾**",
    }

}
# ======== Templates ========
