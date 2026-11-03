"""
RECORD CHECK  -  my version
===========================

Name  : Harry
Lane  : IT      
Date  : 26/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""
RECORD CHECK - my version
=========================

Name  : Harry
Lane  : IT
Date  : 26/10/2026
"""


class Record:
    """Stores one record."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Create a record."""
        self.label = label
        self.value = value
        self.limit = limit

        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Return the record status."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Load records from a file."""
    records = []

    with open(path) as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            records.append(
                Record(label, float(value), float(limit))
            )

    return records


records = load_records("records_sample.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"Value : {record.value}")
    print(f"Limit : {record.limit}")
    print(f"Status: {record.status()}")

    print("=" * 34)

print()
print(f"{Record.over_limit_count} of {len(records)} were over limit")