class AbstractCommand:
    COMMAND = '*TYPE COMMAND HERE*'

    def handler(self, bot, update):
        raise NotImplementedError('Handler is not implemented')
