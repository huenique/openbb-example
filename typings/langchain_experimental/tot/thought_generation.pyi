"""
This type stub file was generated by pyright.
"""

from abc import abstractmethod
from typing import Any, Dict, List, Tuple
from langchain.chains.llm import LLMChain
from langchain.prompts.base import BasePromptTemplate

"""
We provide two strategies for generating thoughts in the Tree of Thoughts (ToT)
framework to avoid repetition:

These strategies ensure that the language model generates diverse and
non-repeating thoughts, which are crucial for problem-solving tasks that require
exploration.
"""
class BaseThoughtGenerationStrategy(LLMChain):
    """
    Base class for a thought generation strategy.
    """
    c: int = ...
    @abstractmethod
    def next_thought(self, problem_description: str, thoughts_path: Tuple[str, ...] = ..., **kwargs: Any) -> str:
        """
        Generate the next thought given the problem description and the thoughts
        generated so far.
        """
        ...
    


class SampleCoTStrategy(BaseThoughtGenerationStrategy):
    """
    Sample thoughts from a Chain-of-Thought (CoT) prompt.

    This strategy works better when the thought space is rich, such as when each
    thought is a paragraph. Independent and identically distributed samples
    lead to diversity, which helps to avoid repetition.
    """
    prompt: BasePromptTemplate = ...
    def next_thought(self, problem_description: str, thoughts_path: Tuple[str, ...] = ..., **kwargs: Any) -> str:
        ...
    


class ProposePromptStrategy(BaseThoughtGenerationStrategy):
    """
    Propose thoughts sequentially using a "propose prompt".

    This strategy works better when the thought space is more constrained, such
    as when each thought is just a word or a line. Proposing different thoughts
    in the same prompt completion helps to avoid duplication.
    """
    prompt: BasePromptTemplate = ...
    tot_memory: Dict[Tuple[str, ...], List[str]] = ...
    def next_thought(self, problem_description: str, thoughts_path: Tuple[str, ...] = ..., **kwargs: Any) -> str:
        ...
    

