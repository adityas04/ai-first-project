import os

folders = [
    "agents",
    "tools",
    "workflows",
    "configs",
    "data/input",
    "data/output",
    "tests"
]

files = {
    "agents/__init__.py": "",
    "agents/task_agent.py": "# Define your task agent here\n",
    "tools/__init__.py": "",
    "tools/search_tool.py": "# Search tool implementation\n",
    "workflows/__init__.py": "",
    "workflows/langgraph_workflow.py": "# LangGraph workflow logic\n",
    "configs/__init__.py": "",
    "configs/settings.py": "# Configuration settings\n",
    "configs/prompt_templates.yaml": "# Add prompt templates\n",
    "tests/__init__.py": "",
    "tests/test_agents.py": "# Tests for agents\n",
    "main.py": "# Entry point\n",
    "requirements.txt": "# Add dependencies here\n",
    ".env": "# Add your environment variables here\n",
    "README.md": "# Project README\n"
}

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
