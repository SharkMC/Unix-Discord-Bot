import discord
import os
import requests
import dotenv

from discord import app_commands 
from server import server_thread

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")



class MyClient(discord.Client):

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    tree = app_commands.CommandTree(client)

    async def on_ready(self):
        print(f'ログインしました: {self.user}')
        await tree.sync()

    @tree.command(name='info', description='Show server information')
    async def info(interaction: discord.Interaction):
        await interaction.response.send_message('Discord: https://discord.gg/zns7VZteC2')

    @tree.command(name='staff', description='Show staff members')
    async def staff(interaction: discord.Interaction):
        await interaction.response.send_message('-------« Staff Member »-------\nShqrkMC - Founder, Owner, Dev\neozah - Owner, Dev\nUran3007 - Manager, Builder\nx Ramuneee - Admin, Builder\nYuk1yQwQ - Admin\n--------------------------------')

    @tree.command(name='status', description='Show server status')
    async def status(interaction: discord.Interaction):
        try:
            url = f"https://api.mcsrvstat.us/bedrock/2/unix.f5.si:25720"
            response = requests.get(url)
            data = response.json()
            if data['online']:
                await interaction.response.send_message(f"{data['players']['online']} / 100")
            else:
                await interaction.response.send_message("The server is offline")

        except Exception as e:
            await interaction.response.send_message(f"Error: {e}")

# サーバースレッドを開始
server_thread()

# Bot を実行
client.run(TOKEN)