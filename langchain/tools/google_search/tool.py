"""Tool for the Google search API."""

from langchain.tools.base import BaseTool
from langchain.utilities.google_search import GoogleSearchAPIWrapper


class GoogleSearchRun(BaseTool):
    """Tool that adds the capability to query the Google search API."""

    name = "Google Search"
    description = (
        "A wrapper around Google Search. "
        "Useful for when you need to answer questions about current events. "
        "Input should be a search query."
    )
    api_wrapper: GoogleSearchAPIWrapper

    def _run(self, query: str) -> str:
        """Use the tool."""
        return self.api_wrapper.run(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("GoogleSearchRun does not support async")


class GoogleSearchResults(BaseTool):
    """Tool that has capability to query the Google Search API and get back json."""

    name = "Google Search Results JSON"
    description = (
        "A wrapper around Google Search. "
        "Use only for when you need to answer questions about current events, or when you need to validate a fact. Otherwise rely on your own knowledge. "
        "Input should be a search query. Output is a JSON array of the query results"
    )
    num_results: int = 4
    api_wrapper: GoogleSearchAPIWrapper

    def _run(self, query: str) -> str:
        """Use the tool."""
        return str(self.api_wrapper.results(query, self.num_results))

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("GoogleSearchRun does not support async")
