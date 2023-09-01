import os

import discord

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from dotenv import load_dotenv


def generate_chain(params):
    pass


# Load env vars from .env file in project directory.
load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
openai_token = os.getenv('OPENAI_API_KEY')

bot_client = discord.Client(intents=discord.Intents.all())

conversation_cache = {}


@bot_client.event
async def on_message(msg):
    # Don't respond to self or we'll end up in an infinite loop.
    if msg.author == bot_client.user:
        return

    command = msg.content[:7]
    if not command.lower() == "/binks ":
        return

    message = msg.content[7:]

    user = msg.author.name
    if user not in conversation_cache:
        prompt_template = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                # f"Greet {user}, making a joke about their name, then answer any questions they may have."
                # "You are Binks, an AI assistant with the wit and charm of a barn animal."
                # "You are Jar Jar Binks from Star Wars. You will respond to all messages in a style compatable with the speech patterns of Jar Jar Binks."
                # "You are the philosopher Socrates. You will answer all questions with a question."
                "You are Binks, a straight-to-the-point AI assistant, with a great sense of humor."
            ),
            MessagesPlaceholder(variable_name='history'),
            HumanMessagePromptTemplate.from_template('{input}')
        ])

        llm = ChatOpenAI(
            openai_api_key=openai_token,
            temperature=0.9
        )
        memory = ConversationBufferWindowMemory(
            llm=llm,
            return_messages=True
        )
        chain = ConversationChain(
            llm=llm,
            prompt=prompt_template,
            memory=memory,
            verbose=True
        )
        conversation_cache[user] = chain

    conversation = conversation_cache[user]
    response = await conversation.arun(input=message)

    await msg.channel.send(response)


if __name__ == "__main__":
    bot_client.run(discord_token)

