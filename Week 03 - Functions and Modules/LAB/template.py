"""
RECORD CHECK  -  my version
===========================

Name  : Harry 
Lane  : IT     
Date  : 20/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Return status string based on percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the full bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status}")
    print("=" * 34)


# ==================================================================== LOOP
# Ask for records until user types "quit"
over_limit_count = 0

while True:
    label = input("Hostname (or 'quit' to stop): ")
    if label.lower() == "quit":
        break

    value = float(input("GB used: "))
    limit = float(input("GB total: "))

    # Calculate
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # Print report
    print_report(label, value, limit, difference, percent, status)

# After loop ends
print(f"\nRecords over limit: {over_limit_count}")
