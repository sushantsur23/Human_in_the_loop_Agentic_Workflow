# Handles LLM and external API setup

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", "")

# Initialize LLM
llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)

# Tavily search
tavily_search = TavilySearch(max_results=5, topic="general")
