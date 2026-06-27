from agents.researcher import create_research

topic = input("請輸入今天的主題：")

content = create_research(topic)

with open("outputs/research.md", "w", encoding="utf-8") as file:
    file.write(content)

print("✅ research.md 已建立")