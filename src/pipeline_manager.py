import os
from typing import TypedDict
from langgraph.graph import StateGraph, END

# --- YE HAI TERA CHALLENGE SOLUTION ---
# Humne dusri files se functions import kiye
from src.data_cleaner import clean_industrial_data 
from src.agent_engine import analyze_machine_health
import pandas as pd

# 1. State ki definition (Wahi rahegi)
class AgentState(TypedDict):
    raw_data_path: str
    cleaned_data_present: bool
    diagnostic_report: str

# 2. Logic Nodes (Ab isme asali functions call honge)

def clean_data_node(state: AgentState):
    print("🛠️ Node 1: Cleaning Data...")
    # Asali cleaning function call kiya jo humne pehle banaya tha
    clean_industrial_data(state['raw_data_path']) 
    return {"cleaned_data_present": True}

def analyze_data_node(state: AgentState):
    print("🤖 Node 2: AI Analyzing...")
    # Cleaned data ko load karo
    df = pd.read_csv('src/data/cleaned_sensor_data.csv')
    
    # Sirf latest reading (aakhri row) ko analyze karo
    latest_reading = df.iloc[-1] 
    report = analyze_machine_health(latest_reading)
    
    return {"diagnostic_report": report}

# 3. Graph Workflow Setup (Wahi rahega)
workflow = StateGraph(AgentState)
workflow.add_node("cleaner", clean_data_node)
workflow.add_node("analyzer", analyze_data_node)

workflow.set_entry_point("cleaner")
workflow.add_edge("cleaner", "analyzer")
workflow.add_edge("analyzer", END)

app = workflow.compile()

# --- PIPELINE KO CHALANE KA TARIKA ---
if __name__ == "__main__":
    print("🚀 Starting Industrial Digital Twin Pipeline...")
    
    # Shuruati data dena (Initial State)
    inputs = {"raw_data_path": "data/raw_sensor_data.csv"}
    
    # Pura flow ek baar mein chalega
    final_state = app.invoke(inputs)
    
    print("\n--- FINAL INDUSTRIAL REPORT ---")
    print(final_state['diagnostic_report'])