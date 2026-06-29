from agents.researcher import create_research
from agents.writer import create_article
from services.file_service import save_markdown

topic = input("請輸入今天的主題：")
research_content = create_research(topic)
filename = "research.md"
save_markdown(filename,research_content)

print("✅ research.md 已建立")

article_content = create_article(topic)
filename = "article.md"
save_markdown(filename,article_content)

print("✅ article.md 已建立")