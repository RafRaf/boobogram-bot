import json
import random
import requests

from commands.abstract import AbstractCommand
from settings import BOOBS_API_URL, BOOBS_AMOUNT, BOOBS_MEDIA_URL


class BoobsCommand(AbstractCommand):
    COMMAND = 'boobs'

    @staticmethod
    def _make_request(url):
        return requests.get(url)

    def get_random_boobs(self):
        response = self._make_request('{url}noise/{amount}/'.format(url=BOOBS_API_URL, amount=BOOBS_AMOUNT))

        if response.status_code == 200:
            return json.loads(response.text)

    def get_boobs_by_model(self, model_name):
        response = self._make_request('{url}boobs/model/{name}/'.format(url=BOOBS_API_URL, name=model_name))

        if response.status_code == 200:
            photo_items_list = json.loads(response.text)

            if len(photo_items_list) > BOOBS_AMOUNT:
                photo_items_id_list = [item['id'] for item in photo_items_list]
                processed_photo_items_list = set()

                while len(processed_photo_items_list) != BOOBS_AMOUNT:
                    processed_photo_items_list.add(random.choice(photo_items_id_list))

                return [item for item in photo_items_list if item['id'] in processed_photo_items_list]

            return photo_items_list

    def handler(self, bot, update):
        cmd, *params = update.message.text.split()
        message = ' '.join(params)

        photo_items = self.get_boobs_by_model(message) if message else self.get_random_boobs()

        if photo_items:
            for photo_item in photo_items:
                photo_url = photo_item.get('preview')

                if photo_url:
                    bot.sendPhoto(update.message.chat_id, photo=BOOBS_MEDIA_URL + photo_url)
        else:
            bot.sendMessage(update.message.chat_id, text='"%s" - not found :(' % message)
