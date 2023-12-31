"""
This type stub file was generated by pyright.
"""

from langchain.schema.language_model import BaseLanguageModel
from langchain_experimental.plan_and_execute.planners.base import LLMPlanner
from langchain_experimental.plan_and_execute.schema import Plan, PlanOutputParser

SYSTEM_PROMPT = ...
class PlanningOutputParser(PlanOutputParser):
    """Planning output parser."""
    def parse(self, text: str) -> Plan:
        ...
    


def load_chat_planner(llm: BaseLanguageModel, system_prompt: str = ...) -> LLMPlanner:
    """
    Load a chat planner.

    Args:
        llm: Language model.
        system_prompt: System prompt.

    Returns:
        LLMPlanner
    """
    ...

