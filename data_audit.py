"""
Data audit for the XYZ Corporation HR dataset.
Checks run before building the Tableau dashboard.

Usage:  python data_audit.py "Human Resources.csv"
"""
import sys
import pandas as pd

path = sys.argv[1] if len(sys.argv) > 1 else "Human Resources.csv"
df = pd.read_csv(path, encoding="utf-8-sig")
print(f"Rows: {len(df):,}   Columns: {df.shape[1]}")

# 1. Unique IDs
print(f"Unique employee IDs: {df['Id'].nunique():,}")

# 2. Missing values in key fields
key = ["Id", "Department", "Jobtitle", "Gender", "Race", "Location",
       "Location State", "Hire Date", "Employement Status", "Age", "Tenure"]
print("\nMissing values in key fields:")
print(df[key].isna().sum())

# 3. Parse text dates
fmt = "%d-%m-%Y %H:%M:%S"
df["hire"] = pd.to_datetime(df["Hire Date"], format=fmt, errors="coerce")
df["term"] = pd.to_datetime(df["Termdate"], format=fmt, errors="coerce")
print(f"\nHire dates: {df['hire'].min():%Y-%m-%d} to {df['hire'].max():%Y-%m-%d}")

# 4. Do the two status fields agree?
print("\nEmployment Status vs Termdate (group):")
print(pd.crosstab(df["Employement Status"], df["Termdate (group)"]))
scheduled = df[(df["Employement Status"] == "Active") & df["term"].notna()]
print(f"Active employees with a termination date: {len(scheduled):,}")

# 5. Columns that carry no information
constant = [c for c in df.columns if df[c].nunique(dropna=False) <= 1]
mostly_empty = [c for c in df.columns if df[c].isna().mean() > 0.9]
print(f"\nConstant columns: {constant}")
print(f"Mostly empty columns (>90% null): {mostly_empty}")

# 6. Headline numbers to check the dashboard against
n = len(df)
active = (df["Employement Status"] == "Active").sum()
remote = (df["Location"] == "Remote").sum()
print("\nExpected dashboard values:")
print(f"  Total employees : {n:,}")
print(f"  % Active        : {active / n:.1%}")
print(f"  % Remote        : {remote / n:.1%}")
print(f"  Avg / median age: {df['Age'].mean():.1f} / {df['Age'].median():.0f}")
print(f"  Avg tenure      : {df['Tenure'].mean():.1f} years")
print(f"  Departments     : {df['Department'].nunique()}")
