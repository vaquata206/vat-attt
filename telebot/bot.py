import telegram
from telebot.credentials import bot_token, URL
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

telegram_bot = telegram.Bot(token=bot_token)
PARSE_MODE_MARK_DOWN = "MarkdownV2"
PARSE_MODE_HTML = "HTML"


def send_message_with_button(chat_id, text: str, buttons: []):
    print("send_message_with_button")
    button_list = [InlineKeyboardButton(btn["title"], callback_data=str(btn["callback_data"])) for btn in buttons]
    # n_cols = 1 is for single column and mutliple rows
    reply_markup = InlineKeyboardMarkup(_build_menu(button_list, n_cols=1))
    telegram_bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)


def send_message(chat_id, text, parse_mode=None):
    telegram_bot.sendMessage(chat_id=chat_id, text=text, parse_mode=parse_mode)


def reply_message(chat_id, text: str, reply_message_id, buttons: [] = None):
    reply_markup = None
    if buttons is not None and len(buttons) > 0:
        button_list = [InlineKeyboardButton(btn["title"], callback_data=str(btn["callback_data"])) for btn in buttons]
        reply_markup = InlineKeyboardMarkup(_build_menu(button_list, n_cols=1))
    telegram_bot.send_message(chat_id=chat_id, text=text,
                              reply_to_message_id=reply_message_id, reply_markup=reply_markup)


def edit_message_text(chat_id, text: str, message_id, buttons: [], parse_mode=None):
    button_list = [InlineKeyboardButton(btn["title"], callback_data=str(btn["callback_data"])) for btn in buttons]
    # n_cols = 1 is for single column and mutliple rows
    reply_markup = InlineKeyboardMarkup(_build_menu(button_list, n_cols=1))
    telegram_bot.edit_message_text(text, chat_id=chat_id,
                                   message_id=message_id,
                                   reply_markup=reply_markup,
                                   parse_mode=parse_mode)


def set_web_hook():
    print("webhook: " + "{URL}{HOOK}".format(URL=URL, HOOK=bot_token))
    s = telegram_bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=bot_token))
    # s = "{URL}{HOOK}".format(URL=URL, HOOK=bot_token)
    print(s)
    return s


def decode_message(json):
    return telegram.Update.de_json(json, telegram_bot)


def is_admin_group(user_id, chat_id):
    admins = telegram_bot.getChatAdministrators(chat_id)
    for ad in admins:
        mem = telegram.ChatMember.de_json(ad.to_dict(), telegram_bot)
        if not mem.user.is_bot and mem.user.id == user_id:
            return True
    return False


def get_update():
    return telegram_bot.get_updates()


def get_file(file_id):
    return telegram_bot.get_file(file_id=file_id)


def _build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
