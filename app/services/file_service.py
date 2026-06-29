
def save_markdown(filename: str, content: str) -> None:
    """
    Save Markdown content into outputs folder.
    """
    path = f"outputs/{filename}"
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    