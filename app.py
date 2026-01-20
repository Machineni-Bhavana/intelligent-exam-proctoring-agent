import streamlit as st
from knowledge_base import RULES
from reasoning_engine import evaluate_risk
from explanation import generate_action

st.title("AI Exam Proctoring Agent")
st.write("Utility-Based Intelligent Agent for Online Exam Monitoring")

st.subheader("Enter Exam Behaviour Details")

# Inputs (Percepts)
tab_switches = st.slider("Number of tab switches", 0, 10, 0)
head_turns = st.slider("Head movement count", 0, 15, 0)
inactive_time = st.slider("Inactive time (seconds)", 0, 300, 0)
multiple_faces = st.checkbox("Multiple faces detected")

if st.button("Evaluate Behaviour"):
    percepts = {
        "tab_switches": tab_switches,
        "head_turns": head_turns,
        "inactive_time": inactive_time,
        "multiple_faces": multiple_faces
    }

    risk_score, reasons = evaluate_risk(percepts, RULES)
    result = generate_action(risk_score, reasons)

    st.subheader("Evaluation Result")
    st.write(f"**Risk Level:** {result['risk_level']}")
    st.write(f"**Confidence:** {result['confidence']} %")
    st.write(f"**Action:** {result['action']}")

    st.subheader("Reasons")
    if reasons:
        for r in reasons:
            st.write("- ", r)
    else:
        st.write("No suspicious behaviour detected")

