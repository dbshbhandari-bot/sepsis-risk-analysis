import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

def plot_heart_rate(df):
    plt.hist(df["Heart_Rate"], bins=20)
    plt.title("Heart Rate Distribution")
    plt.savefig(IMAGES_DIR / "heart_rate.png")
    plt.close()

def plot_doctors(df):
    df["Doctor_On_Duty"].value_counts().plot(kind="bar")
    plt.title("Patients per Doctor")
    plt.savefig(IMAGES_DIR / "doctors.png")
    plt.close()


def plot_doctor_risk(doctor_analysis):
        doctor_analysis.plot(kind="bar", stacked=True)
        plt.title("Doctor Risk Distribution")
        plt.xlabel("Doctor")
        plt.ylabel("Number of Patients")
        plt.legend(title="Risk Score")
        plt.tight_layout()
        plt.savefig(IMAGES_DIR / "doctor_risk_distribution.png")
        plt.close()