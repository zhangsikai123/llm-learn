import dotenv

dotenv.load_dotenv()
from wrapper import ChatChainWrapper
import os

from git import RemoteProgress
from git import Repo
from tqdm import tqdm

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=""):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
)
# from git import Repo
# Clone

repo_path = "/Users/zhangsikai/tmp/test_repo"
url = "https://github.com/pallets/flask.git"
if not (os.path.exists(repo_path) and os.listdir(repo_path)):
    repo = Repo.clone_from(url, to_path=repo_path, progress=CloneProgress())
# Load
loader = GenericLoader.from_filesystem(
    repo_path,
    glob="**/*",
    suffixes=[".py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
)
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)
wrapper = ChatChainWrapper(llm, loader, splitter, memory)
db = Chroma.from_documents(wrapper.split(), OpenAIEmbeddings(disallowed_special=()))
retriever = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)
wrapper.load_retriever(retriever)
wrapper.run()
