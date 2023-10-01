from langchain_core.wrapper import ChatChainWrapper

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from bs4 import BeautifulSoup as Soup
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.memory import ConversationSummaryMemory
from langchain_core.models import chatgpt_three_point_five_turbo

url = "https://python.langchain.com/docs/use_cases"
loader = RecursiveUrlLoader(
    url=url, max_depth=2, extractor=lambda x: Soup(x, "html.parser").text
)

llm = chatgpt_three_point_five_turbo
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
wrapper = ChatChainWrapper(llm, loader, splitter, memory)
vectorstore = Chroma.from_documents(
    documents=wrapper.split(), embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
wrapper.load_retriever(retriever)
wrapper.run()
