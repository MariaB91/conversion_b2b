import pdfplumber
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

    # Appliquer le renommage des colonnes selon le mapping
    df_pdf.rename(columns=mapping, inplace=True)

    # Séparer la colonne 'Libelle-EAN' en 'Designation' et 'EAN' si elle existe
    if 'Libelle-EAN' in df_pdf.columns:
        df_pdf[['Designation', 'EAN']] = df_pdf['Libelle-EAN'].str.split('-', n=1, expand=True)
        df_pdf.drop(columns=['Libelle-EAN'], inplace=True)

    # Réorganiser les colonnes dans l'ordre désiré
    desired_order = ['EAN', 'Article', 'Designation', 'Qte', 'PA HT', 'Total PA HT']
    df_pdf = df_pdf[[col for col in desired_order if col in df_pdf.columns]]

    # Enregistrer le fichier converti au format Excel
    output_path = pdf_path.replace(".pdf", "_conforama.xlsx")
    df_pdf.to_excel(output_path, index=False)

    return output_path
