from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

questions_data = {
    "daily_questions": [
        {
            "index": 1,
            "question": {
                "text": "У вас сегодня болела голова?",
                "options": [
                    "Да",
                    "Нет"
                ],
                "is_custom_option_allowed": False
            }
        },
        {
            "index": 2,
            "question": {
                "text": "Принимали ли вы какие-либо медикаменты для купирования приступа головной боли и какие, если принимали?",
                "options": [
                    "Да, принимал",
                    "Нет, не принимал",
                ],
                "is_custom_option_allowed": True
            }
        },
        {
            "index": 3,
            "question": {
                "text": "Насколько интенсивной была головная боль?",
                "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                "is_custom_option_allowed": False
            }
        },
        {
            "index": 4,
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
            "index": 5,
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
            "index": 6,
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
