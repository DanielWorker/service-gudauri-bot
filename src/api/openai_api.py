import json
import re

from openai import OpenAI

# import src.settings as stg
# client = OpenAI(api_key=stg.OPENAI_API_KEY)

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)


def determine_language(text):
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
                    "You are an assistant that extracts booking details from user input. "
                    "The user must answer three questions about their booking: "
                    "1. What date and time should we book for you? "
                    "2. What equipment will you use? Only 'Snowboard' or 'Skis' (including Russian terms and typos) are acceptable answers. "
                    "Return 'None' if the equipment is anything else. Return what the user wrote if the answer is fitting. "
                    "3. Would you prefer a group lesson for adults or an individual lesson for a child? "
                    "Acceptable answers are: 'lesson for adults', 'lesson for a child', '1 adult', '2 adults', '1 child', '2 children'. "
                    "Return 'None' if the answer is unclear or does not match these options. "
                    "You will analyze the input and return a JSON object with three keys: 'date_time', 'equipment', and 'lesson_preference'. "
                    "Each key should contain the exact text that the user sent as a response. If any of the answers are missing or unclear, return 'None' for that key. "
                    "The input may be in English or Russian and may contain typos."
                    "Examples:"
                    "1. January 8th, 10:10\n"
                    "2. Skis\n"
                    "3. 1 child\n"
                    "January 4th, 12:30 "
                    "Snowboard "
                    "2 adults "
                    "10 января лыжи 1 ребенок"
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
                        "date_time": {
                            "description": "The exact date and time for the booking, or 'None' if not provided.",
                            "type": ["string", "null"]
                        },
                        "equipment": {
                            "description": "The exact equipment to be used ('Snowboard' or 'Skis' only), or 'None' if not provided or invalid.",
                            "type": ["string", "null"]
                        },
                        "lesson_preference": {
                            "description": "The exact lesson preference ('lesson for adults', 'lesson for a child', '1 adult', "
                                           "'2 adults', '1 child', '2 children' only), or 'None' if not provided or invalid.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["date_time", "equipment", "lesson_preference"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


def extract_user_details(user_input):
    # Регулярное выражение для поиска международного номера телефона
    phone_pattern = r"(\+?[0-9]{1,3}[ -]?)?(\(?\d{1,5}\)?[ -]?)?[\d\s\-]{6,13}"

    # Поиск телефона с помощью регулярного выражения
    match = re.search(phone_pattern, user_input)
    phone_number = match.group(0) if match else 'None'

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
                    "You should extract a valid name, a valid phone number, and a valid place in Georgia related to Gudauri. "
                    # "The acceptable places are: 'New Gudauri', 'Upper Gudauri', 'Lower Gudauri', 'Club 2100', 'Gudauri Lodge', 'Hills', 'Roshka', 'Gogi', or any mention of 'Gudauri'. "
                    "If the name is unclear or not valid (like only a single letter), return 'None'."
                    "For phone numbers, return 'None' if it doesn't follow international format.  "
                    "If any of the answers are missing or unclear, return 'None' for that key. "
                    "You will return a JSON object with three keys: 'name', 'phone_number', and 'place'. "
                    "Each key should contain the exact text that the user sent as a response if it matches the valid criteria. "
                    "Examples: "
                    "1. John Doe "
                    "2. +995123456789 "
                    "3. New Gudauri "
                    "or "
                    "Иван Иванов "
                    "+995912345678 "
                    "Рошка "
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
                            "description": "The exact phone number provided by the user, or 'None' if not provided or invalid. The phone number should follow a valid international format. It could look like +1234567890",
                            "type": ["string", "null"]
                        },
                        "place": {
                            "description": "The exact place where the user lives or will stay (must be a valid place related to Gudauri or Georgia, or any mention of 'Gudauri'), or 'None' if not provided or invalid.",
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
                    "and optionally the quantity in their input. You need to return a JSON object containing two keys: "
                    "'selected_items' and 'total_price'. "
                    "1. 'selected_items' should be an array of objects, where each object has 'number' (item number) "
                    "and 'quantity' (default is 1). "
                    "2. 'total_price' should be the sum of the prices of all selected items. "
                    "3. If a product number is repeated in the input, treat it as a separate instance with its own quantity. "
                    "Example: For the input '2 2 4 7', the output should be: "
                    "{'selected_items': [{'number': 2, 'quantity': 2}, {'number': 4, 'quantity': 1}, {'number': 7, 'quantity': 1}], 'total_price': 45}. "
                    "4. The input may include typos, and you should account for similar words (e.g., 'Syrniki', 'Блинчики'). "
                    "Analyze and match product names or numbers accurately. "
                    "You should handle input in both English and Russian, account for typos, and match product names "
                    "or numbers accurately. "
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
                        "total_price": {
                            "description": "The total price of all selected items in the order. This can be a fractional value.",
                            "type": "number"
                        },
                        **default_properties
                    },
                    "required": ["selected_items", "total_price"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = response.choices[0].message.content
    return json.loads(result)


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


default_properties = {
    "is_request_canceled": {
        "description": "True if the response contains a cancellation request, otherwise False.",
        "type": "boolean"
    },
}

# print(extract_mentor_booking_details('2 взрослых 4 января 12.30 Сноуборд'))
# print(extract_food_order_details('2 2 2 4 7'))
# print(extract_mentor_booking_details('8 января, санки, 3 котика'))
# print(extract_user_details('Даниил +48572779167'))

# print(extract_order_details("1, 2 и 19"))
# print(extract_rental_equipment_details("1. Мне нужен шлем, перчатки\n2. Куртка"))
# print(analyze_answer_yes_no("Чего"))
# print(extract_booking_details('16 января, 14:00, лыжи, 1 взрослый'))
# print(determine_service('1'))
# print(determine_service('Я хочу массаж'))