def create_article(topic: str) -> str:
    """
    Generate an article in Markdown format.

    Args:
        topic: The topic provided by the user.

    Returns:
       Markdown formatted article content.
    """

    return f"""# {topic}

Content:
Many learners study English for years but still struggle to speak fluently.

Speaking requires active practice rather than passive listening.

Consistency is the key to long-term improvement.

Start speaking a little every day instead of waiting until you feel ready.
"""