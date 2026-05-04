import os
from dotenv import load_dotenv
import pandas as pd
from langchain_groq import ChatGroq # Yeh library AI se baat karne ke liye hai
from langchain_core.prompts import PromptTemplate # Yeh AI ko 'Role' dene ke liye hai

load_dotenv()
# 1. AI Model Setup (Yahan hum 'Brain' choose kar rahe hain)
# Groq fast hai isliye hum ise use kar rahe hain
llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))

def analyze_machine_health(row):
    """
    Yeh function har ek sensor reading par 'Mechanical Reasoning' lagayega.
    Input: Data ki ek row (Temp, Vibration, Flow)
    """
    
    # 2. Humne manual ka knowledge yahan 'Hardcode' kiya hai (RAG ka chota roop)
    
    manual_context = """
    Normal Temp: 50-75°C | Normal Vibration: < 3.5 | Normal Flow: > 40
    If Temp > 80: Lubrication Issue. If Vib > 4: Alignment Issue.
    """
    
    # 3. AI ko batana ki uska kaam kya hai (Prompt Engineering)
    
    prompt = f"""
    You are an Industrial Expert System. Analyze these sensor readings:
    Temperature: {row['temp']}°C
    Vibration: {row['vibration']} mm/s
    Flow Rate: {row['flow']} m3/h
    
    Reference Manual: {manual_context}
    
    Task: Give a 1-sentence diagnostic and action plan.
    """
    
    # 4. AI se jawab mangna
    response = llm.invoke(prompt)
    return response.content

# --- TEST KARNE KE LIYE ---
if __name__ == "__main__":
    # Cleaned data load karo
    df = pd.read_csv('data/cleaned_sensor_data.csv')
    
    # Sirf pehli row test karte hain
    print("🤖 AI is analyzing the first data point...")
    result = analyze_machine_health(df.iloc[0])
    print(f"Result: {result}")