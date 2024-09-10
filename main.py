from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

questions_data = {
    "registration_questions": [
        {
            "index": 1,
            "question": {
                "text": "Произнесите голосом (либо напишите текстовым сообщением) вашу Фамилию, Имя и дату рождения (число, месяц, год).",
                "options": [],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 2,
            "question": {
                "text": "Пожалуйста, сообщите, имеется ли у вас менструальный цикл?",
                "options": ["Да", "Нет"],
                "is_custom_option_allowed": False
            }
        },
        {
            "index": 3,
            "question": {
                "text": "Назовите вашу страну и город проживания.",
                "options": [],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 4,
            "question": {
                "text": "Принимаете ли вы какой-либо препарат для купирования приступа головной боли? Если “Да”, то какой?",
                "options": ["Да", "Нет"],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 5,
            "question": {
                "text": "Принимаете ли вы какой-либо препарат на постоянной основе для лечения хронической головной боли?",
                "options": ["Да", "Нет"],
                "is_custom_option_allowed": True
            }
        }
    ],
    "daily_survey_questions": [
        {
            "index": 1,
            "question": {
                "text": "Пожалуйста, произнесите голосом или напишите текстовым сообщением ваш ответ на мой вопрос: У вас сегодня болела голова и если ответ положительный, то принимали ли вы какие-либо медикаменты для купирования приступа головной боли и какие, если принимали?",
                "options": ["Да", "Нет"],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 2,
            "question": {
                "text": "Пожалуйста, произнесите голосом или укажите, насколько интенсивной была головная боль?",
                "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                "is_custom_option_allowed": False
            }
        },
        {
            "index": 3,
            "question": {
                "text": "В какой области болела голова?",
                "options": [
                    "висок",
                    "теменная область",
                    "бровь",
                    "глаз",
                    "верхняя челюсть",
                    "нижняя челюсть",
                    "лоб",
                    "затылок"
                ],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 4,
            "question": {
                "text": "С какой стороны: с одной или с двух сторон, справа или слева?",
                "options": [
                    "с одной стороны справа",
                    "с одной стороны слева",
                    "с двух сторон"
                ],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 5,
            "question": {
                "text": "Какой был характер головной боли?",
                "options": [
                    "давящая",
                    "пульсирующая",
                    "сжимающая",
                    "ноющая",
                    "ощущение прострела",
                    "режущая",
                    "тупая",
                    "пронизывающая",
                    "острая",
                    "жгучая"
                ],
                "is_custom_option_allowed": True
            }
        }
    ]
}


@app.get("/get-questions")
async def get_questions():
    return JSONResponse(content=questions_data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082)
