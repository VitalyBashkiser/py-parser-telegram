import csv
import os
from typing import List


def save_to_file(data: List[dict], filename: str):
    file_exists = os.path.isfile(filename)

    existing_links = set()
    if file_exists:
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                existing_links = set(row["resume"] for row in reader)
        except Exception as e:
            print(f"Failed to read existing file for uniqueness check: {e}")

    new_data = [item for item in data if item["resume"] not in existing_links]

    if not new_data:
        print("No new unique candidates to add.")
        return

    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "title",
                    "resume",
                    "years_of_experience",
                    "skills",
                    "location",
                    "salary_expectation",
                ],
            )

            if not file_exists:
                writer.writeheader()

            writer.writerows(new_data)
        print(f"Data successfully added to the file: {filename}")
    except Exception as e:
        print(f"Failed to add data to file: {e}")
