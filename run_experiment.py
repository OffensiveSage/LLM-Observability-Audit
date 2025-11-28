import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import phoenix as px_app
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor


load_dotenv('.env')

print("🚀 Launching Phoenix Dashboard...")
session = px_app.launch_app()
print(f"🌍 Phoenix Dashboard is running at: {session.url}")

from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

tracer_provider = trace_sdk.TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:6006/v1/traces")))
trace_api.set_tracer_provider(tracer_provider)

LlamaIndexInstrumentor().instrument()
print("✅ LlamaIndex instrumentation enabled")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ API Key missing! Check your .env file.")


llm = Groq(model="llama-3.3-70b-versatile", api_key=api_key)
print(f"✅ Setup Complete. Dashboard running at: {session.url}")

try:
    df = pd.read_csv('data/RA_Application_Task.csv')
    print(f"✅ Loaded {len(df)} housing records.")
except FileNotFoundError:
    print("❌ Error: Could not find the CSV file. Please check the 'data' folder.")
    exit(1)

def get_ai_estimate(row):
    """
    Sends home details to Llama 3 and extracts a price.
    """
    prompt = (
        f"You are a professional real estate appraiser. Analyze this specific property and provide a realistic market value estimate.\n\n"
        f"Property Details:\n"
        f"- Bedrooms: {row['Bedrooms']}\n"
        f"- Bathrooms: {row['Bathrooms Comparable']}\n"
        f"- Lot Size: {row['LotSize Comparable']} square feet\n"
        f"- Year Built: {row['YearBuilt Comparable']}\n\n"
        f"Consider the property's age, size, and features. Older homes (1920s-1950s) typically have lower values than newer ones. "
        f"Larger lots and more bathrooms increase value. Provide your best estimate of the fair market value.\n\n"
        f"IMPORTANT: Respond with ONLY a number (no dollar signs, commas, or text). Example: 245000"
    )
    
    try:
        response = llm.complete(prompt)
        price_text = response.text.strip().replace('$', '').replace(',', '').replace('.', '')
        # Extract just the number
        import re
        numbers = re.findall(r'\d+', price_text)
        if numbers:
            return float(numbers[0])
        return np.nan
    except Exception as e:
        print(f"⚠️  Error processing row: {e}")
        return np.nan

print("🚀 Starting AI Valuation (This takes about 30-60 seconds)...")


df['AI_Estimated_Value'] = df.apply(get_ai_estimate, axis=1)


df['Estimation_Diff'] = df['AI_Estimated_Value'] - df['Comparable Sale Price']


results = df.dropna(subset=['AI_Estimated_Value'])


fig = go.Figure()
fig.add_trace(go.Scatter(x=results.index, y=results['Comparable Sale Price'],
                         mode='lines+markers', name='Actual Price', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=results.index, y=results['AI_Estimated_Value'],
                         mode='lines+markers', name='AI Estimate', line=dict(color='red', dash='dot')))

fig.update_layout(title="Llama 3 vs. Actual Market Prices", xaxis_title="House ID", yaxis_title="Price ($)")


os.makedirs('outputs', exist_ok=True)


fig.write_html("outputs/performance_curve.html")
results.to_csv("outputs/experiment_results.csv", index=False)

print("\n🎉 SUCCESS!")
print(f"1. Observability Dashboard: {session.url} (Click this for traces!)")
print(f"2. Graph Saved: outputs/performance_curve.html")
print(f"3. Results CSV: outputs/experiment_results.csv")
print("\n📊 Dashboard will remain running. Press Ctrl+C to stop.")

try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n👋 Shutting down Phoenix Dashboard...")
