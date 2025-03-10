nous navons pas dout path n  ce script est utilisé dans le script app.py de streamlit pour que une fois le fichier est converti , on affiche un aoercu, et on le telecharge import pdfplumber
import pandas as pd

def extraire_tableaux_du_pdf(pdf_path):
    """
    Extrait les tableaux d'un fichier PDF et les retourne sous forme de DataFrame.
    """
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                tables.append(df)
    return pd.concat(tables, ignore_index=True) if tables else pd.DataFrame()

def convertir_pdf_en_excel(pdf_path, source_xlsx, mapping):
    """
    Effectue la conversion d'un PDF en Excel en appliquant un mapping spécifique.
    """
    # Extraction des données PDF
    df_pdf = extraire_tableaux_du_pdf(pdf_path)
    
    if df_pdf.empty:
        raise ValueError("Aucune donnée trouvée dans le PDF.")
    
    # Nettoyage et transformation des données
    for old_col, new_col in mapping.items():
        if old_col in df_pdf.columns:
            df_pdf.rename(columns={old_col: new_col}, inplace=True)

    # Charger le fichier source pour références éventuelles
    df_source = pd.read_excel(source_xlsx)
    
    # Fusionner ou nettoyer selon le besoin
    # df_pdf = df_pdf.merge(df_source, on="CodeEAN", how="left")  # Exemple si besoin de fusion
    
    # Sauvegarder le fichier converti
    output_path = pdf_path.replace(".pdf", "_converti.xlsx")
    df_pdf.to_excel(output_path, index=False)
    
    return output_path

def convertir_pdf_en_excel_conforama(pdf_path, source_xlsx):
    """
    Conversion spécifique pour Conforama.
    """
    # Mapping des colonnes
    mapping = {
        'QteenUVC': 'Qte',
        'Prixachatbrut\nhsEcoPart': 'PA HT',
        'Libellearticle-CodeEAN': 'Libelle-EAN',
        'Totalprixachatnet': 'Total PA HT'
    }

    # Extraction et transformation des données
    df_pdf = extraire_tableaux_du_pdf(pdf_path)

    if df_pdf.empty:
        raise ValueError("Aucune donnée trouvée dans le PDF.")

    # Supprimer les colonnes inutiles
    columns_a_supprimer = ['Noligne', 'Prixunit.D3E', 'Prixunit.DEA', 'No.O.S.']
    df_pdf.drop(columns=[col for col in columns_a_supprimer if col in df_pdf.columns], inplace=True)

    # Appliquer le renommage
    df_pdf.rename(columns=mapping, inplace=True)

    # Séparer la colonne 'Libelle-EAN' en 'Libelle' et 'EAN'
    if 'Libelle-EAN' in df_pdf.columns:
        df_pdf[['Designation', 'EAN']] = df_pdf['Libelle-EAN'].str.split('-', n=1, expand=True)
        df_pdf.drop(columns=['Libelle-EAN'], inplace=True)

    # Réorganiser les colonnes
    desired_order = ['EAN', 'Article', 'Designation', 'Qte', 'PA HT', 'Total PA HT']
    df_pdf = df_pdf[[col for col in desired_order if col in df_pdf.columns]]

    # Enregistrer le fichier converti
    output_path = pdf_path.replace(".pdf", "_conforama.xlsx")
    df_pdf.to_excel(output_path, index=False)

    return output_path
