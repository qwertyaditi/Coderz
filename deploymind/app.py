import streamlit as st
from model import predict_risk
from models.groq_runner import query_groq
from templates.prompts import make_prompt
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="DeployMind", page_icon="🚀", layout="wide")
st.title("🚀 DeployMind – AI Deployment Risk Checker + LLM Explainer")

# SECTION 1 – Risk Score from Regression Model
st.header("📊 Deployment Risk Score")

lines = st.slider("Lines of Code Changed", 0, 1000, 100)
files = st.slider("Number of Files Changed", 0, 10, 2)
auth = st.checkbox("Touches Authentication Logic?")
config = st.checkbox("Changes Config/Secrets?")
test = st.checkbox("Includes Tests?")

if st.button("🔍 Check Deployment Risk"):
    input_data = [lines, files, int(auth), int(config), int(test)]
    risk = predict_risk(input_data)

    if risk > 0.7:
        st.error(f"🚨 High Risk! Deployment may fail. Risk Score: {risk:.2f}")
    elif risk > 0.4:
        st.warning(f"⚠️ Medium Risk. Proceed with caution. Risk Score: {risk:.2f}")
    else:
        st.success(f"✅ Low Risk. Safe to deploy. Risk Score: {risk:.2f}")

# SECTION 2 – Code File + LLM Explanation
st.header("🧠 Code Vulnerability Explanation via LLM (Groq)")

with st.form("llm_form"):
    vuln_title = st.text_input("Vulnerability Name", value="Prototype Pollution")
    vuln_severity = st.selectbox("Severity", ["low", "medium", "high", "critical"], index=2)
    vuln_cvss = st.number_input("CVSS Score (0–10)", min_value=0.0, max_value=10.0, value=8.2, step=0.1)
    code_file = st.file_uploader("📂 Upload Source Code File", type=["py", "js", "ts", "java", "txt"])
    submitted = st.form_submit_button("🧠 Analyze Code")

if submitted:
    if code_file is None:
        st.warning("Please upload a code file first.")
    else:
        code = code_file.read().decode("utf-8")
        vuln_data = {
            "title": vuln_title,
            "severity": vuln_severity,
            "cvss": vuln_cvss
        }

        with st.spinner("🧠 Calling Groq..."):
            prompt = make_prompt(vuln_data, code)
            result = query_groq(prompt)

        st.success("✅ LLM Analysis Complete")
        st.subheader("📖 Groq's Explanation:")
        st.markdown(result)