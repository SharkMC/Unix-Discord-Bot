import discord
import os
import requests
import dotenv

from server import server_thread

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

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

                response = requests.get(url)
                data = response.json()
                if data['online']:
                    await message.channel.send(f"{data['players']['online']} / 100")
                else:
                    await message.channel.send("The server is offline")
            except Exception as e:
                await message.channel.send(f"Error: {e}")

# Intents を設定
intents = discord.Intents.default()
intents.message_content = True

# MyClient のインスタンスを作成（← ここが重要！）
client = MyClient(intents=intents)

# サーバースレッドを開始
server_thread()

# Bot を実行
client.run(TOKEN)