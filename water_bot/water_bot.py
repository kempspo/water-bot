import os
from datetime import datetime
import discord
import asyncio


class water_bot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as: {self.user.name}')
        print(self.user.id)
        print('------')

    def check_time(self):
        current_time = datetime.now()

        if (current_time.hour > 9 and current_time.hour < 12):
            if (current_time.minute % 30 == 0):
                return True

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(705490952135114816)
        while not self.is_closed():
            if (self.check_time() == True):
                await channel.send('Drink Water')
                await asyncio.sleep(60)


if __name__ == "__main__":
    token = os.getenv('WATER_BOT_TOKEN')
    client = water_bot()
    client.run(token)