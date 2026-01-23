"""
LLM Summarizer Module

Generates weekly paper summaries using a custom LLM endpoint
with OpenAI-compatible API format.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI


def summarize_weekly_papers(
    papers: List[Dict],
    api_base: str,
    api_key: str,
    model: str = "deepseek-chat",
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str:
    """
    Call LLM API to generate a weekly summary of papers.

    Args:
        papers: List of paper dictionaries
        api_base: LLM API base URL (e.g., https://api.deepseek.com)
        api_key: LLM API key
        model: Model name (e.g., "deepseek-chat")
        temperature: Sampling temperature
        max_tokens: Maximum tokens in response

    Returns:
        Generated summary string
    """
    if not papers:
        return "No papers to summarize this week."

    # Build prompt with paper information
    prompt = _build_summary_prompt(papers)

    try:
        response = _call_llm_api(
            api_base=api_base,
            api_key=api_key,
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response

    except Exception as e:
        print(f"Error generating weekly summary: {e}")
        return f"Error generating summary: {str(e)}"


def _build_summary_prompt(papers: List[Dict]) -> str:
    """
    Build a prompt for the LLM summarization task.

    Args:
        papers: List of paper dictionaries

    Returns:
        Prompt string
    """
    prompt = """Please summarize the following research papers for this week.

For each paper, provide a brief summary (1-2 sentences) highlighting the key contribution.
Group related papers together when possible.
Provide a concise weekly overview at the beginning (2-3 sentences).

Format the response in Markdown with the following structure:

## Weekly Overview
[2-3 sentence overview of the week's papers]

## Paper Summaries

### [Paper Title 1]
[Brief summary]

### [Paper Title 2]
[Brief summary]

---

Papers to summarize:

"""

    for i, paper in enumerate(papers, 1):
        prompt += f"\n### Paper {i}\n"
        prompt += f"**Title:** {paper.get('title', 'N/A')}\n"
        prompt += f"**Authors:** {', '.join(paper.get('authors', [])[:5])}\n"
        if paper.get('conference'):
            prompt += f"**Conference:** {paper.get('conference')}\n"
        if paper.get('categories'):
            prompt += f"**Categories:** {', '.join(paper.get('categories', []))}\n"
        prompt += f"**Abstract:** {paper.get('summary', 'N/A')[:500]}...\n"

    return prompt


def _call_llm_api(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict],
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str:
    """
    Call an LLM API with OpenAI-compatible format using OpenAI SDK.

    Args:
        api_base: API base URL (e.g., https://api.deepseek.com)
        api_key: API key
        model: Model name
        messages: List of message dictionaries
        temperature: Sampling temperature
        max_tokens: Maximum tokens in response

    Returns:
        Response content string

    Raises:
        Exception: If the API request fails
    """
    # Create OpenAI client with custom base URL
    client = OpenAI(api_key=api_key, base_url=api_base)

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=False
    )

    return response.choices[0].message.content


def summarize_single_paper(
    paper: Dict,
    api_base: str,
    api_key: str,
    model: str = "deepseek-chat",
    temperature: float = 0.7,
    max_tokens: int = 500
) -> str:
    """
    Generate a summary for a single paper.

    Args:
        paper: Paper dictionary
        api_base: LLM API base URL
        api_key: LLM API key
        model: Model name
        temperature: Sampling temperature
        max_tokens: Maximum tokens in response

    Returns:
        Generated summary string
    """
    prompt = f"""Summarize the following research paper in 2-3 sentences, focusing on the key contribution and method.

**Title:** {paper.get('title', 'N/A')}
**Authors:** {', '.join(paper.get('authors', [])[:5])}
**Abstract:** {paper.get('summary', 'N/A')[:1000]}
"""

    try:
        return _call_llm_api(
            api_base=api_base,
            api_key=api_key,
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
    except Exception as e:
        print(f"Error summarizing paper: {e}")
        return f"Error generating summary: {str(e)}"


def generate_recommendation_comment(
    paper: Dict,
    api_base: str,
    api_key: str,
    model: str = "deepseek-chat",
    temperature: float = 0.8,
    max_tokens: int = 300
) -> str:
    """
    Generate a short recommendation comment for a paper.

    Args:
        paper: Paper dictionary
        api_base: LLM API base URL
        api_key: LLM API key
        model: Model name
        temperature: Sampling temperature (higher for more creative)
        max_tokens: Maximum tokens in response

    Returns:
        Generated recommendation string
    """
    prompt = f"""Write a short, engaging recommendation (2-3 sentences) for why someone should read this paper. Be enthusiastic but honest.

**Title:** {paper.get('title', 'N/A')}
**Abstract:** {paper.get('summary', 'N/A')[:500]}
"""

    try:
        return _call_llm_api(
            api_base=api_base,
            api_key=api_key,
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
    except Exception as e:
        print(f"Error generating recommendation: {e}")
        return f"An interesting paper worth reading!"


def is_summary_day(day_name: str) -> bool:
    """
    Check if the current day is the summary day.

    Args:
        day_name: Day name (e.g., "Friday")

    Returns:
        True if today is the summary day
    """
    from datetime import datetime

    current_day = datetime.now().strftime("%A")
    return current_day.lower() == day_name.lower()


if __name__ == "__main__":
    # Test with DeepSeek API
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if api_key:
        print("Testing DeepSeek API connection...")
        try:
            response = _call_llm_api(
                api_base="https://api.deepseek.com",
                api_key=api_key,
                model="deepseek-chat",
                messages=[{"role": "user", "content": "Hello! Please say 'DeepSeek API is working!' in one sentence."}],
                temperature=0.7,
                max_tokens=100
            )
            print(f"\nAPI Response: {response}")
            print("\nDeepSeek API is working!")
        except Exception as e:
            print(f"\nError: {e}")
    else:
        print("LLM summarizer module loaded.")
        print("Set DEEPSEEK_API_KEY environment variable to test the API.")
