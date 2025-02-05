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
    embed = discord.Embed(
        title="**Information**",
        description="**Discord: https://discord.gg/zns7VZteC2**",
        color=discord.Color.blue()  # 修正: () を追加
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name='staff', description='Show staff members')
async def staff(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Staff",
        description=(
            "-------« Staff Member »-------\n"
            "ShqrkMC - Founder, Owner, Dev\n"
            "eozah - Owner, Dev\n"
            "Uran3007 - Manager, Builder\n"
            "x Ramuneee - Admin, Builder\n"
            "Yuk1yQwQ - Admin\n"
            "--------------------------------"
        ),
        color=discord.Color.blue()  # 修正: () を追加
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name='status', description='Show server status')
async def status(interaction: discord.Interaction):
    try:
        url = "https://api.mcsrvstat.us/bedrock/2/unix.f5.si:25720"
        response = requests.get(url)
        data = response.json()
        
        if data['online']:
            embed = discord.Embed(
                title="**🟢 ONLINE**",
                color=discord.Color.blue()  # 修正: () を追加
            )
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/1232460820034621483/1336660604760621127/70_4EDCD21.png?ex=67a49db2&is=67a34c32&hm=9519a88f37a73456ee8e6e627ecd0939d7a1ef03028429698cc607c32a484ecc&")
            embed.add_field(name="__**Players**__", value=f"**{data['players']['online']} / 100**\n", inline=False)  # 修正: f"" を追加
            embed.add_field(name="__**Server Address**__", value="**IP: unix.f5.si\nPort: 25720**\n", inline=False)
            embed.add_field(name="__**Version**__", value="**1.21.50**", inline=False)

            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                title="**🔴 OFFLINE**",
                description="**Server is offline.**",
                color=discord.Color.blue()  # 修正: () を追加
            )
            embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/1232460820034621483/1336660604760621127/70_4EDCD21.png?ex=67a49db2&is=67a34c32&hm=9519a88f37a73456ee8e6e627ecd0939d7a1ef03028429698cc607c32a484ecc&")
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")

# サーバースレッドを開始
server_thread()

# Bot を実行
if TOKEN:
    client.run(TOKEN)
else:
    print("Error: TOKEN is not set! Check your environment variables.")