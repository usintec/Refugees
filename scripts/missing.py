import pandas as pd

file_path = "data/Questionnaire.xlsx"

df = pd.read_excel(file_path)

# Calculate missing values
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    "Column": df.columns,
    "Missing Count": missing_count.values,
    "Missing (%)": missing_percent.values
})

# Add a status column
missing_summary["Status"] = missing_summary["Missing (%)"].apply(
    lambda x: "✅ Complete" if x == 0 else
              "🟢 Low" if x < 5 else
              "🟡 Moderate" if x < 20 else
              "🔴 High"
)

# Sort by highest missing percentage
missing_summary = missing_summary.sort_values(
    by="Missing (%)",
    ascending=False
).reset_index(drop=True)

# print("\n" + "="*90)
# print("MISSING VALUE SUMMARY")
# print("="*90)
# print(missing_summary.to_string(index=False))
# print("="*90)
# print(f"Total Rows    : {len(df)}")
# print(f"Total Columns : {len(df.columns)}")
# print(f"Columns with Missing Values : {(missing_count > 0).sum()}")
# print(f"Complete Columns            : {(missing_count == 0).sum()}")
# print("="*90)

missing_summary.to_csv(
    "outputs/tables/missing_value_summary.csv",
    index=False
)

print("\nMissing value summary saved to outputs/tables/missing_value_summary.csv")