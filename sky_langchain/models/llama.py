import os

import dotenv

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import LlamaCpp

dotenv.load_dotenv()

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
codellama = LlamaCpp(
    model_path=os.getenv("CODE_LLAMA_MODEL_PATH"),
    n_ctx=5000,
    n_gpu_layers=40,
    n_batch=512,
    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
    callback_manager=callback_manager,
    verbose=True,
)
