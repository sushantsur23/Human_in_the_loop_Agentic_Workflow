import streamlit as st
from app.graph_builder.graph_builder import build_graph
from app.pdf_generator.pdf_generator import generate_pdf

st.set_page_config(layout="wide")
st.title("🚀 Product Launch Strategy — AI Analyst Panel")

graph = build_graph()
thread = {"configurable": {"thread_id": "launch-001"}}

if "analysts" not in st.session_state:
    st.session_state["analysts"] = []
if "refined" not in st.session_state:
    st.session_state["refined"] = []
    
topic = st.text_input("📌 Product Launch Topic", "Launch of AI-powered Fitness Wearable Watch")

# User Input — Only one field: Product Brief
brief = st.text_area(
    "📝 Product Launch Brief (includes goals, target users, and features)",
    value=(
        "AI-powered Smart Fitness Band: Goal is to attract early adopters and fitness enthusiasts with "
        "AI coaching, recovery insights, and app integration. Competitors include Fitbit and Garmin. "
        "Target audience: tech-savvy millennials seeking personalized fitness solutions."
    ),
    height=180
)

max_analysts = st.slider("👥 Analysts to Generate", 2, 6, 4)

# Step 1: Generate Analysts
if st.button("🔍 Generate Analysts"):
    st.session_state["analysts"].clear()
    input_state = {"topic": brief, "max_analysts": max_analysts}
    for event in graph.stream(input_state, thread, stream_mode="values"):
        analysts = event.get("analysts", [])
        if analysts:
            st.session_state["analysts"] = analysts

if st.session_state["analysts"]:
    st.subheader("📊 Generated Analysts")
    for a in st.session_state["analysts"]:
        st.markdown(a.persona)
        st.markdown("---")

    pdf = generate_pdf(st.session_state["analysts"], "Product Launch Report")
    st.download_button("💾 Download Analyst Report", pdf, "analyst_report.pdf")

# Step 2: Feedback Loop
st.markdown("### ✍️ Refine Analysts with Feedback")
feedback = st.text_area(
    "Provide feedback to refine the analyst personas",
    placeholder="e.g., Include pricing strategy specialist or influencer marketing perspective."
)
if st.button("✨ Refine Analysts"):
    if not feedback.strip():
        st.warning("Please enter feedback before refining.")
    else:
        update = {"topic": brief, "max_analysts": max_analysts, "human_analyst_feedback": feedback}
        graph.update_state(thread, update, as_node="human_feedback")
        for event in graph.stream(update, thread, stream_mode="values"):
            analysts = event.get("analysts", [])
            if analysts:
                st.session_state["refined"] = analysts

if st.session_state["refined"]:
    st.subheader("🧠 Refined Analysts After Feedback")
    for a in st.session_state["refined"]:
        st.markdown(a.persona)
        st.markdown("---")

    pdf_ref = generate_pdf(st.session_state["refined"], "Refined Analyst Report")
    st.download_button("💾 Download Refined Report", pdf_ref, "refined_analyst_report.pdf")
