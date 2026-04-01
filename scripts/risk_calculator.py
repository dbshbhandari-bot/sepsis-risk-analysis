def calculate_risk(df):
    df["Risk_Score"] = (
        (df["Heart_Rate"] > 100).astype(int) +
        (df["WBC_Count"] > 12).astype(int) +
        (df["Lactate_mmol_L"] > 2).astype(int)
    )
    return df

def split_risk(df):
    high = df[df["Risk_Score"] == 3]
    medium = df[df["Risk_Score"] == 2]
    low = df[df["Risk_Score"] <= 1]
    return high, medium, low
def doctor_risk_analysis(df):
    result = df.groupby(["Doctor_On_Duty", "Risk_Score"]).size().unstack(fill_value=0)
    return result

def ward_risk_analysis(df):
    result = df.groupby(["Ward", "Risk_Score"]).size().unstack(fill_value=0)
    return result