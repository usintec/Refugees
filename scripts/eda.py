import pandas as pd

file_path = "data/Questionnaire.xlsx"

df = pd.read_excel(file_path)

# print(df.head())
# print("="*60)
# print("DATASET SHAPE")
# print("="*60)

# print(df.shape)

# print("\nRows:", df.shape[0])
# print("Columns:", df.shape[1])

# print(df.columns.tolist())
# print(df.dtypes)
# df.info()
missing = df.isnull().sum()

print(missing)

missing_summary.to_csv(
    "outputs/tables/missing_value_summary.csv",
    index=False
)

print("\nMissing value summary saved to outputs/tables/missing_value_summary.csv")