import discord
from discord import Intents
import requests
import math

intents = Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=await get_eth_price()))

async def get_eth_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    data = response.json()
    price = data['ethereum']['usd']

    rounded_price = round(price)

    return f'ETH: ${rounded_price} USD'

client.run('YOUR TOKEN')


