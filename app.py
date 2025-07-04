import streamlit as st
from generator import generate_test_cases
import hashlib
import pandas as pd

st.set_page_config(page_title ="AI Test Case Generator", layout="centered")
st.title("AI Test Case Generator")

