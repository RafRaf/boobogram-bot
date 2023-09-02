import json
import random
import aiohttp

from commands.abstract import AbstractCommand
from settings import BOOBS_API_URL, BOOBS_AMOUNT, BOOBS_MEDIA_URL


class BoobsCommand(AbstractCommand):
    COMMAND = "boobs"

    @staticmethod
    async def _make_request(url):
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)

            return resp.status, await resp.read()

    async def get_random_boobs(self):
        url = f"{BOOBS_API_URL}noise/{BOOBS_AMOUNT}/"
        code, resp = await self._make_request(url)

        if code == 200:
            return json.loads(resp)

    async def get_boobs_by_model(self, model_name):
        url = f"{BOOBS_API_URL}boobs/model/{model_name}/"
        code, resp = await self._make_request(url)

        if code == 200:
            photo_items_list = json.loads(resp)

            if len(photo_items_list) > BOOBS_AMOUNT:
                photo_items_id_list = [item['id'] for item in photo_items_list]
                processed_photo_items_list = set()

                while len(processed_photo_items_list) != BOOBS_AMOUNT:
                    processed_photo_items_list.add(random.choice(photo_items_id_list))

                return [
                    item
                    for item in photo_items_list if item['id'] in processed_photo_items_list
                ]

            return photo_items_list

    async def handler(self, update, context):
        _, *params = update.message.text.split()
        message = ' '.join(params)
        coro = self.get_boobs_by_model(message) \
            if message else self.get_random_boobs()

        if photo_items := await coro:
            for photo_item in photo_items:
                photo_url = photo_item.get('preview')

                if photo_url:
                    await context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=BOOBS_MEDIA_URL + photo_url
                    )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="\"%s\" - not found :(" % message
            )
