import dotenv

from langchain.chat_models import ChatOpenAI

dotenv.load_dotenv()

chatgpt_three_point_five_turbo = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
)
