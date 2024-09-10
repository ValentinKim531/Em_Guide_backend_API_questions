from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class RegistrationQuestions(Enum):
    QUESTION_1 = {
        "text": "Произнесите голосом (либо напишите текстовым сообщением) вашу Фамилию, Имя и дату рождения (число, месяц ,год).",
        "options": [],
        "is_custom_option_allowed": True,
    }
    QUESTION_2 = {
        "text": "Пожалуйста, сообщите, имеется ли у вас менструальный цикл?",
        "options": ["Да", "Нет"],
        "is_custom_option_allowed": False,
    }
    QUESTION_3 = {
        "text": "Назовите вашу страну и город проживания.",
        "options": [],
        "is_custom_option_allowed": True,
    }
    QUESTION_4 = {
        "text": "Принимаете ли вы какой-либо препарат для купирования приступа головной боли? Если “Да”, то какой?",
        "options": ["Да", "Нет"],
        "is_custom_option_allowed": True,
    }
    QUESTION_5 = {
        "text": "Принимаете ли вы какой-либо препарат на постоянной основе для лечения хронической головной боли?",
        "options": ["Да", "Нет"],
        "is_custom_option_allowed": True,
    }

class DailySurveyQuestions(Enum):
    QUESTION_1 = {
        "text": "Пожалуйста, произнесите голосом или напишите текстовым сообщением ваш ответ на мой вопрос: У вас сегодня болела голова и если ответ положительный, то принимали ли вы какие либо медикаменты для купирования приступа головной боли и какие, если принимали?",
        "options": ["Да", "Нет"],
        "is_custom_option_allowed": True,
    }
    QUESTION_2 = {
        "text": "Пожалуйста, произнесите голосом или укажите, насколько интенсивной была головная боль?",
        "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "is_custom_option_allowed": False,
    }
    QUESTION_3 = {
        "text": "В какой области болела голова?",
        "options": ["висок", "теменная область", "бровь", "глаз", "верхняя челюсть", "нижняя челюсть", "лоб", "затылок"],
        "is_custom_option_allowed": True,
    }
    QUESTION_4 = {
        "text": "С какой стороны: с одной или с двух сторон, справа или слева?",
        "options": ["с одной стороны справа", "с одной стороны слева", "с двух сторон"],
        "is_custom_option_allowed": True,
    }
    QUESTION_5 = {
        "text": "Какой был характер головной боли?",
        "options": ["давящая", "пульсирующая", "сжимающая", "ноющая", "ощущение прострела", "режущая", "тупая", "пронизывающая", "острая", "жгучая"],
        "is_custom_option_allowed": True,
    }

# Маршрут для получения всех вопросов по регистрации
@app.get("/registration_questions")
async def get_registration_questions():
    return {question.name: question.value for question in RegistrationQuestions}

# Маршрут для получения всех вопросов для ежедневного опроса
@app.get("/daily_survey_questions")
async def get_daily_survey_questions():
    return {question.name: question.value for question in DailySurveyQuestions}
