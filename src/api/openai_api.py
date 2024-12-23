import json
import re

from openai import OpenAI

# import src.settings as stg
# client = OpenAI(api_key=stg.OPENAI_API_KEY)

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)


def detect_input_language(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that determines the language of a user's input. "
                    "If the text is in Russian, respond with 'russian'. If the text is in English, respond with 'english'. "
                    "For all other languages or if the text is unrecognizable, respond with 'undefined'. "
                    "Only return a JSON object containing the key 'language' with one of the following values: "
                    "'russian', 'english', or 'undefined'."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_language_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "language": {
                            "description": "The detected language of the user's input.",
                            "type": "string",
                            "enum": ["russian", "english", "undefined"]
                        }
                    },
                    "required": ["language"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)['language']


def get_selected_language(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that determines the language based on user input. "
                    "The user may respond with one of the following languages: 'Russian', 'English', 'Русский', 'Английский'. "
                    "If the input is '1', it indicates Russian, and if the input is '2', it indicates English. "
                    "Additionally, the input may contain typos or similar words (e.g., 'Rusky', 'Englesh'). "
                    "Analyze the input, correct potential typos, and return a JSON object with a single key 'language' containing one of the following values: "
                    "'russian', 'english', or 'undefined'. If the input is unrecognizable, return 'undefined'."
                )
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_language_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "language": {
                            "description": "The language detected from the user's input. Possible values are 'russian', 'english', or 'undefined'.",
                            "type": "string",
                            "enum": ["russian", "english", "undefined"]
                        }
                    },
                    "required": ["language"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def determine_service(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that analyzes the user's request for services. "
                    "The user can provide a response in Russian or English, either by service name or by the service number from the following list:""1. Rent Ski/Board Прокат"
                    "1. Rent Equipment Ski/Board Прокат снаряжения"
                    "2. Instructor Инструктор"
                    "3. Food/Coffee Еда/Кофе"
                    "4. Massage Массаж"
                    "5. Transfer/Taxi Трансфер/Такси"
                    "6. Paragliding Полет на параплане"
                    "7. Snowbike tour Снегоход"
                    "8. Exchange Обмен валют"
                    "9. Ski-service Ремонт снаряжения"
                    "10. Photo/Video Фото/Видео"
                    "11. Cleaning Уборка"
                    "12. RentFlat Аренда Квартир"
                    "If the user mentions more than one service, select the most appropriate service or use 'undefined' if no valid service is selected. "
                    "Return a JSON object containing a single key 'service' with one of the following enum values: "
                    "'rent_equipment', 'instructor', 'food_coffee', 'massage', 'transfer_taxi', 'paragliding', 'snowbike_tour', "
                    "'exchange', 'ski_service', 'photo_video', 'cleaning', 'rent_flat', or 'undefined'. "
                    "If no valid service is detected, return 'undefined'."
                )
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_service_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "service": {
                            "description": "The selected service. Possible values are "
                                           "'rent_equipment', 'instructor', 'food_coffee', 'massage', 'transfer_taxi', "
                                           "'paragliding', 'snowbike_tour', 'exchange', 'ski_service', 'photo_video', "
                                           "'cleaning', 'rent_flat', or 'undefined'.",
                            "type": "string",
                            "enum": [
                                "rent_equipment", "instructor", "food_coffee", "massage", "transfer_taxi", "paragliding",
                                "snowbike_tour", "exchange", "ski_service", "photo_video", "cleaning", "rent_flat", "undefined"
                            ]
                        },
                        # "multiple_services": {
                        #     "description": "List of selected services if more than one.",
                        #     "type": "array",
                        #     "items": {
                        #         "type": "string"
                        #     }
                        # }
                    },
                    "required": ["service"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_rental_equipment_details(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts rental equipment details from user input. "
                    "The user may request equipment based on the available options: "
                    "1-3 consecutive days: 47.5₾ (18$)/day per set, "
                    "4-6 consecutive days: 42₾/day per set, "
                    "7 or more consecutive days: 35₾/day per set, "
                    "Skis + poles / snowboard: 39₾/day, "
                    "Goggles: 10₾/day, "
                    "Helmet: 10₾/day, "
                    "Gloves: 10₾/day, "
                    "Protective shorts: 10₾/day, "
                    "Jacket: 20₾/day, "
                    "Pants: 20₾/day."
                    "You will analyze the input and return a JSON object with a key 'rental_equipment' "
                    "which contains the exact text that the user mentioned in their request. "
                    "If no rental equipment is mentioned or it's unclear, return 'None'. "
                    "Example input could be: "
                    "'I would like to rent skis and a helmet for 3 days' or "
                    "'I need a snowboard for 7 days'."
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_rental_equipment_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "rental_equipment": {
                            "description": "The exact equipment requested by the user, or 'None' if not provided.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["rental_equipment"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)

def extract_mentor_booking_details(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты помощник, который извлекает данные для бронирования инструктора. "
                    "Пользователь отвечает на вопросы строго по столбикам в следующем порядке: "
                    "1. На какие даты вас записать? "
                    "2. Время начала занятия? "
                    "3. Лыжи или сноуборд? "
                    "4. Сколько людей? "
                    "5. Укажите примерный возраст. "
                    "Твоя задача: проанализировать текст и извлечь ответы на каждый из вопросов. "
                    "Верни JSON-объект с ключами: 'dates', 'time', 'equipment', 'participants', 'age'. "
                    "Примеры ввода: "
                    "- 8 января\n10 10\nЛыжи\n1 ребенок\n10 лет "
                    "- 4 января\n12 30\nСноуборд\n2 взр\n25-50 лет "
                    "Примечания: "
                    "1. 'dates' должен содержать текст даты или 'None', если даты нет. "
                    "2. 'time' должен содержать время в формате HH MM, если оно указано, иначе 'None'. "
                    "3. 'equipment' должен быть 'Лыжи' или 'Сноуборд', иначе 'None'. "
                    "4. 'participants' содержит информацию о количестве людей, например, '1 ребенок' или '2 взрослых' или '1 взр'. Если не указано, то 'None'. "
                    "5. 'age' содержит возраст участников, например, '10 лет' или диапазон '25-50 лет'. Если возраст не указан, то 'None'."
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_booking_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "dates": {
                            "description": "Текст даты или 'None', если дата не указана.",
                            "type": ["string", "null"]
                        },
                        "time": {
                            "description": "Время в формате HH MM или 'None', если не указано.",
                            "type": ["string", "null"]
                        },
                        "equipment": {
                            "description": "Точное оборудование: 'Лыжи' или 'Сноуборд', иначе 'None'.",
                            "type": ["string", "null"]
                        },
                        "participants": {
                            "description": "Количество людей, например, '1 ребенок' или '2 взр', или 'None', если не указано.",
                            "type": ["string", "null"]
                        },
                        "age": {
                            "description": "Возраст или диапазон возраста, например, '10 лет' или '25-50 лет', или 'None', если не указано.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["dates", "time", "equipment", "participants", "age"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_user_details(user_input):
    phone_pattern = r"(\+?\d{1,3}[ -]?)?(\(?\d{1,5}\)?[ -]?)?[\d\s\-]{6,13}"

    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0).strip() if match else 'None'

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts user details from input. "
                    "The user must answer three questions about their details: "
                    "1. What is your name? "
                    "2. What is your phone number? "
                    "3. Where do you live or where will you stay? "
                    "You should extract a valid name, a valid phone number, and accept any place mentioned by the user for the 'place' key. "
                    "If the name is unclear or not valid (like only a single letter), return 'None'. "
                    "For phone numbers, return 'None' if it doesn't follow international format. "
                    "If any of the answers are missing or unclear, return 'None' for that key. "
                    "You will return a JSON object with three keys: 'name', 'phone_number', and 'place'. "
                    "Each key should contain the exact text that the user sent as a response. "
                    "Examples: "
                    "1. John Doe "
                    "2. +995123456789 "
                    "3. Tbilisi' "
                    "or "
                    "Иван Иванов "
                    "+995912345678 "
                    "В Гудаури или рядом."
                    "or "
                    "Игорь, +995912345678, Hills "
                    "or "
                    "Данил, +487561236532, Gudauri"
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_user_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "description": "The exact name provided by the user, or 'None' if not provided or invalid. It should be a valid name, including first names like 'Даниил'.",
                            "type": ["string", "null"]
                        },
                        "phone_number": {
                            "description": "The exact phone number provided by the user, or 'None' if not provided or invalid. The phone number should follow a valid international format. It could look like +1234567890.",
                            "type": ["string", "null"]
                        },
                        "place": {
                            "description": "The exact place where the user lives or will stay. Accept any user-provided text.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["name", "phone_number", "place"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    user_details = json.loads(result)
    user_details["phone_number"] = phone_number

    return user_details


def extract_food_order_details(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that processes food orders. The user will provide a product number, name, "
                    "and optionally the quantity in their input. You need to return a JSON object containing one key: "
                    "'selected_items'. "
                    "1. 'selected_items' should be an array of objects, where each object has 'number' (item number) "
                    "and 'quantity' (default is 1). "
                    "2. If a product number is repeated in the input, treat it as a separate instance with its own quantity. "
                    "Example: For the input '2 2 4 7', the output should be: "
                    "{'selected_items': [{'number': 2, 'quantity': 2}, {'number': 4, 'quantity': 1}, {'number': 7, 'quantity': 1}]}. "
                    "3. The input may include typos, and you should account for similar words (e.g., 'Syrniki', 'Блинчики'). "
                    "Analyze and match product names or numbers accurately. "
                    "You should handle input in both English and Russian, account for typos, and match product names "
                    "or numbers accurately. "
                    "Do not treat 'pickup' or 'self-pickup' as a cancellation request. "
                    "Example input: '1', '3', 'Syrniki 2 psc', 'Блинчики', 'Вок с курицей 2 шт', 'Burger 6', '1 Syrniki and 3 Borscht'. "
                    "Menu: "
                    "1. Syrniki with sour cream (3 pcs) — 10₾, "
                    "2. Pancakes with sour cream (3 pcs) — 10₾, "
                    "3. Rice-milk porridge + jam — 10₾, "
                    "4. “FastTrack” Sandwich (2 pcs) — 5₾, "
                    "5. Borscht soup (beef) — 10₾, "
                    "6. “Junior” Burger (beef) — 15₾, "
                    "7. “KurCheese” Burger — 20₾, "
                    "8. “BeefCheese” Burger (beef) — 25₾, "
                    "9. Spaghetti Carbonara — 15₾, "
                    "10. Chicken Wok — 15₾, "
                    "11. Vegetable Wok — 15₾, "
                    "12. Rice Wok with beef — 20₾, "
                    "13. Water 0.5 L — 2.5₾, "
                    "14. Cola 0.5 L — 5₾, "
                    "15. Quince juice 1 L — 10₾, "
                    "16. 100% Grape juice 1 L — 15₾, "
                    "17. Freshly squeezed apple juice 0.5 L — 20₾, "
                    "18. Americano (350 ml) — 5₾, "
                    "19. Cappuccino (350 ml) — 7.5₾, "
                    "20. Latte (350 ml) — 10₾, "
                    "21. Glace (350 ml) — 10₾"
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "order_details_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_items": {
                            "description": "An array of selected items, each containing the item number and quantity.",
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "number": {
                                        "description": "The product number as specified in the menu.",
                                        "type": "integer"
                                    },
                                    "quantity": {
                                        "description": "The quantity of the selected item. Defaults to 1 if not provided.",
                                        "type": "integer"
                                    }
                                },
                                "required": ["number", "quantity"]
                            }
                        },
                        **default_properties
                    },
                    "required": ["selected_items"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def detect_delivery_or_pickup(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that determines if the user's input refers to 'delivery' or 'pickup'. "
                    "The user might input their choice in English ('delivery', 'pickup') or Russian ('доставка', 'самовывоз'). "
                    "If the input indicates delivery, respond with 'delivery'. If it indicates pickup, respond with 'pickup'. "
                    "For any other input or if it is unclear, respond with 'None'. "
                    "Only return a JSON object containing the key 'choice' with one of the following values: "
                    "'delivery', 'pickup', or 'None'."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_choice_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "choice": {
                            "description": "The user's choice between delivery, pickup, or None if unclear.",
                            "type": "string",
                            "enum": ["delivery", "pickup", "null"]
                        }
                    },
                    "required": ["choice"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)['choice']


def extract_user_details_for_food_order(user_input):
    phone_pattern = r"\+?\d{1,3}[-\s]?\(?\d{1,5}\)?[-\s]?[\d\s\-]{6,13}"

    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0).strip() if match else 'None'

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts details from the user's input. "
                    "The user must answer three questions: "
                    "1. What is the name/number of your house? "
                    "2. What is your apartment number? "
                    "3. What is your phone number? "
                    "You must extract the following keys: "
                    "- 'house_name': the name/number of the house, or 'None' if not provided or invalid. "
                    "- 'apartment': the number of the apartment, or 'None' if not provided or invalid. "
                    "- 'phone_number': the phone number, or 'None' if it is not in a valid international format. "
                    "Accept answers in both English and Russian. Return 'None' for any missing or unclear values. "
                    "The result must be returned as a JSON object with the keys 'house_name', 'apartment', and 'phone_number'."
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_user_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "house_name": {
                            "description": "The name of the house provided by the user.",
                            "type": ["string", "null"]
                        },
                        "apartment": {
                            "description": "The apartment number provided by the user.",
                            "type": ["string", "null"]
                        },
                        "phone_number": {
                            "description": "The phone number provided by the user in valid international format.",
                            "type": ["string", "null"]
                        }, **default_properties
                    },
                    "required": ["house_name", "apartment", "phone_number"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    user_details = json.loads(result)
    user_details["phone_number"] = phone_number

    return user_details


def analyze_answer_yes_no(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You classify a response based on the user's input as 'yes', 'confirm', 'no', or 'none'. "
                    "If the user response includes any affirmative words like 'yes', 'yeah', 'confirm', 'sure', 'ok', etc., return true. "
                    "If the response includes any negative words like 'no', 'nope', 'nah', 'cancel', 'again', 'заново', etc., return false. "
                    "If the response does not contain any of these, return null (none)."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "yes_no_answer_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "description": "True if the user said yes, False if the user said no, or None if no answer was given.",
                            "type": ["boolean", "null"]
                        },
                        **default_properties
                    },
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_booking_details_for_massage(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты помощник, который извлекает данные для бронирования массажа. "
                    "Пользователь отвечает на вопросы строго по столбикам в следующем порядке: "
                    "1. На какие даты вас записать? "
                    "2. Время начала занятия? "
                    "Твоя задача: проанализировать текст и извлечь ответы на каждый из вопросов. "
                    "Верни JSON-объект с ключами: 'date' и 'time'. "
                    "Примеры ввода: "
                    "- 8 января\n10 10 "
                    "- 4 января\n12 30 "
                    "- 4.01\n12 30 "
                    "- 4 января, 12 00 "
                    "- 8 января в 10 "
                    "- 8.12 10.00 "
                    "Примечания: "
                    "1. 'date' должен содержать дату в формате DD/MM или 'None', если дата не указана. "
                    "2. 'time' должен содержать время в формате HH:MM или 'None', если не указано."
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_booking_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "description": "Дата в формате DD/MM или 'None', если дата не указана.",
                            "type": ["string", "null"]
                        },
                        "time": {
                            "description": "Время в формате HH:MM или 'None', если не указано.",
                            "type": ["string", "null"]
                        }
                    },
                    "required": ["date", "time"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)

def extract_massage_details(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts massage details from user input. "
                    "The user can choose from the following types of massage: "
                    "1. Расслабляющий 1ч/1.5ч "
                    "2. Классический 1ч/1.5ч "
                    "3. Спортивный 1ч/1.5ч "
                    "4. Лечебный 1.5ч/2ч "
                    "5. Балийский массаж 1ч/1.5ч "
                    "6. Антицеллюлитный 1ч/1.5ч "
                    "7. Спина + ноги 1ч/1.5ч. "
                    "You will analyze the input and return a JSON object with the keys 'massage_type' and 'duration'. "
                    "The 'massage_type' should be one of the available types: "
                    "['relaxing', 'classic', 'sports', 'therapeutic_session', 'balinese', 'anti_cellulite', 'back_and_legs'], "
                    "or 'undefined' if it's not specified correctly. "
                    "The 'duration' should be one of the available durations (1, 1.5, or 2), or 'None' if not specified. "
                    "Example input: 'Лечебный 2ч', 'Расслабляющий 1', 'Anti Cellulite\n1h', 'Back and legs\n1'."
                )
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "get_massage_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "massage_type": {
                            "description": "The type of massage requested by the user, or 'undefined' if not provided.",
                            "type": "string",
                            "enum": ["relaxing", "classic", "sports", "therapeutic_session", "balinese", "anti_cellulite", "back_and_legs", "undefined"]
                        },
                        "duration": {
                            "description": "The duration of the massage requested (1h or 1.5h or 2h), or 'None' if not provided.",
                            "type": "number",
                            "enum": [1, 1.5, 2]
                        },
                        **default_properties
                    },
                    "required": ["massage_type", "duration"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


default_properties = {
    "is_request_canceled": {
        "description": "True if the response contains a cancellation request or 'menu'/'меню' command in any register, otherwise False.",
        "type": "boolean"
    },
}

# x = extract_massage_details('Расслабляющий 1ч')
# x = extract_booking_details_for_massage('35.01 12 00')
x = extract_rental_equipment_details('1 2 3')
print(x)

# x = detect_delivery_or_pickup('1 2 3 4')
# print(extract_mentor_booking_details('2 взрослых 4 января 12.30 Сноуборд, 10-20 лет'))
# print(extract_mentor_booking_details('8 января\n10 10\nЛыжи\n1 ребенок\n10 лет'))
# print(extract_food_order_details('2 2 2 4 7'))
# print(extract_mentor_booking_details('8 января, санки, 3 котика'))
# print(extract_user_details('Даниил +48572779167'))

# print(extract_order_details("1, 2 и 19"))
# print(extract_rental_equipment_details("1. Мне нужен шлем, перчатки\n2. Куртка"))
# print(analyze_answer_yes_no("Чего"))
# print(extract_booking_details('16 января, 14:00, лыжи, 1 взрослый'))
# print(determine_service('1'))
# print(determine_service('Я хочу массаж'))
