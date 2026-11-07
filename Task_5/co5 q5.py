import csv
from datetime import datetime, timedelta

def read_data():
    with open("attendance.csv") as f:
        return list(csv.DictReader(f))

def statistics(data):
    total = len(data)
    present = sum(r["status"] == "Present" for r in data)
    return present, total, present / total * 100

def report(data):
    p, t, percentage = statistics(data)
    print("Total:", t)
    print("Present:", p)
    print("Attendance:", percentage, "%")

def consecutive_report(data):
    students = {}
    for r in data:
        students.setdefault(r["student"], []).append(r)

    for name, records in students.items():
        records.sort(key=lambda x: x["date"])
        for i in range(len(records) - 2):
            dates = [datetime.strptime(
                records[j]["date"], "%Y-%m-%d").date()
                for j in range(i, i + 3)]

            if (all(records[j]["status"] == "Absent"
                    for j in range(i, i + 3))
                    and dates[1] - dates[0] == timedelta(days=1)
                    and dates[2] - dates[1] == timedelta(days=1)):
                print(name, "absent for 3 consecutive days")
                break

data = read_data()
report(data)
consecutive_report(data)    