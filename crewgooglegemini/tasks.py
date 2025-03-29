from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

research_task = Task(
    description="Research the latest trends in {topic}",
    expected_output="A list of the latest trends in {topic}",
    agent=news_researcher,
    tools=[tool] 
)

write_task = Task(
    description="Write a news article about the most important news in the field of {topic}",
    expected_output="A news article about the most important news in the field of {topic}",
    agent=news_writer,
    tools=[tool],
    async_execution=False,
    output_file="news_article.md"
)
