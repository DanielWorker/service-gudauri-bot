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
1-3 дня подряд: **47,5₾ (18$)/сутки** комплект
4-6 дней подряд: **42₾/сутки** комплект
От 7 дней подряд: **35₾/сутки** комплект

**🎿 Комплект включает:**
• Лыжи, палки, ботинки, шлем
• Сноуборд, ботинки, шлем
• Куртка, штаны, маска

**🧩 Дополнительные предметы:**
• Лыжи + палки / сноуборд: **39₾/1 сутки**
• Маска: **10₾/день**
• Шлем: **10₾/день**
• Перчатки: **10₾/день**
• Защитные шорты: **10₾/день**
• Куртка: **20₾/день**
• Штаны: **20₾/день**

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
        return (f"Confirm your booking, after which we will connect you with an operator\n"
                f"You can also add any additional equipment by writing them below\n"
                f"To cancel the rental, type 'Cancel'\n\n"
                f"{user_list}")
    else:
        return (f"Подтвердите ваше бронирование, после чего мы свяжем вас с оператором\n"
                f"Вы так же можете добавить необходимое снаряжение написав ниже\n"
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
        return "🎉 Your equipment booking has been confirmed!"
    else:
        return "🎉 Ваша бронирование снаряжения подтверждено!"
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
- **250₾ (91$)** for 1 person
- **360₾ (132$)** for a group of 2 people

🕘 12:30 – 14:30 🕒
- **230₾ (84$)** for 1 person
- **350₾ (128$)** for a group of 2 people

🕘 15:00 – 17:00 🕒
- **210₾ (77$)** for 1 person
- **310₾ (114$)** for a group of 2 people

┌────────┐
    **👨‍👩‍👦 For Children**
└────────┘
🕘 10:10 – 12:10 🕒
- **250₾ (91$)** for 1 child 
- **360₾ (132$)** for a group of 2 children

🕘 12:30 – 14:30 🕒
- **240₾ (88$)** for 1 child 
- **350₾ (128$)** for a group of 2 children

🕘 15:00 – 17:00 🕒
- **240₾ (88$)** for 1 child 
- **350₾ (128$)** for a group of 2 children
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
- **250₾ (91$)** за 1 человека
- **360₾ (132$)** за группу из 2 человек

🕘 12:30 – 14:30 🕒
- **230₾ (84$)** за 1 человека
- **350₾ (128$)** за группу из 2 человек

🕘 15:00 – 17:00 🕒
- **210₾ (77$)** за 1 человека
- **310₾ (114$)** за группу из 2 человек

┌───────┐
    **👨‍👩‍👦 Для детей**
└───────┘ 
🕘 10:10 – 12:10 🕒
- **250₾ (91$)** за 1 ребенка
- **360₾ (132$)** за группу из 2 детей

🕘 12:30 – 14:30 🕒
- **240₾ (88$)** за 1 ребенка
- **350₾ (128$)** за группу из 2 детей

🕘 15:00 – 17:00 🕒
- **240₾ (88$)** за 1 ребенка
- **350₾ (128$)** за группу из 2 детей
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
1. На какую дату и время вас записать?
2. Какой снаряд вы будете использовать?
3. Предпочитаете групповое занятие для взрослых или индивидуальное для ребенка?

**Примеры:**
1. 8 января, 10:10
2. Лыжи
3. 1 ребенок

1. 4 января, 12:30
2. Сноуборд
3. 2 взрослых"""


def instructor_booking_confirmation_text(lang, date_time, lesson_preference, equipment):
    if lang == "english":
        return (f"Confirm your booking, after which we will connect you with an operator, or write 'cancel'\n\n"
                f"1. {date_time}\n"
                f"2. {lesson_preference}\n"
                f"3. {equipment}")
    else:
        return (f"Подтвердите вашу запись, после чего мы свяжем ваc с оператором, или же напишите 'отмена'\n\n"
                f"1. {date_time}\n"
                f"2. {lesson_preference}\n"
                f"3. {equipment}")


def new_instructor_booking_text(user, date_time, lesson_preference, equipment):
    user_mention = utils.get_user_mention(user.user_id, user.full_name)
    username = f' | @{user.username}' if user.username else ''

    return (f"🆕 Заявка на инструктора\n\n"
            f"👤 {user_mention}{username}\n"
            f"1. {date_time}\n"
            f"2. {lesson_preference}\n"
            f"3. {equipment}")


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
**1.** Syrniki with sour cream (3 pcs) — **10₾**  
**2.** Pancakes with sour cream (3 pcs) — **10₾**  
**3.** Rice-milk porridge + jam — **10₾**  
**4.** “FastTrack” Sandwich (2 pcs) — **5₾**  
**5.** Borscht soup (beef) — **10₾**  
**6.** “Junior” Burger (beef) — **15₾**  
**7.** “KurCheese” Burger — **20₾**  
**8.** “BeefCheese” Burger (beef) — **25₾**  

**🍝 Hot Dishes & Wok**  
**9.** Spaghetti Carbonara — **15₾**  
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
**1.** Сырники с сметаной (3 шт) — **10₾**
**2.** Блинчики с сметаной (3 шт) — **10₾**
**3.** Каша рисо-молочная + варенье — **10₾**
**4.** Сэндвич “ФастТрэк” (2 шт) — **5₾**
**5.** Суп борщ (говядина) — **10₾**
**6.** Бургер “Джуниор” (говяжий) — **15₾**
**7.** Бургер “КурЧиз” — **20₾**
**8.** Бургер “БифЧиз” (говяжий) — **25₾**

**🍝 Горячее и Wok**
**9.** Спагетти Карбонара — **15₾**
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
    text = (f"{title}:\n"
            f"{order_text}\n\n"
            f"{payment_info}")

    return text


def get_order_text(selected_items, total_price, lang='russian'):
    unit = 'pcs' if lang == 'english' else 'шт'
    total_text = 'Total' if lang == 'english' else 'Итого'
    text = ''

    for n, item in enumerate(selected_items, start=1):
        number = item['number']
        quantity = item['quantity']
        position_name = food_coffee_dict[lang][number]
        q_text = f"  x {quantity} ({unit})" if quantity > 1 else ""

        text += f'{n}. {position_name}{q_text}\n'

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
