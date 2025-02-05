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
        color=discord.Color.blue()
    )
    embed.set_image(url="https://example.com/logo.png")  # 右上にロゴを表示
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
        color=discord.Color.blue()
    )
    embed.set_image(url="https://example.com/logo.png")  # 右上にロゴを表示
    await interaction.response.send_message(embed=embed)

@tree.command(name='status', description='Show server status')
async def status(interaction: discord.Interaction):
    try:
        url = "https://api.mcsrvstat.us/bedrock/2/unix.f5.si:25720"
        response = requests.get(url)
        data = response.json()

        server_logo = "https://cdn.discordapp.com/attachments/1232460820034621483/1336660604760621127/70_4EDCD21.png"

        if data['online']:
            embed = discord.Embed(
                title="🟢 **ONLINE**",
                color=discord.Color.blue()  # 緑色のライン
            )
            embed.set_author(name="Unix")  # 上部の名前
            embed.set_thumbnail(url=server_logo)  # 右上の画像
            embed.add_field(name="__**Players**__", value=f"**{data['players']['online']} / 100**", inline=False)

            embed.add_field(name=" ", value="", inline=False)
            embed.add_field(name="__**Server Address**__", value="**IP:** unix.f5.si\n**Port:** 25720", inline=False)

            embed.add_field(name=" ", value="", inline=False)
            embed.add_field(name="__**Version**__", value="**1.21.50**", inline=False)
            embed.set_footer(text="unix.f5.si")

            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                title="🔴 **OFFLINE**",
                description="**Server is offline.**",
                color=discord.Color.blue()  # 赤色のライン
            )
            embed.set_thumbnail(url=server_logo)  # 右上の画像
            embed.set_footer(text="unix.f5.si")

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