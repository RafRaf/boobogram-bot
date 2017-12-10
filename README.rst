.. image:: https://travis-ci.org/RafRaf/boobogram-bot.svg?branch=master
    :target: https://travis-ci.org/RafRaf/boobogram-bot

Boobogram Bot (@boobogram_bot)
==============================
Just a simple bot created for fun and relaxation. It's especially needed when you spend days and nights just coding.

How to Use
----------
* Add the bot to your telegram's group. (Add **@boobogram_bot** or go to https://telegram.me/boobogram_bot)
* Type "/boobs" and take a break. :)

How to Contribute
-----------------
Your PR (or even issue) will be very appreciate. Every PR merged to "master" branch triggers bot's code updating.

How to Use locally
----------------------
You have to create local.py and define some variables:

.. code:: python

    import logging


    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Settings
    BOOBS_API_URL = 'http://api.oboobs.ru/'
    BOOBS_MEDIA_URL = 'http://media.oboobs.ru/'
    BOOBS_AMOUNT = 1
    BOOBS_TOKEN = '***'

Docker support
--------------
You can build your own boobogram_bot container:

* docker build . -t boobs
* docker run -v /path_to_project_folder/boobogram-bot:/app --rm boobs

Have fun! ( . )( . )
