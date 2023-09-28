from wrapper import ChatChainWrapper

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


loader = WebBaseLoader("https://python.langchain.com/docs/use_cases/code_understanding")
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
wrapper = ChatChainWrapper(llm, loader, splitter)
vectorstore = Chroma.from_documents(
    documents=wrapper.split(), embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()
wrapper.load_retriever(retriever)
wrapper.run()
