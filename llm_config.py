import streamlit as st
from crewai import LLM


class GroqLLM(LLM):
    """CrewAI LLM adapter that removes its internal cache marker for Groq."""

    def _format_messages_for_provider(self, messages):
        cleaned_messages = [
            {
                key: value
                for key, value in message.items()
                if key != "cache_breakpoint"
            }
            for message in messages
        ]
        return super()._format_messages_for_provider(cleaned_messages)


def get_groq_llm():
    api_key = st.secrets.get("GROQ_API_KEY")
    model_name = st.secrets.get("GROQ_MODEL", "openai/gpt-oss-120b")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to .streamlit/secrets.toml."
        )

    return GroqLLM(
        model=f"groq/{model_name}",
        api_key=api_key,
        temperature=0.2,
        reasoning_effort="medium",
    )
