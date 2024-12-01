

def select_language_text():
    return ("Выберите язык / Choose a language:\n"
            "`Русский` / `English`")


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
13. 🏠RentFlat"""
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
13. 🏠Аренда Квартир """

    return text


def service_unavailable_error(lang):
    if lang == "english":
        return "🏗 This service is unavailable"
    else:
        return "🏗 Этот сервис временно недоступен"


service_types = [
    "rent_sky_board", "instructor", "food_coffee", "massage", "transfer_taxi", "paragliding",
    "snowbike_tour", "exchange", "ski_service", "photo_video", "cleaning", "rent_flat", "undefined"
]


SERVICES = {
    "1": ["rent_sky_board", "Rent Ski/Board", "Прокат"],
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
