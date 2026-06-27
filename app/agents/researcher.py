def create_research(topic: str) -> str:
    """
    Generate a research document in Markdown format.

    Args:
        topic: The topic provided by the user.

    Returns:
        Markdown formatted research content.
    """

    return f"""# Research

Topic:
{topic}

Key Points

- Speaking requires active practice.
- Listening alone is not enough.
- Consistency is important.
"""