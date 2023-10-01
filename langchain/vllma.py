from typing import Any, Dict, List, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import BaseLLM
from langchain.llms.openai import BaseOpenAI
from langchain.pydantic_v1 import Field, root_validator
from langchain.schema.output import Generation, LLMResult
from langchain.llms.vllm import VLLM

llm = VLLM(model="/nfs_beijing/sikai/weight/llama/llama-7b-chat/",
           trust_remote_code=True,  # mandatory for hf models
           max_new_tokens=128,
           top_k=10,
           top_p=0.95,
           temperature=0.8,
)

print(llm("What is the capital of France ?"))