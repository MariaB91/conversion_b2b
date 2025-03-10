import streamlit as st

# Sidebar
st.sidebar.title("Select a Company")
company = st.sidebar.selectbox(
    "Choose a company:",
    ["Confo Suisse", "Coformama", "Bon Ami", "But"]
)

# Main content based on the selected company
if company == "Confo Suisse":
    st.header("Confo Suisse Details")
    st.write("Here is the information for Confo Suisse...")
elif company == "Coformama":
    st.header("Coformama Details")
    st.write("Here is the information for Coformama...")
elif company == "Bon Ami":
    st.header("Bon Ami Details")
    st.write("Here is the information for Bon Ami...")
elif company == "But":
    st.header("But Details")
    st.write("Here is the information for But...")

