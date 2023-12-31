"""
This type stub file was generated by pyright.
"""

from typing import List
from langchain.tools.base import BaseTool

FINISH_NAME = ...
class PromptGenerator:
    """A class for generating custom prompt strings.

    Does this based on constraints, commands, resources, and performance evaluations.
    """
    def __init__(self) -> None:
        """Initialize the PromptGenerator object.

        Starts with empty lists of constraints, commands, resources,
        and performance evaluations.
        """
        ...
    
    def add_constraint(self, constraint: str) -> None:
        """
        Add a constraint to the constraints list.

        Args:
            constraint (str): The constraint to be added.
        """
        ...
    
    def add_tool(self, tool: BaseTool) -> None:
        ...
    
    def add_resource(self, resource: str) -> None:
        """
        Add a resource to the resources list.

        Args:
            resource (str): The resource to be added.
        """
        ...
    
    def add_performance_evaluation(self, evaluation: str) -> None:
        """
        Add a performance evaluation item to the performance_evaluation list.

        Args:
            evaluation (str): The evaluation item to be added.
        """
        ...
    
    def generate_prompt_string(self) -> str:
        """Generate a prompt string.

        Returns:
            str: The generated prompt string.
        """
        ...
    


def get_prompt(tools: List[BaseTool]) -> str:
    """Generates a prompt string.

    It includes various constraints, commands, resources, and performance evaluations.

    Returns:
        str: The generated prompt string.
    """
    ...

