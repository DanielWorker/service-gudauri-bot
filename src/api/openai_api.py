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
                    "'rent_sky_board', 'instructor', 'food_coffee', 'massage', 'transfer_taxi', 'paragliding', 'snowbike_tour', "
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
                                       "'rent_sky_board', 'instructor', 'food_coffee', 'massage', 'transfer_taxi', "
                                       "'paragliding', 'snowbike_tour', 'exchange', 'ski_service', 'photo_video', "
                                       "'cleaning', 'rent_flat', or 'undefined'.",
                        "type": "string",
                        "enum": [
                            "rent_sky_board", "instructor", "food_coffee", "massage", "transfer_taxi", "paragliding",
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


print(determine_service('1'))
print(determine_service('Я хочу массаж'))
