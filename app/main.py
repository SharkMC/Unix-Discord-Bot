import discord
import os
import requests
import dotenv
from discord import app_commands
from server import server_thread

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

url_discord = 'https://discord.gg/zns7VZteC2'
url_logo = 'https://cdn.discordapp.com/attachments/1232460820034621483/1336660604760621127/70_4EDCD21.png'
ip = 'unix.f5.si'
port = '25720'
server_name = 'Unix'


@client.event
async def on_ready():
    print(f'Logined: {client.user}')
    await tree.sync()

@tree.command(name='info', description='Show server information')
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="**Information**",
        description=f"**Discord: {url_discord}**",
        color=discord.Color.blue()
    )
    embed.set_author(name=server_name)
    embed.set_thumbnail(url=url_logo)
    embed.set_footer(text=ip)
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
    embed.set_author(name=server_name)
    embed.set_thumbnail(url=url_logo)
    embed.set_footer(text=ip)
    await interaction.response.send_message(embed=embed)

@tree.command(name='rule', description='Send rule')
@app_commands.describe(channel="Please select a channel", message="Please enter the rule")
@app_commands.checks.has_permissions(manage_messages=True)
async def rule(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    embed = discord.Embed(
        title="**Rule**",
        description=message,
        color=discord.Color.blue()
    )
    embed.set_author(name=server_name)
    embed.set_thumbnail(url=url_logo)
    embed.set_footer(text=ip)
    await channel.send(embed=embed)
    await interaction.response.send_message(f"Sent message to {channel.mention}", ephemeral=True)

@tree.command(name='status', description='Show server status')
async def status(interaction: discord.Interaction):
    try:
        url = f"https://api.mcsrvstat.us/bedrock/2/{ip}:{port}"
        response = requests.get(url)
        data = response.json()

        if data['online']:
            embed = discord.Embed(
                title="🟢 **ONLINE**",
                color=discord.Color.blue()
            )
            embed.set_author(name=server_name)
            embed.set_thumbnail(url=url_logo)
            embed.add_field(name="__**Players**__", value=f"**{data['players']['online']} / {data['players']['max']}**\n\n\n", inline=False)
            embed.add_field(name="__**Server Address**__", value=f"**IP:** {ip}\n**Port:** {port}\n\n\n", inline=False)
            embed.add_field(name="__**Version**__", value=f"**{data['version']}**", inline=False)
            embed.set_footer(text=ip)

            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                title="🔴 **OFFLINE**",
                description="**Server is offline.**",
                color=discord.Color.blue()
            )

            embed.set_author(name=server_name)
            embed.set_thumbnail(url=url_logo)
            embed.set_footer(text=ip)

            await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")

server_thread()

if TOKEN:
    client.run(TOKEN)
else:
    print("Error: TOKEN is not set! Check your environment variables.")