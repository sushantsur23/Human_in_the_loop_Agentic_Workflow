# Human_in_the_loop_Agentic_Workflow

### 🚀 Product Launch AI — Agentic Workflow with Streamlit, LangGraph & Groq

## 📘 Overview
**Product Launch AI** is an intelligent, agentic system that generates multi-perspective **analyst personas** to evaluate a new **product launch strategy**.

Each AI analyst provides:
- Competitor-based **SWOT analysis**
- **Step-by-step action plans**
- **Market and competitor insights**
- **Actionable marketing recommendations**

The system runs multiple analysts (agents) in **parallel**, aggregates their output, and allows users to **refine the analysis interactively** using feedback — all powered by **LangGraph**, **Groq LLMs**, and **Streamlit**.

---

## 🏗️ Architecture

```mermaid
graph TD
    A[User Input via Streamlit UI] --> B[LangGraph State Manager]
    B --> C1[Analyst Creation Node]
    B --> C2[Human Feedback Node]
    C1 --> D[Competitor Context Fetch (Tavily API)]
    D --> E[Structured SWOT Generation via Groq LLM]
    E --> F[Analyst Personas (Pydantic Models)]
    F --> G[PDF Report Generator (ReportLab)]
    G --> H[Streamlit Visualization & Download]
    H --> I[Feedback Refinement Loop]




🧩 Tech Stack

| Layer               | Technology                                                |
| ------------------- | --------------------------------------------------------- |
| 🧠 LLM              | [Groq Qwen3-32B](https://groq.com)                        |
| 🔄 Orchestration    | [LangGraph](https://python.langchain.com/docs/langgraph/) |
| 🌐 Search Context   | [Tavily Search API](https://tavily.com)                   |
| 🧱 UI               | [Streamlit](https://streamlit.io)                         |
| 🗂️ PDF Engine      | [ReportLab](https://www.reportlab.com)                    |
| 🧮 Data Validation  | [Pydantic](https://docs.pydantic.dev/)                    |
| 🐳 Containerization | Docker (Python 3.12)                                      |


📂 Project Structure

product_launch_ai/
│
├── app/
│   ├── mainapp.py              # Streamlit UI + workflow integration
│   ├── llm_setup/              # LLM setup (Groq, Tavily configuration)
│   │   └── llm_init.py
│   ├── analysts/               # Analyst and persona logic
│   │   └── analysts.py
│   ├── pdf_generator/          # PDF report creation (ReportLab)
│   │   └── generator.py
│   ├── graph_generator/        # LangGraph agent workflow
│   │   └── graph_build.py
│   └── __init__.py
│
├── graphs/
│   └── product_launch_graph.png  # Saved architecture graph
│
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md



⚙️ Setup & Installation
1️⃣ Clone the Repository

```bash
git clone https://github.com/sushantsur23/Human_in_the_loop_Agentic_Workflow.git
cd product_launch_ai
```

2️⃣ Create a Python Virtual Environment
```bash
./init.sh
```

3️⃣ Install Dependencies
This will happen together in the previous command itself.

4️⃣ Configure Environment Variables

Create a .env file at the root of your project and fill in the following keys:
```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

▶️ Running the Application Locally

Start the Streamlit app:

```bash
streamlit run app/mainapp.py
```


🐳 Running with Docker
Step 1 — Build the Docker Image

```bash
docker build -t product-launch-ai:latest .
```

Step 2 — Run the Docker Container

```bash
docker run -p 8000:8000 --env-file .env product-launch-ai:latest
```

Now open your browser to:
👉 http://localhost:8000

| Input       | Example                                                                        |
| ----------- | ------------------------------------------------------------------------------ |
| **Product** | “AI-powered Fitness Wearable Watch”                                            |
| **Goal**    | Drive early access sign-ups and awareness                                      |
| **Output**  | 4 analyst personas with SWOT analysis, competitor insights, and marketing plan |
| **Export**  | Analyst Report as downloadable PDF                                             |

🧠 Core Features

✅ Multi-Agent Analysis — Each agent acts as a specialized strategist.

✅ SWOT & Competitor Insight — Grounded in live search data.

✅ Interactive Refinement — Regenerate improved analyst reports based on your feedback.

✅ Structured LLM Outputs — Schema-validated JSON ensures accuracy.

✅ PDF Export — Beautiful, structured analyst report.

✅ Docker Ready — Consistent and reproducible deployments.

📊 Example Workflow

1. Enter product launch details and strategic brief.

2. Generate Analysts — Agents analyze competitor data and produce SWOTs.

3. Review and study each analyst's insights.

4. Provide Feedback — Add your feedback to refine analysts further.

5. Download final, polished analyst report as PDF.

🌟 Support

If this project helps you, please ⭐ Star the repo and share it with others in the community!