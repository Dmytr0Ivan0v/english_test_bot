from dataclasses import dataclass

# greeting section

greeting_start_ukr = "Привіт, "
greeting_end_ukr = "Я бот зі школи англійської мови CTRLSHIFT і я допоможу тобі визначити твій рівень англійської"
greeting_start_eng = "Hello, "
greeting_end_eng = (
    "I am a bot from CTRLSHIFT English school and I'll help you define your level"
)


# button section

button_lets_go_eng = "Let's go"
button_next_eng = "Next"
button_dont_know_eng = "I don't know, skip"
button_get_result_eng = "Get result"
button_result_to_teacher_eng = "Get result and feedback from the teacher"

button_lets_go_ukr = "Почати"
button_next_ukr = "Наступний"
button_dont_know_ukr = "Не знаю, пропустити"
button_get_result_ukr = "Отримати результат"
button_result_to_teacher_ukr = "Отримати результат та консультацію викладача"


# result section

question_result_eng = "Get result?"
result_eng = "Your result"
start_eng = "Press /start to repeat"

question_result_ukr = "Отримати результат?"
result_ukr = "Твій результат"
start_ukr = "Натисни /start щоб спробувати ще раз"


@dataclass
class TextLanguage:
    language: str = "English"
    greeting_start: str = greeting_start_eng
    greeting_end: str = greeting_end_eng
    button_lets_go: str = button_lets_go_eng
    button_next: str = button_next_eng
    button_i_dont_know: str = button_dont_know_eng
    button_get_result: str = button_get_result_eng
    question_result: str = question_result_eng
    result: str = result_eng
    result_to_teacher: str = button_result_to_teacher_eng
    start: str = start_eng

    @classmethod
    def choose_language(cls, user_lang) -> None:
        cls.language: str = user_lang
        if cls.language == "Українська":
            cls.greeting_start: str = greeting_start_ukr
            cls.greeting_end: str = greeting_end_ukr
            cls.button_lets_go: str = button_lets_go_ukr
            cls.button_next: str = button_next_ukr
            cls.button_i_dont_know: str = button_dont_know_ukr
            cls.button_get_result: str = button_get_result_ukr
            cls.question_result: str = question_result_ukr
            cls.result: str = result_ukr
            cls.result_to_teacher: str = button_result_to_teacher_ukr
            cls.start: str = start_ukr
