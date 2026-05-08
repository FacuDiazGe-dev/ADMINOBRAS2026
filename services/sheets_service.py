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

SPREADSHEET_ID = st.secrets["spreadsheet_id"]

SPREADSHEET = client.open_by_key(
    SPREADSHEET_ID
)


def get_dataframe(sheet_name):

    sheet = SPREADSHEET.worksheet(sheet_name)

    data = sheet.get_all_records()

    return pd.DataFrame(data)


def append_row(sheet_name, row):

    sheet = SPREADSHEET.worksheet(sheet_name)

    sheet.append_row(row)
