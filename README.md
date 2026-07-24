# 🤖 AI Test Architect

> An Agentic AI-powered Test Automation Framework built with **LangGraph, OpenAI, Playwright, and Pytest** to autonomously generate, execute, and analyze software tests.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-purple)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 📌 Overview

AI Test Architect is an intelligent test automation framework that transforms a natural language requirement into executable automated tests using AI agents.

Instead of manually writing test cases and automation scripts, the framework orchestrates specialized agents that:

- Understand requirements
- Generate test cases
- Execute browser automation
- Analyze results
- Investigate failures

---

## 🚀 Features

- ✅ Agent-based workflow using LangGraph
- ✅ AI-powered test generation
- ✅ Playwright browser automation
- ✅ Pytest integration
- ✅ Failure analysis
- ✅ Screenshot capture
- ✅ GitHub Actions CI/CD

---

## 🏗️ Architecture

> *(Replace this with a real architecture diagram later.)*

```text
                    User Requirement
                           │
                           ▼
                 ┌─────────────────┐
                 │ Planner Agent   │
                 └─────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Test Generator Agent   │
              └────────────────────────┘
                           │
                           ▼
                 ┌─────────────────┐
                 │ Execution Agent │
                 └─────────────────┘
                           │
                           ▼
             ┌────────────────────────┐
             │ Result Analyzer Agent  │
             └────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────┐
            │ Failure Analyzer Agent  │
            └─────────────────────────┘
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python 3.11 |
| AI | OpenAI, LangGraph |
| Automation | Playwright |
| Testing | Pytest |
| Reporting | Allure |
| CI/CD | GitHub Actions |

---

## 📂 Project Structure

```text
ai-test-architect/
│
├── src/
│   ├── agents/
│   ├── ai/
│   ├── browser.py
│   ├── graph/
│   ├── pages/
│   └── tools/
│
├── tests/
│
├── screenshots/
│
├── .github/
│   └── workflows/
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/mohgermany1606/ai-test-architect.git
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Run Tests

```bash
pytest -v
```

Run a specific workflow

```bash
python -m pytest tests/ai/test_workflow.py -v -s
```

---

## 💡 Example

### Input Requirement

```text
Search Wikipedia for AI
```

### AI Workflow

```text
Requirement
      │
      ▼
Planner
      │
      ▼
Generate Test Case
      │
      ▼
Execute Test
      │
      ▼
Analyze Result
      │
      ▼
Generate Report
```

---

## 📸 Screenshots


Example:

```
screenshots/
    ai_article.png
```

---

## 🔄 CI/CD

GitHub Actions automatically:

- Install dependencies
- Install Playwright browsers
- Execute Pytest
- Publish test results

---

## 🗺️ Roadmap

### ✅ Completed

- Multi-agent architecture
- LangGraph workflow
- AI test generation
- Playwright execution
- Pytest tests
- GitHub Actions pipeline

### 🚧 In Progress

- AI Decision Router
- Self-healing locators
- Memory-enabled agents
- Retry strategy

### 🔮 Future

- Bug report generation
- Jira integration
- Test optimization
- Multi-browser support
- Visual testing
- API testing agent

---

## 👩‍💻 Author

**Mohini Gupta**

## 👩‍💻 Author

**Mohini Gupta**

Senior QA Lead • Test Manager • AI Engineer

Experienced in designing scalable automation frameworks and leading QA teams. Passionate about applying Generative AI and Multi-Agent Systems to transform software testing.

**Tech Stack**

- Python
- Playwright
- Selenium
- Robot Framework
- Appium
- LangGraph
- OpenAI
- CI/CD

---

## ⭐ Contributing

Contributions, ideas, and feedback are welcome.

---

## 📄 License

MIT License