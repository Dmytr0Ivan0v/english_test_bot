from get_questions import get_questions


class Test:

    question_list = get_questions()

    user_answers = ""
    counter_for_email = -1
    question_counter = 0
    count_right_answers = 0
    counter = 0
    counter_for_answers = -1
    questions_left: int = len(question_list)  # number of questions
    current_item = question_list[counter]  # {question: answer} position
    current_question = list(current_item.keys())[0]
    item_for_r_answer = question_list[counter_for_answers]
    right_answer = list(item_for_r_answer.values())[0]
    user_level = "A1 - Elementary"

    def change_counter(self):
        self.counter += 1
        self.current_item = self.question_list[self.counter]
        self.current_question = list(self.current_item.keys())[0]

    def change_right_answer(self):
        self.question_counter += 1
        self.counter_for_answers += 1
        self.item_for_r_answer = self.question_list[self.counter_for_answers]
        self.right_answer = list(self.item_for_r_answer.values())[0]

    def add_user_answers(self, answer):
        mark = "\U00002705" * 5
        if answer != self.right_answer:
            mark = "\U0000274C" * 5
        if answer in ("A", "B", "C", "D", "I don't know, skip", "Не знаю, пропустити"):
            self.user_answers += f"{mark} {answer}\n\n"
        self.user_answers += f"{self.current_question}\n"
        print(self.user_answers)  # for chacking

    def restart(self):
        self.counter_for_email = -1
        self.question_counter = 0
        self.count_right_answers = 0
        self.counter = 0
        self.counter_for_answers = -1
        self.questions_left: int = len(self.question_list)
        self.current_item = self.question_list[self.counter]
        self.current_question = list(self.current_item.keys())[0]
        self.item_for_r_answer = self.question_list[self.counter_for_answers]
        self.right_answer = list(self.item_for_r_answer.values())[0]
