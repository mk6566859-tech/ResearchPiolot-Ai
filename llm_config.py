import streamlit as st
from crewai import LLM

DEFAULT_MODEL = "openai/gpt-oss-120b"


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


def get_groq_llm(model_name=None):
    api_key = st.secrets.get("GROQ_API_KEY")
    model_name = model_name or st.secrets.get(
        "GROQ_MODEL", DEFAULT_MODEL
    )

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to .streamlit/secrets.toml."
        )

    llm_options = {
        "model": f"groq/{model_name}",
        "api_key": api_key,
        "temperature": 0.2,
        "max_tokens": 800,
    }
    if model_name.startswith("openai/gpt-oss"):
        llm_options["reasoning_effort"] = "low"

    return GroqLLM(**llm_options)


def get_groq_model_name():
    return st.secrets.get("GROQ_MODEL", DEFAULT_MODEL)


def is_rate_limit_error(error):
    message = str(error).lower()
    return (
        "ratelimit" in message
        or "rate limit" in message
        or "tokens per minute" in message
    )
