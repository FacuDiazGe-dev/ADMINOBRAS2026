import streamlit as st
import gspread
import pandas as pd

from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = dict(st.secrets["gcp_service_account"])

CREDS = Credentials.from_service_account_info(
    creds_dict,
    scopes=SCOPES
)

client = gspread.authorize(CREDS)

SPREADSHEET = client.open_by_key(
    "1sWkC3zvx4ufecZBxLIpCMGo2llsvjuGxl_Putr7iLHA"
)


def get_dataframe(sheet_name):

    sheet = SPREADSHEET.worksheet(sheet_name)

    data = sheet.get_all_records()

    return pd.DataFrame(data)


def append_row(sheet_name, row):

    sheet = SPREADSHEET.worksheet(sheet_name)

    sheet.append_row(row)

def update_obra(
    obra_id,
    nueva_fila
):

    sheet = SPREADSHEET.worksheet("Obras")

    data = sheet.get_all_records()

    for idx, row in enumerate(data, start=2):

        if row["ID_Obr"] == obra_id:

            rango = f"A{idx}:J{idx}"

            sheet.update(
                rango,
                [nueva_fila]
            )

            return True

    return False

def update_contratista(
    contratista_id,
    nueva_fila
):

    sheet = SPREADSHEET.worksheet(
        "Contratistas"
    )

    data = sheet.get_all_records()

    for idx, row in enumerate(data, start=2):

        if row["ID_Con"] == contratista_id:

            rango = f"A{idx}:I{idx}"

            sheet.update(
                rango,
                [nueva_fila]
            )

            return True

    return False
