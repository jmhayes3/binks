import random

from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)


async def choose(*choices):
    return random.choice(*choices)


def make_chain(user, model="llama2"):
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            f"Greet {user} and make a joke about their name, then answer any questions."
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])
    callbacks = []
    llm = Ollama(
        model=model,
        callbacks=callbacks,
    )
    memory = ConversationBufferMemory(
        llm=llm,
        return_messages=True
    )
    chain = ConversationChain(
        llm=llm,
        prompt=prompt_template,
        memory=memory,
        verbose=True
    )
    return chain

