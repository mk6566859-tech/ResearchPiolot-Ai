import re
import time

from crewai import Agent, Task, Crew, Process
from llm_config import (
    get_groq_llm,
    get_groq_model_name,
    is_rate_limit_error,
)
from search_tools import duckduckgo_search

def create_research_agent(model_name=None):
    llm = get_groq_llm(model_name)

    researcher = Agent(
        role="Senior Research Analyst",
        goal=(
            "Research the given topic using reliable and recent web sources, "
            "identify important facts and trends, cross-check information where "
            "possible, and produce a well-structured research report."
        ),
        backstory=(
            "You are an experienced research analyst specializing in technology, "
            "business, science, cybersecurity, AI, and emerging topics. You conduct "
            "evidence-based research, distinguish facts from analysis, and never "
            "invent sources or facts."
        ),
        tools=[duckduckgo_search],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=4,
    )
    return researcher


def create_research_task(topic, researcher):
    return Task(
        description=f"""
Conduct comprehensive research on:

"{topic}"

Requirements:
1. Search the web for relevant information.
2. Prioritize recent and credible sources.
3. Look for multiple independent sources.
4. Identify important facts, statistics, trends, developments,
   examples, and expert perspectives.
5. Cross-check important claims when possible.
6. Do not invent information.
7. Clearly identify uncertainty when information conflicts.
8. Keep track of source names and URLs.
9. Focus on useful information rather than filler.

Create a professional Markdown report with:
# Executive Summary
# Introduction
# Key Findings
# Detailed Analysis
# Current Trends
# Challenges and Limitations
# Future Outlook
# Conclusion
# Sources

For Sources, provide source title, publisher/website, and URL whenever available.
""",
        expected_output="""
A comprehensive Markdown research report containing Executive Summary,
Introduction, Key Findings, Detailed Analysis, Current Trends,
Challenges and Limitations, Future Outlook, Conclusion, and Sources.
The report must be factual, organized, readable, and supported by web research.
""",
        agent=researcher,
    )


def run_research(topic: str):
    configured_model = get_groq_model_name()
    for attempt in range(3):
        try:
            researcher = create_research_agent(configured_model)
            crew = Crew(
                agents=[researcher],
                tasks=[create_research_task(topic, researcher)],
                process=Process.sequential,
                verbose=True,
            )
            return crew.kickoff()
        except Exception as error:
            if not is_rate_limit_error(error) or attempt == 2:
                raise

            wait_seconds = get_rate_limit_wait(error)
            time.sleep(wait_seconds)


def get_rate_limit_wait(error):
    match = re.search(r"try again in ([\d.]+)s", str(error), re.IGNORECASE)
    if match:
        return min(float(match.group(1)) + 0.5, 30)
    return 5
