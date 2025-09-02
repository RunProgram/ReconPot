from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client

# load tokens
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL_ID: Final[int] = int(os.getenv('DISCORD_CHANNEL_ID'))

# setup bot
intents: Intents = Intents.default()
client: Client = Client(intents=intents)


# how alerts will be sent from honeypot.py
async def send_alert(ip: str):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"@everyone Web Reconnaissance detected! Fake admin page served to `{ip}`")


# start the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


def run_bot() -> None:
    client.run(token=TOKEN)
