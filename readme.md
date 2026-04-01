# 🧠 Sepsis Risk Analysis System

**Author:** Dibash Bhandari

Project Overview

This project analyzes patient health data to identify individuals at risk of sepsis. It performs data cleaning, risk scoring, and generates insights through visualizations and reports.

The goal of this project is to demonstrate practical skills in:

* Python programming
* Data analysis
* Data visualization
* Project structuring (modular code)

---

## ⚙️ Area i have focused on :

* Data cleaning (removal of invalid values)
* Risk score calculation based on:

  * Heart Rate
  * White Blood Cell Count (WBC)
  * Lactate levels
* Patient categorization:

  * High Risk
  * Medium Risk
  * Low Risk
* Doctor-wise and Ward-wise risk analysis
* Automatic CSV report generation
* Graphical visualization of patient data

---

## 📂 MY  Project Structure

```
Sepsis_Risk_Analysis/
├─ data/
│   ├─ Sepsis_Dataset.csv
│   ├─ High_Risk_Patients.csv
│   ├─ Medium_Risk_Patients.csv
│   ├─ Low_Risk_Patients.csv
│   ├─ doctor_risk_analysis.csv
│   ├─ ward_risk_analysis.csv
│   └─ summary_report.txt
│
├─ scripts/
│   ├─ main.py
│   ├─ data_handler.py
│   ├─ risk_calculator.py
│   └─ visualizer.py
│
├─ images/
│   ├─ heart_rate.png
│   ├─ wbc_count.png
│   └─ doctor_risk_distribution.png
│
└─ README.md
```

---

## ▶️ How to Run

1. Open terminal in the project root directory
2. Run the following command:

```bash
python scripts/main.py
```

---

## 📊 Output

After running this project, the system will:

* Generate categorized CSV files for patient risk levels
* Produce doctor and ward analysis reports
* Save visual graphs in the `images/` folder
* Create a summary report (`summary_report.txt`)

---

## 🧠 Key information to learn 

* Working with real-world healthcare datasets
* Applying condition-based risk modeling
* Structuring Python projects professionally
* Automating analysis pipelines

---

## 🚀 Future plan , my future aim 

* Add machine learning model for prediction
* Build a web dashboard (Streamlit)
* Integrate real-time hospital data

---

## 📎 Dataset 

Dataset sourced from Kaggle (for learning purposes)

---

## 💡 Note

This project is built for educational and portfolio purposes to demonstrate practical data analysis and Python programming skills.
thank you 