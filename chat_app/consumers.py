from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        return await super().connect()()
    pass