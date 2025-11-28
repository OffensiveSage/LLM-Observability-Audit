# 🕵️‍♂️ Cracking the Black Box: LLM Observability & Integrity Audit

## ❓ The Security Question
**Can we trust an AI model with critical financial decisions?**

As security professionals, we are trained to never trust a "black box." Yet, we often deploy LLMs without seeing what's happening inside. This project challenges that norm.

We are not just predicting housing prices; we are **auditing the "brain" of Llama-3.3-70b**. By attaching a forensic "flight recorder" (OpenTelemetry), we capture every thought, every token, and every latency spike to answer the ultimate security question: **Is this model hallucinating, or is it reliable?**

---

## 🛡️ The Investigation: AI Security & Forensics

This project demonstrates a complete **AI Observability & Integrity Audit** pipeline. We treat the LLM as a suspect and the traces as our evidence.

### 🔍 What We Uncovered
By instrumenting the model with **Arize Phoenix**, we gained X-Ray vision into its decision-making process:

---

## 🔐 Security & Observability Implications

This project implements core **AI Security (AISec)** concepts:

### 1. LLM Forensics (The "Flight Recorder")
We utilize **Arize Phoenix** to capture full traces of every execution. In a security context, this is critical for:
- **Incident Response**: Reconstructing exactly what input caused a harmful output.
- **Prompt Injection Detection**: Analyzing raw inputs to identify adversarial patterns.
- **Data Leakage Auditing**: Verifying that model responses do not contain PII (Personally Identifiable Information).

### 2. Model Integrity & Hallucination Detection
The `performance_curve.html` visualization serves as an **Integrity Audit**. Significant deviations between AI predictions and ground truth indicate:
- **Model Drift**: The model losing alignment with reality.
- **Hallucinations**: Fabrication of facts, posing a reliability and integrity risk.
- **Adversarial Susceptibility**: Identifying inputs that cause the model to fail catastrophically.

### 3. Automated Red Teaming Infrastructure
The `run_experiment.py` script demonstrates an automated framework for **Batch Auditing**. This same infrastructure can be repurposed to:
- Batch-test the model against **Jailbreak Prompts**.
- Verify compliance with **Safety Policies**.
- Stress-test the model for **Denial of Service (DoS)** resilience.

---

## ✅ Audit Components Completed

### 1. Data Ingestion (The "Test Set")
- **File**: `data/RA_Application_Task.csv`
- **Scope**: 38 records used as the "Ground Truth" for the integrity audit.

### 2. Llama API Integration (The "Subject")
- **Model**: llama-3.3-70b-versatile (Groq)
- **Script**: `run_experiment.py`
- **Action**: 38 AI-generated valuations ($180K-$275K range).

### 3. Integrity Analysis (AI vs Reality)
- **Visualization**: `outputs/performance_curve.html`
- **Data**: `outputs/experiment_results.csv`
- **Finding**: Differences range from -$98K to +$93K, highlighting specific areas of model uncertainty.

### 4. Full Observability (Telemetry)
- **Tool**: Phoenix Dashboard (http://localhost:6006/)
- **Status**: ✅ 38/38 Traces captured. Full visibility into latency, token usage, and prompt chains.

---

## ⚠️ Setup Required: API Key Configuration

**This repository does NOT include API keys.** You must create your own `.env` file locally:

1. Copy the template: `cp .env.example .env`
2. Add your Groq API key to `.env`
3. Get your key from: https://console.groq.com/keys

**Note**: The `.env` file is gitignored and will never be committed to this repository.

---

## Setup Instructions

### 1. Create Virtual Environment
```bash
# Use Python 3.9 or higher (required for arize-phoenix)
python3.9 -m venv .venv39
source .venv39/bin/activate  # On Windows: .venv39\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure API Key
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Groq API key
# Get your key from: https://console.groq.com/keys
```

---

## Quick Start

```bash
# Run the experiment
.venv39/bin/python run_experiment.py

# View Phoenix Dashboard (Forensics)
# Open: http://localhost:6006/

# View Integrity Report
open outputs/performance_curve.html
cat outputs/experiment_results.csv
```

---

## Key Files

| File | Purpose | Security Context |
|------|---------|------------------|
| `TASK_SUMMARY.md` | Complete project report | |
| `run_experiment.py` | Main script | **The Audit Engine** |
| `outputs/performance_curve.html` | Visualization | **Integrity Report** |
| `outputs/experiment_results.csv` | All results with AI estimates | |
| `notebook/experiment_v1.ipynb` | Jupyter notebook version | |
| `.env.example` | Config Template | **Secret Management** |
| `requirements.txt` | Python dependencies | |
| `SECURITY.md` | Security Policy | **Best Practices** |

---

**Audit Status:** ✅ **COMPLETE** - All telemetry captured and integrity verified.
