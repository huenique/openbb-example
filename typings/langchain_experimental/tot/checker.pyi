"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from typing import List, Tuple
from langchain.chains.base import Chain
from langchain_experimental.tot.thought import ThoughtValidity

class ToTChecker(Chain, ABC):
    """
    Tree of Thought (ToT) checker.

    This is an abstract ToT checker that must be implemented by the user. You
    can implement a simple rule-based checker or a more sophisticated
    neural network based classifier.
    """
    output_key: str = ...
    @property
    def input_keys(self) -> List[str]:
        """The checker input keys.

        :meta private:
        """
        ...
    
    @property
    def output_keys(self) -> List[str]:
        """The checker output keys.

        :meta private:
        """
        ...
    
    @abstractmethod
    def evaluate(self, problem_description: str, thoughts: Tuple[str, ...] = ...) -> ThoughtValidity:
        """
        Evaluate the response to the problem description and return the solution type.
        """
        ...
    

