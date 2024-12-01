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

1. 🎿Rent Ski/Board 
2. ⛷Instructor    
3. 🍔Food/Coffee
4. 💆Massage                
5. 🚕Transfer/Taxi
6. 🪂Paragliding
7. 🏍Snowbike tour     
8. 💵Exchange       
9. 🛠Ski-service
11. 📹 Photo/Video  
12. 🧹Cleaning           
13. 🏠RentFlat

Ski-lift Open/Closed 🟢🔴 
Road status 🟢🔴
[Check]](https://t.me/ASG_Status)
"""
    else:
        text = """Здравствуйте, напишите цифру/слово на русском, если вы знаете этот язык

1. 🎿Прокат лыж/сноубордов
2. ⛷Инструктор    
3. 🍔Еда/Кофе
4. 💆Массаж
5. 🚕Трансфер/Такси
6. 🪂Полет на параплане
7. 🏍Тур на снегоходе
8. 💵Обмен валют       
9. 🛠Ремонт снаряжения
11. 📹Фото/Видео  
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
