import pandas as pd
from datetime import date
import json

records = [
    {
        "Date": date(2025, 4, 26),
        "Mileage": 44456,
        "Services": [
            "40,000 Mile Maintenance Service",
            "Perform Transfer Case Fluid Exchange Service",
        ],
        "Price": 630.38
    },
    {
        "Date": date(2024, 10, 19),
        "Mileage": 39622,
        "Services": [
            "40,000 Mile Maintenance Service",
        ],
        "Price": 767.11
    },
    {
        "Date": date(2024, 7, 1),
        "Mileage": 23946,
        "Services": [
            "25,000 Mile Maintenance Service",
        ],
        "Price": 0
    },
    {
        "Date": date(2023, 1, 26),
        "Mileage": 19194,
        "Services": [
            "20,000 Mile Maintenance Service",
            "4 Wheel Alignment",
        ],
        "Price": 109.95
    },
    {
        "Date": date(2022, 9, 3),
        "Mileage": 14507,
        "Services": [
            "15,000 Mile Maintenance Service",
        ],
        "Price": 0
    },
    {
        "Date": date(2022, 5, 16),
        "Mileage": 11186,
        "Services": [
            "TPMS Light Malfunction",
        ],
        "Price": 0
    },
    {
        "Date": date(2022, 5, 8),
        "Mileage": 10992,
        "Services": [
            "10,000 Mile Complimentary Maintenance Service",
            "Re-Program Car Key",
            "Purchase for Physical Car Key",
        ],
        "Price": 523.36
    },
    {
        "Date": date(2021, 12, 7),
        "Mileage": 5801,
        "Services": [
            "5,000 Mile Complimentary Maintenance Service",
        ],
        "Price": 0
    },
]

# convert list of services to JSON string for CSV
for r in records:
    r["Services"] = json.dumps(r["Services"])
    r["Date"] = r["Date"].isoformat() # formats as "YYY-MM-DD"

df = pd.DataFrame(records)
df.to_csv('maintenance_data.csv', index=False)
print("CSV file saved as 'maintenance_data.csv'")



