# GhostBuster CI/CD: AI Hallucination Guardrail

GhostBuster is a lightweight DevSecOps gate that blocks risky AI-assisted code before deployment.
It validates three high-impact risks:

- Hallucinated dependencies (example: `fake_library`)
- Invalid API usage (example: `non_existent_function()`)
- Suspicious AI-generation patterns in source comments/content

It also generates a clean demo report (`report.txt`) and an executive dashboard (`app.py`) for live presentations.

## Why this solves a real problem

Modern teams increasingly use AI coding assistants. Productivity goes up, but silent mistakes can reach CI/CD:

- Non-existent packages suggested by LLMs
- Wrong or invented API calls
- Unverified pasted code segments

GhostBuster adds an automated checkpoint so only verified code proceeds.

## Project structure

- `sample_code/main.py`: Demo application code
- `validator/dependency_check.py`: Detects hallucinated dependencies
- `validator/api_check.py`: Detects invalid API usage
- `validator/ai_detector.py`: Detects suspicious AI patterns
- `validator/run_all.py`: Orchestrates checks, prints AI risk score, writes `report.txt`
- `.github/workflows/pipeline.yml`: CI pipeline that enforces checks
- `app.py`: Streamlit dashboard for visual demo

## Local setup

```bash
pip install -r requirements.txt
python validator/run_all.py
```

Expected successful output includes:

- `AI Risk Score: <70-95>%`
- `ALL CHECKS PASSED`

After execution, inspect:

- `report.txt`

## Streamlit dashboard

Run:

```bash
streamlit run app.py
```

Dashboard highlights:

- Last build status
- AI risk score metric
- Deployment gate verdict
- Live `report.txt` details for screenshot-ready evidence

## Demo flow (high-impact script)

Use this sequence in front of your evaluator.

### 1) Show normal pipeline success

Push clean code.

What to show:

- GitHub Actions pipeline is green
- `report.txt` shows `Status: PASSED`

What to say:

"Only verified code is allowed into deployment. GhostBuster acts as an AI safety gate inside CI/CD."

### 2) Trigger a controlled failure (wow moment)

Edit `sample_code/main.py` and add:

```python
import fake_library
```

Push again.

What to show:

- Pipeline fails
- Logs contain: `Dependency 'fake_library' does not exist`

What to say:

"GhostBuster detected a hallucinated dependency and automatically blocked deployment."

### 3) Show actionable feedback

Open failed GitHub Actions run logs.

What to show:

- Exact failing reason from validator

What to say:

"We do not just block builds, we provide developer-friendly feedback to fix issues fast."

### 4) Remediate and recover

Remove the fake import and push again.

What to show:

- Pipeline returns to green
- Dashboard status updates to PASSED

What to say:

"The system enforces reliability continuously, so only safe, valid code proceeds."

## Advanced storytelling angle (novel + impactful)

Position GhostBuster as an "AI Code Firewall" for DevSecOps:

- Left shift AI risk checks into CI
- Reduce release incidents caused by generated code
- Improve trust in AI-assisted development
- Keep velocity high with immediate, actionable errors

## Team presentation close

"GhostBuster brings governance to AI-assisted coding without slowing developers down. We convert invisible AI risks into visible pipeline controls and measurable build quality."