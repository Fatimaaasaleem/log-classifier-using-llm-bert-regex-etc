# Log Classification with Hybrid Classification Framework

A hybrid log classification system that combines three complementary approaches to handle varying levels of complexity in log patterns.

---

## Classification Approaches

**1. Regular Expressions (Regex)**
Handles simple, predictable patterns using predefined rules.

**2. Sentence Transformer + Logistic Regression**
Manages complex patterns when sufficient labeled training data is available. Generates embeddings via Sentence Transformers and classifies them using Logistic Regression.

**3. Large Language Models (LLM)**
A fallback for complex patterns where labeled training data is scarce or unavailable.

---

## Folder Structure

| Path | Description |
|------|-------------|
| `training/` | Training code for Sentence Transformer + Logistic Regression, and regex-based classification |
| `models/` | Saved models, including Sentence Transformer embeddings and the Logistic Regression model |
| `resources/` | Resource files such as test CSVs, output files, and images |
| `server.py` | FastAPI server (root directory) |

---

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Start the server**
```bash
uvicorn server:app --reload
```

The API will be available at:
- `http://127.0.0.1:8000/` — Main endpoint
- `http://127.0.0.1:8000/docs` — Swagger UI
- `http://127.0.0.1:8000/redoc` — ReDoc documentation

---

## Usage

Upload a CSV file to the classification endpoint. The file must contain the following columns:

- `source`
- `log_message`

The API returns the same CSV with an additional `target_label` column containing the predicted classification for each log entry.
