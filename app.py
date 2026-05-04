import os
import streamlit as st
import pandas as pd
import plotly.express as px
# Humne pipeline_manager se graph ko import kiya
from src.pipeline_manager import app as langgraph_pipeline

# Page Setup
st.set_page_config(page_title="Industrial Digital Twin", layout="wide")

st.title("🏗️ Agentic Digital Twin: Industrial Pump Monitor")
st.write("Real-time Sensor Analysis & AI Diagnostics using LangGraph")

# --- SIDEBAR SECTION ---
st.sidebar.header("🕹️ Pipeline Controls")
st.sidebar.write("Click below to start the AI analysis flow.")

# Button click hone par hi pipeline chalegi
run_button = st.sidebar.button("Run Full Pipeline")

if run_button:
    with st.spinner("🛠️ LangGraph Nodes Working..."):
        # Initial input for the pipeline
        inputs = {"raw_data_path": "src/data/raw_sensor_data.csv"}
        
        # Pure flow ko execute karna
        result = langgraph_pipeline.invoke(inputs)
        
        st.sidebar.success("✅ Analysis Complete!")
        st.sidebar.subheader("🤖 AI Diagnostic Report:")
        st.sidebar.info(result['diagnostic_report'])

# --- MAIN DASHBOARD SECTION ---
st.divider()

# Check ki kya data file bani hai?
if os.path.exists('src/data/cleaned_sensor_data.csv'):
    df = pd.read_csv('src/data/cleaned_sensor_data.csv')

    # Visualizing Data in 2 Columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡️ Temperature Trend")
        fig_temp = px.line(df, x='timestamp', y='temp', 
                          title="Temperature vs Time", line_shape="spline", color_discrete_sequence=['red'])
        st.plotly_chart(fig_temp, use_container_width=True)

    with col2:
        st.subheader("🔀 Vibration Analysis")
        fig_vib = px.line(df, x='timestamp', y='vibration', 
                         title="Vibration vs Time", line_shape="spline", color_discrete_sequence=['orange'])
        st.plotly_chart(fig_vib, use_container_width=True)

    # Health Gauges (Latest Reading)
    st.divider()
    st.subheader("📊 Latest Machine Status")
    last_row = df.iloc[-1]
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Current Temperature", f"{round(last_row['temp'], 2)} °C")
    m2.metric("Vibration Level", f"{round(last_row['vibration'], 2)} mm/s")
    m3.metric("System Status", "Analyzed" if run_button else "Waiting")

else:
    # Agar file nahi hai toh ye dikhega
    st.warning("⚠️ No processed data found. Please use the sidebar button to 'Run Full Pipeline' and generate the Digital Twin view.")
    st.info("💡 Tip: Backend par pehle data clean hoga, phir AI use analyze karega, tabhi yahan graphs dikhenge.")