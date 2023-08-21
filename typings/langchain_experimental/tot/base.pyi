"""
This type stub file was generated by pyright.
"""

from typing import Any, List, Optional, Type
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain_experimental.tot.checker import ToTChecker
from langchain_experimental.tot.controller import ToTController
from langchain_experimental.tot.memory import ToTDFSMemory
from langchain_experimental.tot.thought import Thought
from langchain_experimental.tot.thought_generation import BaseThoughtGenerationStrategy

"""
This a Tree of Thought (ToT) chain based on the paper "Large Language Model
Guided Tree-of-Thought"

https://arxiv.org/pdf/2305.08291.pdf

The Tree of Thought (ToT) chain uses a tree structure to explore the space of
possible solutions to a problem.

"""
class ToTChain(Chain):
    """
    A Chain implementing the Tree of Thought (ToT).
    """
    llm: BaseLanguageModel
    checker: ToTChecker
    output_key: str = ...
    k: int = ...
    c: int = ...
    tot_memory: ToTDFSMemory = ...
    tot_controller: ToTController = ...
    tot_strategy_class: Type[BaseThoughtGenerationStrategy] = ...
    verbose_llm: bool = ...
    class Config:
        """Configuration for this pydantic object."""
        extra = ...
        arbitrary_types_allowed = ...
    
    
    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, **kwargs: Any) -> ToTChain:
        """
        Create a ToTChain from a language model.

        :param llm: The language model to use.
        :param kwargs: Additional arguments to pass to the ToTChain constructor.
        """
        ...
    
    def __init__(self, **kwargs: Any) -> None:
        ...
    
    @property
    def input_keys(self) -> List[str]:
        """Will be whatever keys the prompt expects.

        :meta private:
        """
        ...
    
    @property
    def output_keys(self) -> List[str]:
        """Will always return text key.

        :meta private:
        """
        ...
    
    def log_thought(self, thought: Thought, level: int, run_manager: Optional[CallbackManagerForChainRun] = ...) -> None:
        ...
    


