# 🧠 CrewAI News Writer with Gemini

This project uses the [CrewAI](https://github.com/joaomdmoura/crewai) framework along with **Gemini 1.5 Pro** (via Google Generative AI) to research and write news articles on the latest trends in any topic. The crew consists of two intelligent agents: a **Senior Researcher** and a **News Writer**. The agents collaborate to generate high-quality articles using real-time data from the web.

## 📁 Project Structure

.
├── agents.py           # Defines the agents and their configurations
├── crew.py             # Main entrypoint to initialize and run the crew
├── tasks.py            # Defines the research and writing tasks
├── tools.py            # Adds a web search tool using Serper API
├── .env                # Stores API keys securely
└── news_article.md     # Output file with the final news article

## 🛠️ Requirements

- Python 3.10+
- OpenAI-compatible LLM API (Google Gemini via [LiteLLM](https://docs.litellm.ai))
- [Serper.dev](https://serper.dev) API key for real-time web search

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/crewai-gemini-news.git
cd crewai-gemini-news

	2.	Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

	3.	Install dependencies

pip install -r requirements.txt

	4.	Add your API keys

Create a .env file in the root directory with the following content:

GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key

🚀 Running the Project

To execute the agent crew and generate a news article on a chosen topic:

python crew.py

The default topic is set to "AI in healthcare". You can modify it in crew.py:

result = crew.kickoff(inputs={"topic": "AI in healthcare"})

🧠 How It Works
	•	LLM Setup (LLM): Configured with Gemini 1.5 Pro for powerful text generation.
	•	Agent 1 - Senior Researcher: Searches for the latest trends using Serper.dev.
	•	Agent 2 - News Writer: Writes a high-quality news article based on the findings.
	•	Process: Sequential execution with optional memory and tool support.

✅ Output

The generated article will be saved in:

news_article.md

⚠️ Notes
	•	You might see warnings from Pydantic v2 — they are safe to ignore for now.
	•	Make sure your model name is prefixed with the provider, e.g. gemini/gemini-1.5-pro.

📚 References
	•	CrewAI Documentation
	•	LiteLLM Providers
	•	Google Gemini
	•	Serper.dev

📄 License

MIT License — feel free to fork and customize!

Let me know if you want me to generate a `requirements.txt` or add a badge/header section for GitHub!