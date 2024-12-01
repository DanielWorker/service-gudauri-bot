import json

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
                    "However, the input may contain typos or similar words (e.g., 'Rusky', 'Englesh'). "
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
                    "2. What equipment will you use? "
                    "3. Would you prefer a group lesson for adults or an individual lesson for a child? "
                    "You will analyze the input and return a JSON object with three keys: "
                    "'date_time', 'equipment', and 'lesson_preference'. "
                    "Each key should have the exact text that the user sent as a response. "
                    "If any of the answers are missing or unclear, return 'None' for that key."
                    "Examples:"
                    "1. January 8th, 10:10"
                    "2. Skis"
                    "3. 1 child"
                    "1. January 4th, 12:30"
                    "2. Snowboard"
                    "3. 2 adults"
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
                            "description": "The exact equipment to be used, or 'None' if not provided.",
                            "type": ["string", "null"]
                        },
                        "lesson_preference": {
                            "description": "The exact lesson preference, or 'None' if not provided.",
                            "type": ["string", "null"]
                        },
                        **default_properties
                    },
                    "required": ["date_time", "equipment", "lesson_preference", "is_request_canceled"],
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
                    "You classify a response based on the user's input as 'yes', 'no', or 'none'. "
                    "If the user response includes any affirmative words like 'yes', 'yeah', 'sure', 'ok', etc., return true. "
                    "If the response includes any negative words like 'no', 'nope', 'nah', etc., return false. "
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
    "is_question": {
        "description": "True if the response is a question, otherwise False.",
        "type": "boolean"
    },
    "is_request_canceled": {
        "description": "True if the response contains a cancellation request, otherwise False.",
        "type": "boolean"
    },
}

print(extract_rental_equipment_details("1. Мне нужен шлем, перчатки\n2. Куртка"))


# print(analyze_answer_yes_no("Чего"))
# print(extract_booking_details('16 января, 14:00, лыжи, 1 взрослый'))
# print(determine_service('1'))
# print(determine_service('Я хочу массаж'))