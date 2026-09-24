from crewai.tools import tool
from duckduckgo_search import DDGS


@tool("DuckDuckGo Web Search")
def duckduckgo_search(query: str) -> str:
    """Search the web using DuckDuckGo and return relevant results."""

    try:
        results = DDGS().text(
            query,
            region="wt-wt",
            safesearch="moderate",
            max_results=5,
        )

        if not results:
            return "No search results found."

        formatted = []

        for result in results:
            title = result.get("title", "No title")
            url = result.get("href", "")
            body = result.get("body", "")

            formatted.append(
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Summary: {body}"
            )

        return "\n\n---\n\n".join(formatted)

    except Exception as e:
        return f"Web search failed: {e}"