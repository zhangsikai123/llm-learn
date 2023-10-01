
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
codellama = LlamaCpp(
    model_path="/nfs_beijing/sikai/weight/llama/TheBloke/CodeLlama-13B-Instruct-GGUF/codellama-13b-instruct.Q5_K_M.gguf",
    n_ctx=5000,
    n_gpu_layers=40,
    n_batch=512,
    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
    callback_manager=callback_manager,
    verbose=True,
)