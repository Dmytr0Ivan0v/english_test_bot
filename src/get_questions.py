import sqlite3
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
DB_NAME = "questions.db"


def get_questions():
    connection = sqlite3.connect(ROOT_DIR / DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""SELECT * from questions""")
    data = cursor.fetchall()
    question_list = []
    for el in data:
        question = {}
        question[el[1].replace("\\", "\n")] = el[2]
        question_list.append(question)
    connection.close

    return question_list
