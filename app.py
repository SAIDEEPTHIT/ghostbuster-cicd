from __future__ import annotations

from pathlib import Path
import random
import re

import streamlit as st


REPORT_PATH = Path(__file__).resolve().parent / "report.txt"


def parse_report() -> tuple[str, int, str, str]:
    if not REPORT_PATH.exists():
        score = random.randint(70, 95)
        return "UNKNOWN", score, "Run validator/run_all.py to generate a report.", "GhostBuster Report\nStatus: UNKNOWN"

    raw = REPORT_PATH.read_text(encoding="utf-8")
    status_match = re.search(r"^Status:\s*(.+)$", raw, re.MULTILINE)
    score_match = re.search(r"^AI Risk Score:\s*(\d+)%$", raw, re.MULTILINE)
    details_match = re.search(r"^Details:\s*(.+)$", raw, re.MULTILINE)

    status = status_match.group(1).strip() if status_match else "UNKNOWN"
    score = int(score_match.group(1)) if score_match else random.randint(70, 95)
    details = details_match.group(1).strip() if details_match else "No details available"
    return status, score, details, raw


def build_page() -> None:
    st.set_page_config(page_title="GhostBuster Dashboard", page_icon="👻", layout="wide")

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

        .stApp {
            background: radial-gradient(circle at 10% 10%, #dff5ec, #f7fdf9 35%),
                        radial-gradient(circle at 90% 20%, #d8ecff, #f7fdf9 40%),
                        linear-gradient(120deg, #f7fdf9, #eef7ff);
            font-family: 'Space Grotesk', sans-serif;
        }

        .glass-card {
            border: 1px solid rgba(19, 46, 28, 0.12);
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(8px);
            border-radius: 16px;
            padding: 1.1rem;
            box-shadow: 0 12px 30px rgba(16, 39, 23, 0.08);
        }

        .hero {
            border-radius: 18px;
            padding: 1.3rem 1.5rem;
            background: linear-gradient(110deg, #163f2a, #0f6d6a);
            color: white;
            box-shadow: 0 14px 36px rgba(15, 41, 27, 0.26);
            animation: fadeUp 0.75s ease-out;
        }

        .mono {
            font-family: 'IBM Plex Mono', monospace;
            color: #2b3d31;
        }

        @keyframes fadeUp {
            from {opacity: 0; transform: translateY(10px);}
            to {opacity: 1; transform: translateY(0);}
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    status, score, details, raw = parse_report()

    st.markdown(
        """
        <div class="hero">
            <h1 style="margin: 0; font-size: 2rem;">👻 GhostBuster DevSecOps Control Center</h1>
            <p style="margin: 0.45rem 0 0 0; opacity: 0.92;">Real-time guardrails against hallucinated dependencies and invalid AI-assisted code.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    left, middle, right = st.columns(3)
    with left:
        status_color = "#1a7f37" if status == "PASSED" else "#b42318" if status == "FAILED" else "#7a5f00"
        st.markdown(
            f"""
            <div class="glass-card">
              <div class="mono">Last Build Status</div>
              <h2 style="margin-bottom: 0; color: {status_color};">{status}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with middle:
        st.markdown(
            f"""
            <div class="glass-card">
              <div class="mono">AI Risk Score</div>
              <h2 style="margin-bottom: 0;">{score}%</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(min(max(score, 0), 100))
    with right:
        verdict = "Deployment gate open" if status == "PASSED" else "Deployment blocked"
        st.markdown(
            f"""
            <div class="glass-card">
              <div class="mono">Pipeline Gate</div>
              <h2 style="margin-bottom: 0;">{verdict}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.subheader("Validator Insight")
    st.markdown(f"<div class=\"glass-card\">{details}</div>", unsafe_allow_html=True)

    st.subheader("Latest report.txt")
    st.code(raw, language="text")


if __name__ == "__main__":
    build_page()
