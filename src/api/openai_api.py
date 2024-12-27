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
    response_equipment = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    # "You are an assistant that extracts rental equipment details from user input. "
                    # "The user can provide either equipment numbers or item names and optionally quantities. "
                    "You are an assistant that processes rental equipment orders. The user will provide a equipment number, name, "
                    "and optionally the quantity in their input. You need to return a JSON object containing one key: "
                    "'selected_items'. "
                    "1. 'selected_items' should be an array of objects, where each object has 'number' (item number) "
                    "and 'quantity' (default is 1). "
                    "2. If a equipment number is repeated in the input, treat it as a separate instance with its own quantity. "
                    "Example: For the input '2 2 4 7', the output should be: "
                    "{'selected_items': [{'number': 2, 'quantity': 2}, {'number': 4, 'quantity': 1}, {'number': 7, 'quantity': 1}]}. "
                    "3. The input may include typos, and you should account for similar words. "
                    "Analyze and match equipment names or numbers accurately. "
                    "You should handle input in both English and Russian, account for typos, and match product names. "
                    "4. You should prioritize identifying equipment items and ignore any references to time periods (e.g., '2 days' or '16.01 - 18.01'). "
                    "Rental equipment options include: "
                    "1. Ski Set: Skis, poles, boots, helmet "
                    "2. Snowboard set: Snowboard, boots, helmet "
                    "3. Clothes set: Jacket, pants, goggles. "
                    "Additional items: "
                    "4. Skis + poles / snowboard, "
                    "5. Goggles, "
                    "6. Helmet, "
                    "7. Gloves, "
                    "8. Protective shorts, "
                    "9. Jacket, "
                    "10. Pants. "
                    "You need to return a JSON object with a key 'selected_items' containing an array of objects, "
                    "each with 'number' (the equipment number) and 'quantity' (default is 1). "
                    "If the user mentions equipment by name, match it to the correct number. "
                    "If no equipment is mentioned or it's unclear, return empty array. "
                    "For example, '1 2 1 4' or 'skis, helmet, gloves'. "
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
                "name": "get_rental_equipment_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_items": {
                            "description": "An array of selected items with their number and quantity.",
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "number": {
                                        "description": "The number of the selected equipment item.",
                                        "type": "integer"
                                    },
                                    "quantity": {
                                        "description": "The quantity of the selected item (defaults to 1 if not provided).",
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

    response_rental_period = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts rental period or dates from user input. "
                    "The user may provide information about the rental period in terms of days, or specific dates. "
                    "You should extract this information and return it in a format such as 'X days' or 'from date to date'. "
                    "If no clear rental period or dates are mentioned, return 'None'. "
                    "Examples: '3 days', '16.01 - 18.01', '1 сутки', '2 суток', '3 дня', '20.01 25.01', '1 января - 3 января', 'Jan 2 - Kan 6', '1 декабря'."
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
                "name": "get_rental_period",
                "schema": {
                    "type": "object",
                    "properties": {
                        "rental_period": {
                            "description": "The rental period or dates mentioned by the user, or 'None' if not provided.",
                            "type": "string"
                        },
                    },
                    "required": ["rental_period"],
                    "additionalProperties": False
                }
            }
        }
    )

    rental_period_result = response_rental_period.choices[0].message.content
    rental_period_data = json.loads(rental_period_result)

    equipment_result = response_equipment.choices[0].message.content
    equipment_data = json.loads(equipment_result)

    result = {**rental_period_data, **equipment_data}
    return result


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
    phone_pattern = r"\+?\d{1,3}[-\s]?\(?\d{1,5}\)?[-\s]?[\d\s\-]{6,13}"

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


def extract_selected_paragliding_plan(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts the user's selected plan from the input. "
                    "The user has two options to choose from: "
                    "1. Standard 15-20 minutes 350₾ "
                    "2. Levitation Pro 35-40 minutes 500₾. "
                    "The user may respond in either Russian or English. "
                    "You need to analyze the input and return a JSON object with a key 'selected_plan' "
                    "containing the exact text that the user mentioned. "
                    "If the user's choice is unclear or not one of the options, return 'None'. "
                    "Examples of valid inputs: "
                    "'Standard', "
                    "'Стандарт', "
                    "'1', "
                    "'Levitation Pro'. "
                    "'Левитация Про'. "
                    "'2'. "
                    "Examples of invalid inputs: "
                    "'Any plan', or no clear option specified."
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
                "name": "get_selected_plan",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_plan": {
                            "description": "The exact plan chosen by the user, or 'None' if unclear or not provided.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["selected_plan"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_user_info(user_input):
    phone_pattern = r"\+?\d{1,3}[-\s]?\(?\d{1,5}\)?[-\s]?[\d\s\-]{6,13}"

    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0).strip() if match else 'None'

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты помощник, который извлекает данные пользователя и информацию для бронирования. "
                    "Пользователь может предоставить следующие данные: "
                    "1. Дату бронирования. "
                    "2. Время бронирования"
                    "3. Имя пользователя. "
                    "4. Номер телефона. "
                    "You should extract a valid name, a valid phone number, a valid date and time. "
                    "If the name is unclear or not valid (like only a single letter), return 'None'. "
                    "For phone numbers, return 'None' if it doesn't follow international format. "
                    "If any of the answers are missing or unclear, return 'None' for that key. "
                    "Твоя задача: извлечь имя, номер телефона, дату и время. "
                    "Дата должна быть в формате DD/MM или 'None', если не указана. "
                    "Время должно быть в формате HH:MM или 'None', если не указано. "
                    "Response can be retrieved in English and with typos"
                    "Примеры: "
                    "- '8 января, 10.00, Иван, +995123456789' "
                    "- 'Иван' "
                    "- '+995123456789' "
                    "- '8 января' "
                    "- '10:00'."
                    # "- '8 января, 10.00, Иван, +995123456789' "
                    # "- 'Jan 6, 12 00, Leo, +995123456732' "
                    # "- '+487561236532, Алексей, 8.01, 14:00' "
                    # "- 'Dec 29\n10:00\nМария\n995123456789' "
                    # "- 'Dec 29' "
                    # "- '10:00' "
                    # "- '10.00' "
                    # "- 'Мария' "
                    # "- '995123456789'. "
                    "Верни результат в формате JSON с ключами 'date', 'time', 'name', 'phone_number'."
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
                "name": "get_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "description": "Дата записи в формате DD/MM или 'None', если не указана.",
                            "type": ["string", "null"]
                        },
                        "time": {
                            "description": "Время записи в формате HH:MM или 'None', если не указано.",
                            "type": ["string", "null"]
                        },
                        "name": {
                            "description": "Имя пользователя, или 'None', если имя не указано или некорректно.",
                            "type": ["string", "null"]
                        },
                        "phone_number": {
                            "description": "Номер телефона в международном формате, или 'None', если номер не указан или некорректен.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["name", "phone_number", "date", "time"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    extracted_details = json.loads(result)
    extracted_details["phone_number"] = phone_number

    return extracted_details


def extract_selected_snowmobile_tour(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Вы — помощник, который извлекает выбранный пользователем тур на снегоходе из его ввода. "
                    "Пользователь может выбрать один из двух туров: "
                    "1. 1 человек (4 км круг) - 150₾ "
                    "2. 2 человека (4 км круг) - 250₾. "
                    "Ответ пользователя может быть как на русском, так и на английском языке. "
                    "The user response can be either in Russian or in English. "
                    "Вам нужно проанализировать ввод и вернуть объект JSON с ключом 'selected_tour', "
                    "который будет содержать точный текст, указанный пользователем. "
                    "Если выбор пользователя неясен или не соответствует одной из предложенных опций, верните 'None'. "
                    "Примеры корректных вариантов ввода: "
                    "- '1 человек (4 км круг)', "
                    "- '2 человека (4 км круг)' "
                    "- '1 person' "
                    "- '2 peoples' "
                    "- '1', "
                    "- '2', "
                    "Примеры некорректных вариантов ввода: "
                    "'Любой тур', или нет четкого указания опции."
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
                "name": "get_selected_tour",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_tour": {
                            "description": "The exact tour chosen by the user, or 'None' if unclear or not provided.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["selected_tour"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_exchange_info(user_input):
    # Шаблон для поиска номера телефона
    phone_pattern = r"\+?\d{1,3}[-\s]?\(?\d{1,5}\)?[-\s]?[\d\s\-]{6,13}"

    # Извлечение номера телефона
    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0).strip() if match else 'None'

    # GPT запрос
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts user information for an exchange request. "
                    "The user may provide the following details in either Russian or English: "
                    "1. The amount in dollars they want to exchange (e.g., '100$', 'сто долларов', '400'). "
                    "2. The date of their visit (e.g., '8 January', '8 января'). "
                    "3. The time of their visit (e.g., '10:00', '10 утра'). "
                    "4. Their name (e.g., 'John', 'Иван'). "
                    "5. Their phone number in international format (e.g., '+995123456789'). "
                    "You must extract this information and return it in JSON format. "
                    "If any of the data is missing or unclear, return 'None' for that key. "
                    "Make sure to handle both Russian and English inputs. "
                    "Examples: "
                    "- '400\n4 января\n12.56\nЯрослав\n+995123456789', "
                    "- '400, 4 января, 12.56, Ярослав, +995123456789', "
                    "- '1. 400\n2. 4 января\n3. 12.56\n4. Ярослав\n5. +995123456789', "
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
                "name": "get_selected_tour",
                "schema": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "description": "The amount to exchange in dollars or 'None' if not specified.",
                            "type": ["number", "null"]
                        },
                        "date": {
                            "description": "The visit date in DD/MM format or 'None' if not specified.",
                            "type": ["string", "null"]
                        },
                        "time": {
                            "description": "The visit time in HH:MM format or 'None' if not specified.",
                            "type": ["string", "null"]
                        },
                        "name": {
                            "description": "The user's name or 'None' if not specified or invalid.",
                            "type": ["string", "null"]
                        },
                        "phone_number": {
                            "description": "The phone number in international format or 'None' if not specified or invalid.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["amount", "date", "time", "name", "phone_number"],
                    "additionalProperties": False
                }
            },
        }
    )

    # Обработка ответа
    result = response.choices[0].message.content
    extracted_details = json.loads(result)

    # Добавляем телефон, если он был найден
    extracted_details["phone_number"] = phone_number

    return extracted_details


def extract_selected_ski_service(user_input, lang):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that extracts the service chosen by the user from their input. "
                    "The user can choose one of the following services: "
                    "1. Edge sharpening + waxing "
                    "2. Base repair. "
                    "Или на русском"
                    "1. Заточка кантов + парафин "
                    "2. Ремонт скользящей поверхности. "
                    "The user response can be either in Russian or in English. "
                    f"Return response in the following language: {lang}. "
                    "You need to analyze the input and return a JSON object with the key 'selected_service' "
                    "which will contain the exact service chosen by the user. "
                    "If the user's choice is unclear or does not match one of the offered options, return 'None'. "
                    
                    "Examples of valid inputs: "
                    "- 'Edge sharpening + waxing', "
                    "- 'Sliding surface repair', "
                    "- 'Заточка кантов + парафин', "
                    "- 'Ремонт скользящей поверхности', "
                    "- '1', "
                    "- '2', "
                    "- 'Sharpening and waxing', "
                    "- 'Repair'. "
                    "Examples of invalid inputs: "
                    "'Any service', or no clear indication of the option."
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
                "name": "get_selected_service",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_service": {
                            "description": "The exact service chosen by the user, or 'None' if unclear or not provided.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["selected_service"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_selected_cleaning_service(user_input, lang):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Вы — помощник, который извлекает выбранную пользователем услугу уборки из его ввода. "
                    "Пользователь может выбрать одну из следующих услуг: "
                    "1. Уборка Студия "
                    "2. Уборка Студия генеральная "
                    "3. Уборка в Квартире больше 30м2 "
                    "4. Квартира > 30м2 генеральная уборка "
                    "5. Квартира больше 60м2 "
                    "6. Квартира > 60м2 генеральная "
                    "Or in English: "
                    "1. Studio Cleaning"
                    "2.	Studio Deep Cleaning"
                    "3.	Apartment Cleaning (over 30m²)"
                    "4.	Apartment Deep Cleaning (over 30m²)"
                    "5.	Apartment Cleaning (over 60m²)"
                    "6.	Apartment Deep Cleaning (over 60m²)"
                    "Ответ пользователя может быть на русском или английском языке. "
                    "The user response can be either in Russian or in English. "
                    f"Return response in the following language: {lang}. "
                    "Вам нужно проанализировать ввод и вернуть объект JSON с ключом 'selected_service', "
                    "который будет содержать точный текст, указанный пользователем. "
                    "Если выбор пользователя неясен или не соответствует одной из предложенных опций, верните 'None'. "
                    "Примеры корректных вариантов ввода: "
                    "- 'Уборка Студия' "
                    "- 'Studio Cleaning' "
                    "- 'Квартира > 30м2 генеральная' "
                    "- 'Flat > 30m2 general cleaning' "
                    "- '1' "
                    "- '2', и так далее "
                    "Примеры некорректных вариантов ввода: "
                    "'Любая уборка', или нет четкого указания опции."
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
                "name": "get_selected_service",
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_service": {
                            "description": "The exact cleaning service chosen by the user, or 'None' if unclear or not provided.",
                            "type": ["string", "null"]
                        }
                    },
                    "required": ["selected_service"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_cleaning_appointment_info(user_input):
    phone_pattern = r"\+?\d{1,3}[-\s]?\(?\d{1,5}\)?[-\s]?[\d\s\-]{6,13}"

    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0).strip() if match else 'None'

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты помощник, который извлекает данные пользователя для записи на уборку. "
                    "Пользователь может предоставить следующие данные: "
                    "1. Дата записи. "
                    "2. Дом или корпус. "
                    "3. Номер апартаментов. "
                    "4. Имя пользователя. "
                    "5. Номер телефона. "
                    "Твоя задача: извлечь эти данные и вернуть их в формате JSON. "
                    "Если пользователь не указал какой-то из пунктов, верни 'None' для этого ключа. "
                    "Response can be retrieved in English or Russian. "
                    "Примеры: "
                    "- '4 января, корпус А, апартаменты 123, Иван, +995551234567' "
                    "- '5/01, дом Б, квартира 45, Анна, +487651234567' "
                    "- '5 January, Block C, Apartment 78, John, +1234567890'. "
                    "- '4 января\nF4\n323\nСаша\n+995551234567'. "
                    "Верни результат в формате JSON с ключами 'date', 'building', 'apartment', 'name', 'phone_number'."
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
                "name": "get_cleaning_details",
                "schema": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "description": "Дата записи в формате DD/MM или 'None', если не указана.",
                            "type": ["string", "null"]
                        },
                        "building": {
                            "description": "Название дома/корпуса, или 'None', если не указано.",
                            "type": ["string", "null"]
                        },
                        "apartment": {
                            "description": "Номер апартаментов, или 'None', если не указан.",
                            "type": ["string", "null"]
                        },
                        "name": {
                            "description": "Имя пользователя, или 'None', если не указано или некорректно.",
                            "type": ["string", "null"]
                        },
                        "phone_number": {
                            "description": "Номер телефона в международном формате, или 'None', если номер не указан или некорректен.",
                            "type": ["string", "null"]
                        }
                    },
                    "required": ["date", "building", "apartment", "name", "phone_number"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    extracted_details = json.loads(result)
    extracted_details["phone_number"] = phone_number

    return extracted_details


default_properties = {
    "is_request_canceled": {
        "description": "True if the response contains a cancellation request or 'menu'/'меню' command in any register, otherwise False.",
        "type": "boolean"
    },
}

# x = extract_selected_snowmobile_tour('1 person')
# x = extract_rental_equipment_details('1 2 2 3 4')
x = extract_selected_cleaning_service('1', 'russian')
print(x)
