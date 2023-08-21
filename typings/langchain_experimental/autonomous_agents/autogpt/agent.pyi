"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from langchain.chains.llm import LLMChain
from langchain.chat_models.base import BaseChatModel
from langchain.schema import BaseChatMessageHistory
from langchain.tools.base import BaseTool
from langchain.tools.human.tool import HumanInputRun
from langchain.vectorstores.base import VectorStoreRetriever
from langchain_experimental.autonomous_agents.autogpt.output_parser import BaseAutoGPTOutputParser

class AutoGPT:
    """Agent class for interacting with Auto-GPT."""
    def __init__(self, ai_name: str, memory: VectorStoreRetriever, chain: LLMChain, output_parser: BaseAutoGPTOutputParser, tools: List[BaseTool], feedback_tool: Optional[HumanInputRun] = ..., chat_history_memory: Optional[BaseChatMessageHistory] = ...) -> None:
        ...
    
    @classmethod
    def from_llm_and_tools(cls, ai_name: str, ai_role: str, memory: VectorStoreRetriever, tools: List[BaseTool], llm: BaseChatModel, human_in_the_loop: bool = ..., output_parser: Optional[BaseAutoGPTOutputParser] = ..., chat_history_memory: Optional[BaseChatMessageHistory] = ...) -> AutoGPT:
        ...
    
    def run(self, goals: List[str]) -> str:
        ...
    


