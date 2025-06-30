# Blood Test Report Analyser - Debugged Version

This project is a FastAPI application that uses CrewAI agents to analyze blood test reports and provide recommendations.

---

## Bugs Found and How They Were Fixed

**1️⃣ Incorrect and deprecated imports**

- **Problem:** `from crewai.agents import Agent` failed.
- **Fix:** Corrected to `from crewai import Agent`.
- **Problem:** `OpenAIGPT` was deprecated.
- **Fix:** Removed `OpenAIGPT` and used default LLM configuration.

**2️⃣ Tasks missing required parameters**

- **Problem:** `expected_output` was missing in Tasks.
- **Fix:** Added `expected_output` descriptions to all tasks.

**3️⃣ Tools were functions instead of BaseTool instances**

- **Problem:** Tools were declared as functions, causing validation errors.
- **Fix:** Converted tools to classes inheriting from `BaseTool`.

**4️⃣ Dependency conflicts**

- **Problem:** Incompatible versions of `pydantic` and `openai`.
- **Fix:** Updated `requirements.txt` to compatible versions.

**5️⃣ Missing dependencies**

- **Problem:** `python-multipart` was missing, causing FastAPI upload errors.
- **Fix:** Installed `python-multipart`.

**6️⃣ API key handling**

- **Problem:** `.env` was not created or ignored.
- **Fix:** Added `.env` with your OpenAI key and included `.env` in `.gitignore`.

**7️⃣ Uvicorn reload issues**

- **Problem:** Running `main.py` directly with `reload=True` caused errors.
- **Fix:** Switched to using `uvicorn main:app` from CLI.

---

## Setup and Usage Instructions

You can set up the project in **two ways**:

---

### Method 1: Clone the Repository (Recommended)

1️⃣ Clone the project

```bash
git clone https://github.com/ashwin-muralidharan/Blood-Test-Analyser---Debug-.git
cd Blood-Test-Analyser---Debug-
```

2️⃣ Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4️⃣ Create `.env` file with your OpenAI API key

**How to Get Your API Key:**

- Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys)
- Sign in or create a free account
- Click "Create new secret key"
- Copy the key (it starts with `sk-...`)
- Create a file named `.env` in your project folder and add:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5️⃣ Run the application

```bash
python main.py

uvicorn main:app --host 0.0.0.0 --port 8000
```

✅ Visit [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

---

### Method 2: Download Source Code as ZIP

1️⃣ Download ZIP from GitHub

- Go to the repository page  
  [https://github.com/ashwin-muralidharan/Blood-Test-Analyser---Debug-](https://github.com/ashwin-muralidharan/Blood-Test-Analyser---Debug-)
- Click **Code > Download ZIP**
- Extract the ZIP

2️⃣ Open terminal in the extracted folder

3️⃣ Create and activate a virtual environment (see Method 1)

4️⃣ Install dependencies (see Method 1)

5️⃣ Create `.env` file (see Method 1)

6️⃣ Run the application (see Method 1)

---

## API Documentation

Once running, visit:

[http://localhost:8000/docs](http://localhost:8000/docs)

You will see Swagger UI, where you can:

✅ Upload a PDF blood test report  
✅ Enter a query (e.g., _"Summarise my Blood Test Report"_)  
✅ Receive structured recommendations

---

## Note

- This project requires a valid OpenAI API key.
- Use `pip freeze > requirements.txt` if you modify dependencies.
