# 🏗️ Agentic Digital Twin: Industrial Pump Monitor

A sophisticated **Industry 4.0** project that combines Mechanical Engineering domain knowledge with **Agentic AI** to perform real-time sensor monitoring and predictive maintenance diagnostics.

## 🌟 Overview
This project simulates a "Digital Twin" of an industrial pump. It captures raw sensor data (Temperature & Vibration), processes it through a modular pipeline, and uses a Large Language Model (LLM) acting as a "Senior Maintenance Engineer" to provide health reports.

## 🛠️ Tech Stack
- **Orchestration:** [LangGraph](https://www.langchain.com/langgraph) (for stateful, multi-node agent workflows)
- **AI Brain:** [Llama 3.3-70b](https://groq.com/) (via Groq API for low-latency inference)
- **Dashboard:** [Streamlit](https://streamlit.io/) & [Plotly](https://plotly.com/) (for real-time data visualization)
- **Data Handling:** Pandas & Python-dotenv
- **Development Environment:** Google Project IDX

## 🚀 Key Features
- **Automated Data Pipeline:** A 2-node LangGraph workflow that ensures data is cleaned before analysis.
- **AI-Powered Diagnostics:** Goes beyond simple threshold alerts by using LLMs to interpret trends and suggest specific maintenance actions (e.g., lubrication, alignment check).
- **Industrial Dashboard:** Real-time visualization of Temperature and Vibration trends with automated status metrics.
- **Secure Architecture:** Professional handling of API keys and environment variables.

## 📂 Project Structure
```bash
Agentic_Digital_Twin/
├── src/
│   ├── data/                 # Raw and processed CSV data
│   ├── agent_engine.py       # Groq/LLM logic
│   ├── data_cleaner.py       # Data processing logic
│   ├── pipeline_manager.py   # LangGraph workflow definition
├── app.py                    # Streamlit Dashboard UI
├── .env                      # API Keys (Excluded from Git)
└── requirements.txt          # Project dependencies

## Installation & Setup
1. Clone the repo:
git clone [https://github.com/Moh123S/Agentic_Digital_Twin.git](https://github.com/Moh123S/Agentic_Digital_Twin.git)

2. Install dependencies:
pip install streamlit pandas plotly langgraph langchain-groq python-dotenv

3. Set up environment variables: .env

4. Run the Dashboard:
streamlit run app.py

