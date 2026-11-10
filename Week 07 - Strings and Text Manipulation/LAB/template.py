"""
RECORD CHECK  -  my version
===========================

Name  : Harry
Lane  : IT
Date  : 10 Nov 2026

Run it:   python template.py
"""

from pathlib import Path

folder = Path(__file__).parent


# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}


def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# Messy records, deliberately varied in spacing and case.
# Saved to a file, then loaded back with open() and a for loop.
raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,used=120,total=100",
    "srv-03   ,   USED=45   ,   Total=100",
    "  SRV-04,used=92,total=100",
    "srv-05 , used = 101 , total = 100 ",
    "  Srv-06 ,used=60,total=100  ",
]

file_path = folder / "messy_lines.txt"
file_path.write_text("\n".join(raw_records) + "\n")


# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged = 0

with open(file_path) as f:
    for raw_record in f:
        if not raw_record.strip():
            continue                      # skip blank lines
        record = parse_line(raw_record)
        status = status_of(record["used"], record["total"])
        print(record, "->", status)

        total_records += 1
        if status != "OK":
            flagged += 1

print(f"\nSummary: {total_records} records, {flagged} flagged")


# ========================================================== BAD VALUE DEMO
# Checklist step: a value that will not convert - the error is printed so
# you can write it down.
print("\nBad value test:")
try:
    parse_line("srv-09,used=unknown,total=100")
except ValueError as error:
    print("ValueError:", error)