# week6_lab.py
# Author: Sami Ali

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Riley", "category": "Travel", "amount": 89, "status": "Pending"},
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200,
        "status": "Pending",
    },
]

for rec in records:
    if rec["status"] == "Pending":
        print(f"{rec['name']}: ${rec['amount']:,.2f}")
for rec in records:
    if rec["status"] == "Pending":
        print(f"{rec['name']}: ${rec['amount']:,.2f}")
        LIMIT = 1000
HIGH = 2000

total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]

        if rec["amount"] > LIMIT:
            flagged.append(rec)

        if rec["amount"] > HIGH:
            high_value.append(rec)

print(f"Pending total: ${total:,.2f}")
print(f"Needs review: {len(flagged)}")
print(f"High-value: {len(high_value)}")
# week6_lab.py
# Author: Sami Ali

import os

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Riley", "category": "Travel", "amount": 89, "status": "Pending"},
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200,
        "status": "Pending",
    },
]

LIMIT = 1000
HIGH = 2000

total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]

        if rec["amount"] > LIMIT:
            flagged.append(rec)

        if rec["amount"] > HIGH:
            high_value.append(rec)

os.makedirs("data", exist_ok=True)

lines = [
    f"Pending total:   ${total:,.2f}",
    f"Needs review:    {len(flagged)}",
    f"High-value:      {len(high_value)}",
]

for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for rec in flagged:
    print(f"  ID {rec['id']}: {rec['name']} - ${rec['amount']:,.2f}")
    # week6_lab.py
# Author: Sami Ali

import os

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Riley", "category": "Travel", "amount": 89, "status": "Pending"},
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200,
        "status": "Pending",
    },
]

LIMIT = 1000
HIGH = 2000

total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]

        if rec["amount"] > LIMIT:
            flagged.append(rec)

        if rec["amount"] > HIGH:
            high_value.append(rec)

os.makedirs("data", exist_ok=True)

lines = [
    f"Pending total:   ${total:,.2f}",
    f"Needs review:    {len(flagged)}",
    f"High-value:      {len(high_value)}",
]

for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for rec in flagged:
    print(f"  ID {rec['id']}: {rec['name']} - ${rec['amount']:,.2f}")
