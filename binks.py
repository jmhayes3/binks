import os

import discord

from discord.ext import commands

from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.chains import LLMChain

from utils import make_chain


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = False
intents.typing = False

bot = commands.Bot(command_prefix="/", intents=intents)

CHAIN_CACHE = {}


@bot.event
async def on_ready():
    start_message = f"Logged in as {bot.user} (ID: {bot.user.id})"
    print(start_message)
    print("-" * len(start_message))


@bot.command()
async def chat(ctx, msg):
    """Execute query, keeping track of chat history."""

    user = ctx.author
    if user not in CHAIN_CACHE:
        CHAIN_CACHE[user] = make_chain(user)

    chain = CHAIN_CACHE[user]
    response = chain.run(msg)

    await ctx.send(response)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    bot.run(DISCORD_TOKEN)
