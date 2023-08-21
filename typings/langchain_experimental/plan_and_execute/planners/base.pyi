"""
This type stub file was generated by pyright.
"""

from abc import abstractmethod
from typing import Any, List, Optional
from langchain.callbacks.manager import Callbacks
from langchain.chains.llm import LLMChain
from langchain_experimental.plan_and_execute.schema import Plan, PlanOutputParser
from langchain_experimental.pydantic_v1 import BaseModel

class BasePlanner(BaseModel):
    """Base planner."""
    @abstractmethod
    def plan(self, inputs: dict, callbacks: Callbacks = ..., **kwargs: Any) -> Plan:
        """Given input, decide what to do."""
        ...
    
    @abstractmethod
    async def aplan(self, inputs: dict, callbacks: Callbacks = ..., **kwargs: Any) -> Plan:
        """Given input, asynchronously decide what to do."""
        ...
    


class LLMPlanner(BasePlanner):
    """LLM planner."""
    llm_chain: LLMChain
    output_parser: PlanOutputParser
    stop: Optional[List] = ...
    def plan(self, inputs: dict, callbacks: Callbacks = ..., **kwargs: Any) -> Plan:
        """Given input, decide what to do."""
        ...
    
    async def aplan(self, inputs: dict, callbacks: Callbacks = ..., **kwargs: Any) -> Plan:
        """Given input, asynchronously decide what to do."""
        ...
    

