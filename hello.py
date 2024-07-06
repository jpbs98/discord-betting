import os
from dotenv import load_dotenv
from interactions import Client, Intents, slash_command, SlashContext


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(intents=Intents.DEFAULT)


@slash_command(name="hello", description="Bot is alive!")
async def hello(ctx: SlashContext):
    await ctx.send("Hello World")


bot.start(BOT_TOKEN)
