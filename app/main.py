import discord
import os
import requests

form server import server_thread

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'ログインしました: {self.user}')

    async def on_message(self, message):
        print(f'送信: {message.author}: {message.content}')
        if message.author == self.user:
            return

        if message.content == '!info':
            await message.channel.send('Discord: https://discord.gg/zns7VZteC2')

        elif message.content == '!staff':
            await message.channel.send('-------« Staff Member »-------\nShqrkMC - Founder, Owner, Dev\neozah - Owner, Dev\nUran3007 - Manager, Builder\nx Ramuneee - Admin, Builder\nYuk1yQwQ - Admin\n--------------------------------')

        elif message.content == '!status':
            try:
                url = f"https://api.mcsrvstat.us/bedrock/2/unix.f5.si:25720"

                responce = requests.get(url)
                data = responce.json()
                if data['online']:
                    await message.channel.send(f"{data['players']['online']} / 100")
                else:
                    await message.channel.send("The server is offline")
            except Exception as e:
                    await message.channel.send(f"Error: {e}")

intents = discord.Intents.default()
intents.message_content = True

server_thread()
client.run(TOKEN)