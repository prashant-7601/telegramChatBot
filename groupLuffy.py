# -*- coding: UTF8 -*-
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance
import os

names = ["luffy", "monkey d. luffy", "monkey d luffy", "lucy", "mughiwara-ya", "mughi-chan"]
"""logic_adapters=[
                  {'import_path': 'chatterbot.logic.BestMatch',
                   'default_response': 'I am sorry, but I do not understand.',
                   'maximum_similarity_threshold': 1.0}]"""
bot = ChatBot('Bot',
              statement_comparison_function=levenshtein_distance
              )
trainer = ListTrainer(bot)

for files in os.listdir("C:\\Users\\LENOVO\\PycharmProjects\\telegramBots\\Luffy"):
    data = open("C:\\Users\\LENOVO\\PycharmProjects\\telegramBots\\Luffy\\" + files, "r").readlines()
    trainer.train(data)


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


bot_token = '1470602197:AAEyM_sV39x7GKR8I7QwF6PEoLdn-G79MQs'  # Token of your bot
luffy_bot = BotHandler(bot_token)  # Your bot's name


def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates = luffy_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if current_update['message']['chat']['type'] == "group":
                    if 'group_chat_created' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        title = current_update['message']['chat']['title']
                        luffy_bot.send_message(first_chat_id, "{} group created successfully! Promote me to admin to "
                                                              "make sure I function properly".format(title))
                    elif 'new_chat_title' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        title = current_update['message']['new_chat_title']
                        luffy_bot.send_message(first_chat_id, "Group name changed to {}".format(title))
                    elif 'new_chat_participant' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        if current_update['message']['new_chat_participant']['id'] == "OPLuffyBot":
                            luffy_bot.send_message(first_chat_id, "Thanks for adding me!")
                        else:
                            first_chat_name = current_update['message']['new_chat_participant']['first_name']
                            luffy_bot.send_message(first_chat_id, "{} welcome!".format(first_chat_name))
                    elif 'left_chat_participant' in current_update['message']:
                        if current_update['message']['left_chat_participant']['id'] != "OPLuffyBot":
                            first_chat_name = current_update['message']['left_chat_participant']['first_name']
                            first_chat_id = current_update['message']['chat']['id']
                            luffy_bot.send_message(first_chat_id, "See you again {} !".format(first_chat_name))
                    elif 'text' in current_update['message']:
                        if current_update['message']['text'].lower().split()[0] in names:
                            print("response sent")
                            words = current_update['message']['text'].lower().split()[1:]
                            first_chat_id = current_update['message']['chat']['id']
                            message = ' '.join(words)
                            print(message)
                            response = bot.get_response(message.lower())
                            luffy_bot.send_message(first_chat_id, response)
                    elif 'document' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a document! I can't process "
                                                                      "them right now.")
                    elif 'audio' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me an audio! I can't process "
                                                                      "them right now.")
                    elif 'video' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a video! I can't process "
                                                                      "them right now.")
                    elif 'animation' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me an animation! I can't process "
                                                                      "them right now.")
                    elif 'photo' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a photo! I can't process "
                                                                      "them right now.")
                    elif 'sticker' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a sticker! I can't process "
                                                                      "them right now.")
                    elif 'video_note' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a video note! I can't process "
                                                                      "them right now.")
                    elif 'voice' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a voice! I can't process "
                                                                      "them right now.")
                    elif 'contact' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a contact! I can't process "
                                                                      "them right now.")
                    elif 'dice' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a dice! I can't process "
                                                                      "them right now.")
                    elif 'game' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a game! I can't process "
                                                                      "them right now.")
                    elif 'poll' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a poll! I can't process "
                                                                      "them right now.")
                    elif 'venue' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a venue! I can't process "
                                                                      "them right now.")
                    elif 'location' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a location! I can't process "
                                                                      "them right now.")
                    new_offset = first_update_id + 1
                elif current_update['message']['chat']['type'] == "supergroup":
                    if 'supergroup_chat_created' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        title = current_update['message']['chat']['title']
                        luffy_bot.send_message(first_chat_id, "{} supergroup created successfully! Promote me to "
                                                              "admin to make sure I function properly".format(title))
                    elif 'new_chat_title' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        title = current_update['message']['new_chat_title']
                        luffy_bot.send_message(first_chat_id, "Supergroup name changed to {}".format(title))
                    elif 'new_chat_participant' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        if current_update['message']['new_chat_participant']['id'] == "OPLuffyBot":
                            luffy_bot.send_message(first_chat_id, "Thanks for adding me!")
                        else:
                            first_chat_name = current_update['message']['new_chat_participant']['first_name']
                            luffy_bot.send_message(first_chat_id, "{} welcome!".format(first_chat_name))
                    elif 'left_chat_participant' in current_update['message']:
                        if current_update['message']['left_chat_participant']['id'] != "OPLuffyBot":
                            first_chat_name = current_update['message']['left_chat_participant']['first_name']
                            first_chat_id = current_update['message']['chat']['id']
                            luffy_bot.send_message(first_chat_id, "See you again {} !".format(first_chat_name))
                    elif 'text' in current_update['message']:
                        if current_update['message']['text'].lower().split()[0] in names:
                            print("response sent")
                            words = current_update['message']['text'].lower().split()[1:]
                            first_chat_id = current_update['message']['chat']['id']
                            message = ' '.join(words)
                            print(message)
                            response = bot.get_response(message.lower())
                            luffy_bot.send_message(first_chat_id, response)
                    elif 'document' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a document! I can't process "
                                                                      "them right now.")
                    elif 'audio' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me an audio! I can't process "
                                                                      "them right now.")
                    elif 'video' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a video! I can't process "
                                                                      "them right now.")
                    elif 'animation' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me an animation! I can't process "
                                                                      "them right now.")
                    elif 'photo' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a photo! I can't process "
                                                                      "them right now.")
                    elif 'sticker' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a sticker! I can't process "
                                                                      "them right now.")
                    elif 'video_note' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a video note! I can't process "
                                                                      "them right now.")
                    elif 'voice' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a voice! I can't process "
                                                                      "them right now.")
                    elif 'contact' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a contact! I can't process "
                                                                      "them right now.")
                    elif 'dice' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a dice! I can't process "
                                                                      "them right now.")
                    elif 'game' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a game! I can't process "
                                                                      "them right now.")
                    elif 'poll' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a poll! I can't process "
                                                                      "them right now.")
                    elif 'venue' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a venue! I can't process "
                                                                      "them right now.")
                    elif 'location' in current_update['message']:
                        if 'caption' in current_update['message']:
                            if current_update['message']['caption'].lower().split()[0] in names:
                                first_chat_id = current_update['message']['chat']['id']
                                luffy_bot.send_message(first_chat_id, "Ah, you sent me a location! I can't process "
                                                                      "them right now.")
                    new_offset = first_update_id + 1
                elif current_update['message']['chat']['type'] == "private":
                    if 'text' in current_update['message']:
                        print("response sent")
                        first_chat_id = current_update['message']['chat']['id']
                        message = current_update['message']['text'].lower()
                        print(message)
                        response = bot.get_response(message.lower())
                        luffy_bot.send_message(first_chat_id, response)
                    elif 'document' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a document! I can't process "
                                                              "them right now.")
                    elif 'audio' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me an audio! I can't process "
                                                              "them right now.")
                    elif 'video' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a video! I can't process "
                                                              "them right now.")
                    elif 'animation' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me an animation! I can't process "
                                                              "them right now.")
                    elif 'photo' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a photo! I can't process "
                                                              "them right now.")
                    elif 'sticker' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a sticker! I can't process "
                                                              "them right now.")
                    elif 'video_note' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a video note! I can't process "
                                                              "them right now.")
                    elif 'voice' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a voice! I can't process "
                                                              "them right now.")
                    elif 'contact' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a contact! I can't process "
                                                              "them right now.")
                    elif 'dice' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a dice! I can't process "
                                                              "them right now.")
                    elif 'game' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a game! I can't process "
                                                              "them right now.")
                    elif 'poll' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a poll! I can't process "
                                                              "them right now.")
                    elif 'venue' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a venue! I can't process "
                                                              "them right now.")
                    elif 'location' in current_update['message']:
                        first_chat_id = current_update['message']['chat']['id']
                        luffy_bot.send_message(first_chat_id, "Ah, you sent me a location! I can't process "
                                                              "them right now.")
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
