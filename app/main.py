from agents.researcher import create_research
from agents.writer import create_article

topic = input("請輸入今天的主題：")

research_content = create_research(topic)

with open("outputs/research.md", "w", encoding="utf-8") as file:
    file.write(research_content)

print("✅ research.md 已建立")

article_content = create_article(topic)

with open("outputs/article.md", "w", encoding="utf-8") as file:
    file.write(article_content)

print("✅ article.md 已建立")