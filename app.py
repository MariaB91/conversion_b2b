import streamlit as st
import pandas as pd
import tempfile
import os
from conversion import convertir_pdf_en_excel_conforama  # Importation du script de conversion

# Sidebar
st.sidebar.title("Sélectionner une entreprise")
company = st.sidebar.selectbox(
    "Choisissez une entreprise:",
    ["Conforama Suisse", "Coformama", "Bon Ami", "But"]
)

# Définir les chemins des fichiers sources (XLSX pour les références)
source_files = {
    "Conforama Suisse": "sources/conforama_suisse.xlsx",
    "Coformama": "sources/coformama.xlsx",
    "Bon Ami": "sources/bon_ami.xlsx",
    "But": "sources/but.xlsx"
}

# Fonction pour afficher un bouton et charger un fichier PDF
def charger_pdf():
    uploaded_file = st.file_uploader("Charger un fichier PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Fichier PDF chargé:", uploaded_file.name)
        return uploaded_file
    return None

# Fonction pour lancer la conversion et permettre le téléchargement automatique
def lancer_conversion(uploaded_file, conversion_function, company_name, source_file):
    if uploaded_file and st.button("Lancer la conversion 🔄"):
        st.write("La conversion est en cours... ⏳")
        
        try:
            # Créer un fichier temporaire pour enregistrer le PDF téléchargé
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
                tmpfile.write(uploaded_file.read())
                pdf_path = tmpfile.name  # Chemin temporaire du fichier PDF

            # Afficher un message pour l'extraction des données du PDF
            st.write("Extraction des données du fichier PDF...")
            
            # Vérifier si le fichier source existe
            if not os.path.exists(source_file):
                raise FileNotFoundError(f"Le fichier source pour {company_name} est manquant.")
            
            # Exécuter la conversion spécifique en utilisant le fichier source XLSX
            output_excel_path = conversion_function(pdf_path, source_file)
            
            # Afficher un message pour l'étape de transformation des données
            st.write("Transformation des données et création du fichier Excel... 🔄")
            
            # Lire le fichier Excel généré pour affichage
            df = pd.read_excel(output_excel_path)
            st.write("Aperçu des données extraites :")
            st.dataframe(df.head())  # Afficher un aperçu du fichier Excel

            # Bouton de téléchargement automatique du fichier Excel
            with open(output_excel_path, "rb") as f:
                st.download_button(
                    label=f"📥 Télécharger le fichier Excel - {company_name}",
                    data=f,
                    file_name=f"resultat_{company_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        except Exception as e:
            st.error(f"Erreur lors de la conversion: {str(e)}")
        
        finally:
            # Nettoyage des fichiers temporaires
            if 'pdf_path' in locals() and os.path.exists(pdf_path):
                os.remove(pdf_path)
            if 'output_excel_path' in locals() and os.path.exists(output_excel_path):
                os.remove(output_excel_path)


# Main content based on the selected company
uploaded_file = charger_pdf()

if company == "Conforama Suisse":
    st.header("Conforama Suisse _ Conversion 🚀")
    lancer_conversion(uploaded_file, convertir_pdf_en_excel_conforama, "ConforamaSuisse", source_files["Conforama Suisse"])
    st.video("https://www.example.com/animation_confo_suisse.mp4")

elif company == "Coformama":
    st.header("Coformama _ Conversion 🛠️")
    # Remplacer par la fonction de conversion spécifique à Coformama si elle existe
    # lancer_conversion(uploaded_file, convertir_pdf_en_excel_coformama, "Coformama", source_files["Coformama"])
    st.video("https://www.example.com/animation_coformama.mp4")

elif company == "Bon Ami":
    st.header("Bon Ami _ Conversion 🏡")
    # Remplacer par la fonction de conversion spécifique à Bon Ami si elle existe
    # lancer_conversion(uploaded_file, convertir_pdf_en_excel_bonami, "BonAmi", source_files["Bon Ami"])
    st.video("https://www.example.com/animation_bon_ami.mp4")

elif company == "But":
    st.header("But _ Conversion 🛋️")
    # Remplacer par la fonction de conversion spécifique à But si elle existe
    # lancer_conversion(uploaded_file, convertir_pdf_en_excel_but, "But", source_files["But"])
    st.video("https://www.example.com/animation_but.mp4")
