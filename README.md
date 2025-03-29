# CrewAI News Writer with Gemini

This project uses the [CrewAI](https://github.com/joaomdmoura/crewai) framework along with **Gemini 1.5 Pro** (via Google Generative AI) to research and write news articles on the latest trends in any topic. The crew consists of two intelligent agents: a **Senior Researcher** and a **News Writer**. The agents collaborate to generate high-quality articles using real-time data from the web.

## Project Structure

```text
.
├── agents.py           # Defines the agents and their configurations
├── crew.py             # Main entrypoint to initialize and run the crew
├── tasks.py            # Defines the research and writing tasks
├── tools.py            # Adds a web search tool using Serper API
├── .env                # Stores API keys securely
└── news_article.md     # Output file with the final news article
```

## Requirements

- Python 3.10+
- CrewAI
- LiteLLM
- Serper.dev API key for real-time search
- python-dotenv

## Installation

1. Clone the repository
```
git clone https://github.com/your-username/crewai-gemini-news.git
cd crewai-gemini-news
```

2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Configure environment variables
Create a .env file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

## Running the Project

Run the script to execute the agent crew:
```
python crew.py
```

By default, the topic is set to:
```python
inputs={"topic": "AI in healthcare"}
```

Modify this line in crew.py to change the topic.

## How It Works

- **LLM Setup**: Uses gemini/gemini-1.5-pro with your Google API key.
- **Senior Researcher**: Gathers recent and relevant news from the web using SerperDevTool.
- **News Writer**: Writes a complete news article based on the research.
- **Execution Flow**: Tasks run sequentially, with memory enabled for contextual continuity.

## Output

The generated article will be saved as:
```
news_article.md
```

Example:
```markdown
# AI in Healthcare: Top Trends of 2025
...
```

## Notes

- You may encounter deprecation warnings from Pydantic v2 — these are safe to ignore for now.
- Ensure the LLM model is correctly specified as:
```python
model="gemini/gemini-1.5-pro"
```

## References

- [CrewAI Documentation](https://docs.crewai.com/)
- [LiteLLM Providers](https://docs.litellm.ai/docs/providers)
- [Google AI - Gemini](https://ai.google.dev/)
- [Serper.dev](https://serper.dev/)
