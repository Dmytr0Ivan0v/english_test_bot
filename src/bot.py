import test

import telebot
from dotenv import dotenv_values
from telebot import types

# import bot_email
import lenguages
from levels import UserLevel

config: dict = dotenv_values(".env")

TOKEN = str(config["TOKEN"])
TEACHER_CHAT_ID = int(config["TEACHER_CHAT_ID"])

bot = telebot.TeleBot(TOKEN)

CHATS = {"test_id": test.Test()}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(massage):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Українська")
    button2 = types.KeyboardButton("English")
    markup.add(button1, button2)
    greeting = "Оберіть мову спілкування"
    bot.send_message(massage.chat.id, greeting, reply_markup=markup)
    test_id = massage.chat.id
    CHATS.update({test_id: test.Test()})


@bot.message_handler(content_types=["text"])
def lets_go(message):
    if message.chat.type == "private" and message.chat.id in CHATS:
        if message.text in ["Українська", "English"]:
            CHATS[message.chat.id].restart()
            if message.text == "Українська":
                lenguages.TextLanguage.choose_language("Українська")

            greeting = (
                f"{lenguages.TextLanguage.greeting_start}"
                f"{message.from_user.first_name}. "
                f"{lenguages.TextLanguage.greeting_end}"
            )
            bot.send_message(message.chat.id, greeting)

        if message.text == CHATS[message.chat.id].right_answer:
            CHATS[message.chat.id].count_right_answers += 1

        """ send result for user and if username exists - for teacher to"""

        if message.text == lenguages.TextLanguage.button_get_result:
            user_level = UserLevel.get_level(CHATS[message.chat.id].count_right_answers)
            bot.send_message(
                message.chat.id,
                f"{lenguages.TextLanguage.result}: {user_level}",
            )
            if message.from_user.username:
                bot.send_message(TEACHER_CHAT_ID, ("\U0001F33C" * 9))
                bot.send_message(
                    TEACHER_CHAT_ID,
                    f"@{message.from_user.username}\n{user_level}",
                )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_start = types.KeyboardButton("/start")
            markup.add(button_start)
            bot.send_message(message.chat.id, lenguages.TextLanguage.start, reply_markup=markup)
            CHATS.pop(message.chat.id)


            # доделать если нет юзернэйма

        if message.chat.id in CHATS:

            """ test process """

            if (
                CHATS[message.chat.id].question_counter
                < CHATS[message.chat.id].questions_left
            ):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("A")
                button2 = types.KeyboardButton("B")
                button3 = types.KeyboardButton("C")
                button4 = types.KeyboardButton("D")
                button5 = types.KeyboardButton(
                    lenguages.TextLanguage.button_i_dont_know
                )
                markup.add(button1, button2, button3, button4, button5)
                bot.send_message(
                    message.chat.id,
                    CHATS[message.chat.id].current_question,
                    reply_markup=markup,
                )

                if (
                    CHATS[message.chat.id].question_counter
                    < CHATS[message.chat.id].questions_left - 1
                ):
                    CHATS[message.chat.id].add_user_answers(message.text)
                    CHATS[message.chat.id].change_counter()
                    CHATS[message.chat.id].change_right_answer()

                elif (
                    CHATS[message.chat.id].counter_for_answers
                    < CHATS[message.chat.id].questions_left - 1
                ):
                    CHATS[message.chat.id].add_user_answers(message.text)
                    CHATS[message.chat.id].change_right_answer()

            else:

                """ end of test, get result, request for contact and send to teacher """

                CHATS[message.chat.id].add_user_answers(message.text)

                if message.from_user.username:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button_result = types.KeyboardButton(
                        lenguages.TextLanguage.button_get_result
                    )
                    markup.add(button_result)
                    bot.send_message(
                        message.chat.id,
                        lenguages.TextLanguage.question_result,
                        reply_markup=markup,
                    )
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    button_result = types.KeyboardButton(
                        lenguages.TextLanguage.button_get_result
                    )
                    button_start = types.KeyboardButton("/start")
                    button_teacher = types.KeyboardButton(
                        lenguages.TextLanguage.result_to_teacher, request_contact=True
                    )
                    markup.add(button_result, button_start, button_teacher)
                    bot.send_message(
                        message.chat.id,
                        lenguages.TextLanguage.question_result,
                        reply_markup=markup,
                    )

        print(CHATS)
        print(message.from_user.id)

@bot.message_handler(content_types=['contact'])
def contact(message):
    user_level = UserLevel.get_level(CHATS[message.chat.id].count_right_answers)
    # bot_email.send_email(CHATS[message.chat.id].user_answers)
    bot.send_message(message.chat.id, f"{lenguages.TextLanguage.result}: {user_level}")
    bot.send_message(TEACHER_CHAT_ID, (u"\U0001F33C" * 9))
    bot.send_contact(TEACHER_CHAT_ID, f"{message.contact.phone_number}",
                        f"{user_level}\n",
                        f"{message.contact.first_name} {message.contact.last_name}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = types.KeyboardButton("/start")
    markup.add(button_start)
    bot.send_message(message.chat.id, lenguages.TextLanguage.start, reply_markup=markup)
    CHATS.pop(message.chat.id)


    print(CHATS)
    print(message.from_user.id)


if __name__ == "__main__":
    bot.polling(none_stop=True)
