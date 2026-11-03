"""
RECORD CHECK - my version
=========================

Name : Harry
Lane : IT
Date : 24/10/2026
"""


# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return difference, percent and status."""
    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one record report."""
    print(f"Label      : {label}")
    print(f"Value      : {value}")
    print(f"Limit      : {limit}")
    print(f"Difference : {difference}")
    print(f"Percent    : {percent:.1f}%")
    print(f"Status     : {status}")
    print()


def load_records(path):
    """Load records from a file."""
    records = []

    with open(path) as f:
        for line in f:
            line = line.strip()

            label, value, limit = line.split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


# ====================================================================== STORE

records = load_records("records.txt")


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

with open("results.txt", "w") as output_file:

    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        output_file.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"OVER LIMIT count: {over_limit_count}")


# ==========================================================================