# 5. Create project structure
echo "📂 Setting up project structure..."

mkdir -p app
touch app/__init__.py
touch app/main.py

mkdir -p drafts
mkdir -p graphs
touch .env

mkdir -p drafts
# touch drafts/test.ipynb

# mkdir -p .github
# touch .github/deploy.yml


mkdir -p app/llm_setup
touch app/llm_setup/__init__.py
touch app/llm_setup/llm_setup.py

mkdir -p app/analysts
touch app/analysts/__init__.py
touch app/analysts/analysts.py

mkdir -p app/utils
touch app/utils/__init__.py
touch app/utils/utils.py

mkdir -p app/graph_builder
touch app/graph_builder/__init__.py
touch app/graph_builder/graph_builder.py

mkdir -p app/pdf_generator
touch app/pdf_generator/__init__.py
touch app/pdf_generator/pdf_generator.py

mkdir -p app/tests
touch app/tests/__init__.py
touch app/tests/test_graph.py
touch app/tests/test_graph.py

touch .env
touch Dockerfile

# Write Dockerfile content
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Add the current directory to Python path
ENV PYTHONPATH=/app

# Expose port
EXPOSE 8000

# Run the application
CMD ["streamlit", "run", "app/mainapp.py", "--server.port=8000", "--server.address=0.0.0.0"]
EOF

echo "Dockerfile created successfully"

# 4. Create requirements.txt if not exists & add libraries
if [ ! -f "requirements.txt" ]; then
    echo "📄 Creating requirements.txt..."
    cat <<EOL > requirements.txt
langchain
python-dotenv
langchain_huggingface
langchain-tavily
reportlab
google-api-python-client
google_auth_oauthlib
langchain-openai
streamlit
langchain-groq
pytest
langgraph
EOL
    echo "✅ requirements.txt created with default libraries."
else
    echo "📄 requirements.txt already exists, skipping creation."
fi

set -e  # Exit if any command fails

echo "🚀 Initializing Finance Health Report project with Conda..."
conda create --prefix ./venv python=3.12 -y

# 1. Create Conda environment in local folder (./venv)
if [ ! -d "venv" ]; then
    echo "📦 Creating Conda environment in ./venv ..."
    conda create --prefix ./venv python=3.12 -y
else
    echo "✅ Conda environment already exists in ./venv"
fi

echo "🚀 Creating setup.py file with the Project information as needed..."
touch setup.py

# Create setup.py
echo "📝 Creating setup.py..."
cat > setup.py <<EOL
from setuptools import setup, find_packages

setup(
    name="Routing_Agentic_AI_Workflow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "langchain",
        "langchain-groq",
        "langgraph",
        "python-dotenv",
        "langchain",
        "langchain_huggingface",
        "langchain-tavily",
        "reportlab",
        "google-api-python-client",
        "google_auth_oauthlib",
        "langchain-openai",
        "langchain-groq",
        "pytest"
            ],

    author="Sushant Sur",
    description="ROuting Agentic AI Workflow",
    python_requires=">=3.12",
)
EOL

echo "✅ Setup complete and ready to run! 

echo "✅ Project structure is ready."

echo "⚙️  Installing project in editable mode..."
pip install -e .

#Run the file using the command as ./init.sh in gitbash terminal