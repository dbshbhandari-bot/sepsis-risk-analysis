from data_handler import load_data, clean_data
from risk_calculator import calculate_risk, split_risk
from visualizer import plot_heart_rate, plot_doctors

def main():
    df = load_data()
    df = clean_data(df)
    df = calculate_risk(df)

    high, medium, low = split_risk(df)

    print("High Risk:", len(high))
    print("Medium Risk:", len(medium))
    print("Low Risk:", len(low))

    plot_heart_rate(df)
    plot_doctors(df)
    from risk_calculator import doctor_risk_analysis, ward_risk_analysis


    doctor_analysis = doctor_risk_analysis(df)
    ward_analysis = ward_risk_analysis(df)

    print("\nDoctor Risk Analysis:\n", doctor_analysis)
    print("\nWard Risk Analysis:\n", ward_analysis)
    from pathlib import Path
    from visualizer import plot_doctor_risk

    plot_doctor_risk(doctor_analysis)
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"

    doctor_analysis.to_csv(DATA_DIR / "doctor_risk_analysis.csv")
    ward_analysis.to_csv(DATA_DIR / "ward_risk_analysis.csv")

    print("Doctor & Ward analysis saved!")
    report_file = DATA_DIR / "summary_report.txt"

    with open(report_file, "w") as f:
        f.write("Sepsis Risk Analysis Report\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total Patients: {len(df)}\n")
        f.write(f"High Risk Patients: {len(high)}\n")
        f.write(f"Medium Risk Patients: {len(medium)}\n")
        f.write(f"Low Risk Patients: {len(low)}\n\n")

        f.write("Top Doctors:\n")
        f.write(str(df["Doctor_On_Duty"].value_counts().head()))
        f.write("\n\n")

        f.write("Doctor Risk Breakdown:\n")
        f.write(str(doctor_analysis))

    print("Summary report generated!")

if __name__ == "__main__":
    main()
