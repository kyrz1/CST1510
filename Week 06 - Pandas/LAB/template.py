"""
RECORD CHECK  -  my version
===========================

Name  : Harry
Lane  : IT
Date  : 10 Nov 2026

Run it:   python template.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Work in the same folder as this script, so file paths always match
folder = Path(__file__).parent

# ==================================================================== LOAD
csv_path = folder / "servers_data.csv"

# Create the data file (header + 6 rows) so you don't have to make it by hand
csv_path.write_text(
    "hostname,used,total\n"
    "srv-01,87,100\n"
    "srv-02,120,100\n"
    "srv-03,45,100\n"
    "srv-04,92,100\n"
    "srv-05,101,100\n"
    "srv-06,60,100\n"
)

df = pd.read_csv(csv_path)


# ================================================================= PROCESS
df["percent"] = (df["used"] / df["total"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
print("All servers:")
print(df)

print("\nNeeds attention (not OK):")
print(df[df["status"] != "OK"])

counts = df.groupby("status").size()
print("\nCount per status:")
print(counts)

df.to_csv(folder / "servers_report.csv", index=False)

counts.plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig(folder / "status_counts.png")
plt.show()