import pandas as pd
import streamlit as st

st.set_page_config(page_title="Payroll Validation Bot")

st.title("Payroll Validation Bot")

st.write("Upload monthly payroll records as a CSV file.")

st.write("The bot will:")
st.write("• Detect missing fields")
st.write("• Detect duplicate Employee IDs")
st.write("• Detect sudden salary jumps")
st.write("• Generate an exception report for the HR Manager")

uploaded_file = st.file_uploader(
    "Upload Payroll CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Payroll Data")
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

    # Duplicate Employee ID Check
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

    report_df = pd.DataFrame(
        exceptions,
        columns=["EmployeeID", "Employee Name", "Issue"]
    )

    st.subheader("Validation Results")
    st.dataframe(report_df)

    st.subheader("Summary")
    st.write("Total Employees:", len(df))
    st.write("Exceptions Found:", len(report_df))

    report_df.to_csv(
        "reports/exception_report.csv",
        index=False
    )

    st.success(
        "Payroll validation completed successfully. Exception report generated for HR Manager."
    )

    csv = report_df.to_csv(index=False)

    st.download_button(
        label="Download Exception Report",
        data=csv,
        file_name="exception_report.csv",
        mime="text/csv"
    )