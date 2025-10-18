from app.llm_setup.llm_setup import tavily_search
import re

def _trim(txt: str, limit: int = 500) -> str:
    if not txt:
        return ""
    return (txt[:limit] + "...") if len(txt) > limit else txt

def fetch_competitor_swot_context(topic: str) -> str:
    queries = [
        f"{topic} competitors and alternatives",
        f"{topic} leading competitors market strategy",
        f"{topic} competitor SWOT and product positioning",
    ]
    snippets = []
    for q in queries:
        try:
            results = tavily_search.invoke({"query": q})
        except Exception:
            continue
        if not results or not results.get("results"):
            continue
        for r in results["results"]:
            content = r.get("content", "")
            title = r.get("title", "Unknown Source")
            url = r.get("url", "")
            if content:
                snippets.append(f"- {title} ({url})\n{_trim(content, 600)}")
    return "\n".join(snippets) if snippets else "No competitor info found."
