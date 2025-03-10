import streamlit as st
from pathlib import Path

# Sidebar
st.sidebar.title("Select a Company")
company = st.sidebar.selectbox(
    "Choose a company:",
    ["Confo Suisse", "Coformama", "Bon Ami", "But"]
)

# Main content based on the selected company
if company == "Confo Suisse":
    st.header("Confo Suisse _ Conversion")
   
elif company == "Coformama":
    st.header("Coformama _ Conversion")
   
elif company == "Bon Ami":
    st.header("Bon Ami _ Conversion")
    
elif company == "But":
    st.header("But _ Conversion")

