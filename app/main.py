import discord
import os
import requests
import dotenv
from discord import app_commands
from server import server_thread

# 環境変数を読み込む
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intents を設定
intents = discord.Intents.default()
intents.message_content = True

# クライアントのインスタンスを作成
client = discord.Client(intents=intents)

# コマンドツリーを作成
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')
    await tree.sync()
    print("スラッシュコマンドが同期されました。")

@tree.command(name='info', description='Show server information')
async def info(interaction: discord.Interaction):
    await interaction.response.send_message('Discord: https://discord.gg/zns7VZteC2')

@tree.command(name='staff', description='Show staff members')
async def staff(interaction: discord.Interaction):
    await interaction.response.send_message(
        '-------« Staff Member »-------\n'
        'ShqrkMC - Founder, Owner, Dev\n'
        'eozah - Owner, Dev\n'
        'Uran3007 - Manager, Builder\n'
        'x Ramuneee - Admin, Builder\n'
        'Yuk1yQwQ - Admin\n'
        '--------------------------------'
    )

@tree.command(name='status', description='Show server status')
async def status(interaction: discord.Interaction):
    try:
        url = "https://api.mcsrvstat.us/bedrock/2/unix.f5.si:25720"
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
if TOKEN:
    client.run(TOKEN)
else:
    print("Error: TOKEN is not set! Check your environment variables.")