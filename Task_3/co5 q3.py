import os
import tempfile

class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""
    pass


def parse_line(line):
    parts = line.strip().split(",")

    # TODO 1: Validate the record
    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    if parts[2] not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{parts[2]}'")

    return tuple(parts)


def summarise(path):
    present, absent, errors = 0, 0, []

    # TODO 2: Read and process the file
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                try:
                    sid, date, status = parse_line(line)

                except InvalidRecord as e:
                    errors.append((line_no, str(e)))

                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1

    except FileNotFoundError as e:
        raise RuntimeError("Attendance file not found") from e

    except PermissionError as e:
        raise RuntimeError("Permission denied") from e

    except UnicodeDecodeError as e:
        raise RuntimeError("Invalid file encoding") from e

    except OSError as e:
        raise RuntimeError("File processing error") from e

    else:
        print("File processed successfully.")

    finally:
        print("Processing completed.")

    return present, absent, errors


# Test data
data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

# Create temporary file
with tempfile.NamedTemporaryFile(
    mode="w", suffix=".csv", delete=False,
    encoding="utf-8"
) as tmp:
    tmp.write(data)
    filename = tmp.name

# Execute program
try:
    print(summarise(filename))

except RuntimeError as e:
    print(e)

finally:
    os.remove(filename)