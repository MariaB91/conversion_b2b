import streamlit as st
from pathlib import Path

# Sidebar
st.sidebar.title("Sélectionner une entreprise")
company = st.sidebar.selectbox(
    "Choisissez une entreprise:",
    ["Confo Suisse", "Coformama", "Bon Ami", "But"]
)

# Fonction pour afficher un bouton et charger un fichier PDF
def charger_pdf():
    uploaded_file = st.file_uploader("Charger un fichier PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("PDF chargé:", uploaded_file.name)
        return uploaded_file
    return None

# Fonction pour lancer la conversion (simulée ici)
def lancer_conversion():
    if st.button("Lancer la conversion 🔄"):
        st.write("La conversion est en cours... ⏳")
        # Ajouter ici la logique de conversion
        st.write("Conversion terminée! ✅")

# Main content based on the selected company
if company == "Confo Suisse":
    st.header("Confo Suisse _ Conversion 🚀")
    charger_pdf()
    lancer_conversion()
    st.video("https://www.example.com/animation_confo_suisse.mp4")  # Exemple de vidéo d'effet spécial

elif company == "Coformama":
    st.header("Coformama _ Conversion 🛠️")
    charger_pdf()
    lancer_conversion()
    st.video("https://www.example.com/animation_coformama.mp4")  # Exemple de vidéo d'effet spécial

elif company == "Bon Ami":
    st.header("Bon Ami _ Conversion 🏡")
    charger_pdf()
    lancer_conversion()
    st.video("https://www.example.com/animation_bon_ami.mp4")  # Exemple de vidéo d'effet spécial

elif company == "But":
    st.header("But _ Conversion 🛋️")
    charger_pdf()
    lancer_conversion()
    st.video("https://www.example.com/animation_but.mp4")  # Exemple de vidéo d'effet spécial
