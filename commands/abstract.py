class AbstractCommand:
    COMMAND = "*TYPE COMMAND HERE*"

    async def handler(self, update, context):
        raise NotImplementedError("Handler is not implemented")
