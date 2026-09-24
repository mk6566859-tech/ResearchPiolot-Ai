from crewai import Agent, Task, Crew, Process
from llm_config import get_groq_llm
from search_tools import duckduckgo_search

def create_research_agent():
    llm = get_groq_llm()

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
        max_iter=10,
    )
    return researcher


def run_research(topic: str):
    researcher = create_research_agent()

    research_task = Task(
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

    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True,
    )
    return crew.kickoff()
