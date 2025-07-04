# MyFluent AI Test Case Generator - Hackathon 2025

## 🎯 Project Overview

### Team Information
- **Team Name**: MyFluent Hackers
- **Project Name**: MyFluent AI Test Case Generator
- **Team Members**: 
  - [Toby Broadbent] - QA
  - [Pietro Macedo] - QA
  - [Erika Vilvorder] - Software Dev

### Project Description
A one-click AI-powered tool to generate functional and edge-case test scenarios or product owner-style acceptance criteria (in BDD format) from user stories or GraphQL/API requests. It helps teams speed up QA documentation and improve collaboration between developers, testers, and product managers.

### Problem Statement
QA and product teams spend significant time manually writing test cases or acceptance criteria from user stories, ticket descriptions, or GraphQL queries. This is time-consuming, error-prone, and repetitive — especially in fast-paced agile teams.

### Solution Approach
We built an intuitive Streamlit app that uses OpenAI's GPT-3.5 to auto-generate test cases or BDD-style acceptance criteria based on user input. It detects the type of content (GraphQL, user story, etc.), adjusts prompt context accordingly, and returns structured output. It also supports CSV export for seamless team integration.

## 🛠️ Technical Stack

### Technologies Used
- **Frontend**: Streamlit (Python-based UI)
- **Backend**: Python (OpenAI API)
- **Database**: None (Stateless, ephemeral use)
- **Cloud Services**: Optional deployment on Streamlit Cloud
- **Other Tools**: 
  - OpenAI GPT-3.5
  - dotenv for API key management
  - Pandas for CSV export


### Prerequisites
- Python 3.9+
- OpenAI account + API Key
- Dependencies (`pip install streamlit openai python-dotenv`)

### Installation Steps
1. Clone the repository
2. CD to the repo and run "python -m venv venv"
3. Run "source venv/Scripts/activate to turn on the virtual environment
4. Run the web app using "streamlit run app.py"

