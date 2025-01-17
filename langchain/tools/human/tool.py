"""Tool for asking human input."""

from typing import Callable

from pydantic import Field

from langchain.tools.base import BaseTool


def _print_func(text: str) -> None:
    print("\n")
    print(text)


class HumanInputRun(BaseTool):
    """Tool that adds the capability to ask user for input."""

    name = "Human"
    description = (
        "You can ask a human for guidance when you think you "
        "got stuck or you are not sure what to do next, but try the ai bot first."
        "Engage the human to perform an action you cannot perform."
        "The input should be a question or action item for the human."

    )
    prompt_func: Callable[[str], None] = Field(default_factory=lambda: _print_func)
    input_func: Callable = Field(default_factory=lambda: input)

    def _run(self, query: str) -> str:
        """Use the Human input tool."""
        self.prompt_func(query)
        return self.input_func()

    async def _arun(self, query: str) -> str:
        """Use the Human tool asynchronously."""
        raise NotImplementedError("Human tool does not support async")
