"""
RECORD CHECK  -  my version
===========================

Name  : Harry
Lane  : IT
Date  : 10 Nov 2026

Run it:   python template.py
"""

# ==================================================================== INPUT
label = input("Hostname: ")
used = float(input("Used: "))
total = float(input("Total: "))


# ================================================================== PROCESS
difference = used - total
percent = (used / total) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Used       {used:>10.2f}")
print(f"  Total      {total:>10.2f}")
print(f"  Difference {difference:>+10.2f}")
print(f"  Percent    {percent:>9.2f}%")
print(f"  Status     {status:>10}")
print("=" * 34)