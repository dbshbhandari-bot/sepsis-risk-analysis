from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "Sepsis_Dataset.csv"

def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

def clean_data(df):
    df = df[df["WBC_Count"] >= 0]
    df = df[df["Lactate_mmol_L"] >= 0]
    return df