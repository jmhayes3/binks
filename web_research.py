import os
import logging

from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.retrievers.web_research import WebResearchRetriever
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.utilities import GoogleSearchAPIWrapper


logging.basicConfig()
logging.getLogger("langchain.retrievers.web_research").setLevel(logging.INFO)

os.environ["GOOGLE_CSE_ID"] = "424e6196a076845fb"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBbnJhgblDoKO9OMiE2hcy2ZsIbIoGvuWQ"

search = GoogleSearchAPIWrapper()

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = Ollama(model="llama2", callback_manager=callback_manager)
vectorstore = Chroma(embedding_function=GPT4AllEmbeddings(), persist_directory="./db")

web_research_retriever = WebResearchRetriever.from_llm(
    vectorstore=vectorstore,
    llm=llm,
    search=search,
)

qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm,
    retriever=web_research_retriever,
    return_source_documents=True
)


if __name__ == "__main__":
    user_input = "What is Task Decomposition in LLM Powered Autonomous Agents?"

    result = qa_chain({"question": user_input})

    print(result["answer"])
    print(result["source_documents"])
