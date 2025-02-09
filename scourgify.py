import sys
import csv

# Checks Input Validity
sys_len = len(sys.argv)
if sys_len <= 2:
    sys.exit("Too few command-line arguments")
if sys_len > 3:
    sys.exit("Too many command-line arguments")
unordered_csv = sys.argv[1]
ordered_csv = sys.argv[2]
output_data = []

try:
    with open(unordered_csv, "r") as f:
        csv_data = csv.DictReader(f)
        for row in csv_data:
            last, first = row['name'].split(", ")
            output_data.append({"first": first, "last": last, "house": row['house']})
except FileNotFoundError:
    sys.exit(f"Could not read {unordered_csv}")

with open(ordered_csv, "w") as f2:
    writer = csv.DictWriter(f2, fieldnames= ["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in output_data:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
