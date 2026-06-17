import pandas as pd
import streamlit as st

st.set_page_config(page_title="Payroll Validation Bot")

st.title("Payroll Validation Bot")
st.subheader("HR Payroll Exception Detection System")

df = pd.read_csv("data/payroll_data.csv")

st.write("### Employee Dataset")
st.dataframe(df)

exceptions = []

# Missing Fields Check
for column in ["EmployeeID", "Name", "Department", "Monthly_Salary"]:
    missing_rows = df[df[column].isnull()]

    for _, row in missing_rows.iterrows():
        exceptions.append([
            row["EmployeeID"],
            row["Name"],
            f"Missing {column}"
        ])

# Duplicate EmployeeID Check
duplicate_rows = df[df["EmployeeID"].duplicated()]

for _, row in duplicate_rows.iterrows():
    exceptions.append([
        row["EmployeeID"],
        row["Name"],
        "Duplicate EmployeeID"
    ])

# Sudden Salary Jump Check
for _, row in df.iterrows():

    if pd.notnull(row["Previous_Month_Salary"]) and pd.notnull(row["Monthly_Salary"]):

        increase_percent = (
            (row["Monthly_Salary"] - row["Previous_Month_Salary"])
            / row["Previous_Month_Salary"]
        ) * 100

        if increase_percent > 30:
            exceptions.append([
                row["EmployeeID"],
                row["Name"],
                "Sudden Salary Jump"
            ])

# Create Exception Report
report_df = pd.DataFrame(
    exceptions,
    columns=[
        "EmployeeID",
        "Employee Name",
        "Issue"
    ]
)

st.write("### Exception Report")
st.dataframe(report_df)

# Save Report
report_df.to_csv(
    "reports/exception_report.csv",
    index=False
)

st.success("Exception Report Generated Successfully")