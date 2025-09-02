from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL_ID: Final[int] = int(os.getenv('DISCORD_CHANNEL_ID'))

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
client: Client = Client(intents=intents)


# Function for honeypot.py to send alerts
async def send_alert(ip: str):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"@everyone Web Reconnaissance detected! Fake admin page served to `{ip}`")


# STEP 2: STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


def run_bot() -> None:
    client.run(token=TOKEN)
