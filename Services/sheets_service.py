import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file(
    "data/credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(CREDS)

SPREADSHEET = client.open("AdminObrasDB")


def get_dataframe(sheet_name):
    sheet = SPREADSHEET.worksheet(sheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)


def append_row(sheet_name, row):
    sheet = SPREADSHEET.worksheet(sheet_name)
    sheet.append_row(row)
