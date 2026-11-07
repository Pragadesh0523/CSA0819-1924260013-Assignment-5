from decimal import Decimal, InvalidOperation
def process_file(filename):
    total = Decimal("0.00")
    rejected = []
    try:
        with open(filename, "r") as f:
            with open("report.txt", "w") as out:
                for line_no, line in enumerate(f, 1):
                    if not line.strip():
                        continue
                    try:
                        parts = line.strip().split(",")
                        if len(parts) != 3:
                            raise ValueError("Invalid fields")
                        reg, name, amount = parts
                        amount = Decimal(amount.strip())
                        if not amount.is_finite() or amount < 0:
                            raise ValueError("Invalid amount")
                        total += amount
                        out.write(f"{reg},{name},{amount}\n")
                    except (ValueError, InvalidOperation) as e:
                        rejected.append(
                            f"Line {line_no}: {line.strip()} - {e}"
                        )
        print("Report generated successfully")
        print("Total:", total)
        print("Rejected lines:", rejected)
    except OSError as e:
        print("File error:", e)
process_file("mess_oct.txt")