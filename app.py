import streamlit as st
from generator import generate_test_cases
import hashlib
import pandas as pd

st.set_page_config(page_title="AI Test Case Generator", layout="centered")
st.title("🧪 MyFluent AI Test Case Generator")

# Detect input type
def detect_input_type(text: str) -> str:
    if text.strip().startswith("mutation") or text.strip().startswith("query") or "{" in text:
        return "graphql"
    elif "As a user" in text or "Given" in text:
        return "story"
    else:
        return "unknown"

# UI components
test_depth = st.selectbox("Select test depth", ["Simple", "Detailed", "Edge-heavy"])
user_input = st.text_area("Paste a user story or GraphQL mutation", height=200)

# Generate test cases
if st.button("Generate Test Cases!"):
    if user_input.strip():
        with st.spinner("Generating test cases..."):
            input_type = detect_input_type(user_input)

            # Customize prompt depending on input type
            if input_type == "graphql":
                context = "This is a GraphQL mutation or query. Generate test cases for API validation, edge cases, and response handling"
            else:
                context = "This is a user story or requirement. Generate relevant functional test cases."

            # Add detail level
            if test_depth == "Detailed":
                context += " Include validations, boundary values and some exploratory cases."
            elif test_depth == "Edge-heavy":
                context += " Focus on rare edge cases, invalid data, and unexpected inputs."

            # Generate test cases
            output = generate_test_cases(user_input, context)

            # Display
            st.markdown("### Generated Test Cases")
            test_cases = [case.strip() for case in output.split("\n\n") if case.strip()]
            for i, case in enumerate(test_cases, start=1):
                with st.expander(f"Test Case {i}"):
                    st.markdown(case)

            if len(test_cases) > 1:
                df = pd.DataFrame([{"Test Case": c} for c in test_cases])
                csv = df.to_csv(index=False)
                st.download_button("Download as CSV", csv, file_name="test_cases.csv", mime="text/csv")
    else:
        st.warning("Please enter a user story or GraphQL mutation.")
