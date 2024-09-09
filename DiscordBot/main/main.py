from pickle import NONE
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, user
from responses import get_response

#Step 1: load the token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Step 2: bot setup
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

#Step 3: message functionality
async def sendMessage(message: Message, userMessage: str) -> None:
    if not userMessage:
        print("No message because intents were not enabled")
        return

    isPrivate = userMessage[0] == '?'

    if isPrivate:
        userMessage = userMessage[1:]

    try:
        response: str = get_response(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


#Step 4: Handling starting the bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is running!")

#Step 5: Handling events
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}], {username}: '{user_message}'")
    await sendMessage(message, user_message)

#Step 6: Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()