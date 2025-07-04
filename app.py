import streamlit as st
from generator import generate_test_cases
import hashlib
import pandas as pd

st.set_page_config(page_title ="AI Test Case Generator", layout="centered")
st.title("🧪 MyFluent AI Test Case Generator")

#detecting if its a graph query or a user story
def detect_input_type(text: str) -> str:
    if text.strip().startswith("mutation") or text.strip().startswith("query") or "{" in text:
        return "graphql"
    elif "As a user" in text or "Given" in text:
        return "story"
    else: return "unknown"
    
#test depth selector
test_depth = st.selectbox("Select test depth", ["Simple", "Detailed", "Edge-heavy"])
#page input
user_input = st.text_area("Paste a user story or GraphQL mutation", height=200)

#generate button
if st.button("Generate Test Cases!"):
    if user_input.strip():
        with st.spinner("Generating test cases..."):
            input_type = detect_input_type(user_input)
            
