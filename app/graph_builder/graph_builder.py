from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage, HumanMessage
from typing_extensions import TypedDict
from app.llm_setup.llm_setup import llm
from app.utils.utils import fetch_competitor_swot_context
from app.analysts.analysts import Perspectives

class ProductLaunchState(TypedDict):
    topic: str
    max_analysts: int
    human_analyst_feedback: str
    analysts: list

analyst_instructions = """
You are tasked with creating AI analyst personas to evaluate a PRODUCT LAUNCH STRATEGY.

Product Launch Topic:
{topic}

Competitor Context:
{web_context}

Human Feedback:
{human_analyst_feedback}

Create up to {max_analysts} analysts, each with:
- SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)
- Step-by-step action plan
- Competitor summary
- Marketing recommendations
Return valid structured data.
"""

def create_analysts(state: ProductLaunchState):
    topic = state.get("topic", "Generic Product Launch")
    max_analysts = state.get("max_analysts", 5)
    feedback = state.get("human_analyst_feedback", "")

    web_context = fetch_competitor_swot_context(topic)
    structured_llm = llm.with_structured_output(Perspectives)

    msg = structured_llm.invoke([
        SystemMessage(content=analyst_instructions.format(
            topic=topic, web_context=web_context,
            human_analyst_feedback=feedback, max_analysts=max_analysts
        )),
        HumanMessage(content="Generate the analyst personas for the product launch.")
    ])
    return {"analysts": msg.analysts}

def human_feedback(state: ProductLaunchState):
    pass

def should_continue(state: ProductLaunchState):
    if state.get("human_analyst_feedback"):
        return "create_analysts"
    return END

def build_graph():
    builder = StateGraph(ProductLaunchState)
    builder.add_node("create_analysts", create_analysts)
    builder.add_node("human_feedback", human_feedback)
    builder.add_edge(START, "create_analysts")
    builder.add_edge("create_analysts", "human_feedback")
    builder.add_conditional_edges("human_feedback", should_continue, ["create_analysts", END])
    memory = MemorySaver()
    return builder.compile(interrupt_before=["human_feedback"], checkpointer=memory)
