from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()
import os

# Define your LLM
llm = LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-1.5-pro",
    temperature=0.5,
    verbose=True
)

# create a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground-breaking news in the field of {topic}",
    llm=llm,
    verbose=True,
    memory=True,
    backstory="You are a senior researcher with a knack for finding the most important news in a given topic",
    tools=[tool],
    allow_delegation=True
)

# create a news writer agent with custome tools responsible for writing the news
news_writer = Agent(
    role="News Writer",
    goal="Write a news article about the most important news in the field of {topic}",
    llm=llm,
    verbose=True,
    memory=True,
    backstory="You are a news writer with a knack for writing engaging and informative news articles",
    tools=[tool],
    allow_delegation=False # we don't want to delegate the writing task
)
 