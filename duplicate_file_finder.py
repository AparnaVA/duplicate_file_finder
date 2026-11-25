
import os
import hashlib
import csv

# Function to calculate the hash value of a file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except (OSError, PermissionError):
        return None


# Function to find duplicate files
def find_duplicates(folder_path):
    file_groups = {}

    for root, folders, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                file_size = os.path.getsize(file_path)

                # Skip empty files
                if file_size == 0:
                    continue

                # Use file size as the first check
                key = file_size

                if key not in file_groups:
                    file_groups[key] = []

                file_groups[key].append(file_path)

            except OSError:
                print("Unable to access:", file_path)

    duplicates = []

    # Check files with the same size
    for file_size, file_paths in file_groups.items():

        if len(file_paths) < 2:
            continue

        hash_groups = {}

        for file_path in file_paths:
            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash not in hash_groups:
                hash_groups[file_hash] = []

            hash_groups[file_hash].append(file_path)

        # Store groups having identical content
        for file_hash, paths in hash_groups.items():
            if len(paths) > 1:
                duplicates.append({
                    "files": paths,
                    "size": file_size
                })

    return duplicates


# Function to display duplicate files
def display_duplicates(duplicates):
    total_wasted_space = 0

    if not duplicates:
        print("\nNo duplicate files found.")
        return

    for index, group in enumerate(duplicates, start=1):
        files = group["files"]
        file_size = group["size"]

        duplicate_count = len(files) - 1
        wasted_space = file_size * duplicate_count

        total_wasted_space += wasted_space

        print(f"\nDuplicate Group {index}:")
        for file_path in files:
            print(file_path)

        print("File Size:", format_size(file_size))
        print("Duplicate Copies:", duplicate_count)
        print("Potential Space Savings:", format_size(wasted_space))

    print("\nTotal Potential Space Savings:", format_size(total_wasted_space))


# Function to convert bytes into readable format
def format_size(size):
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    elif size >= 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size} bytes"


# Function to export duplicate report to CSV
def export_csv(duplicates):
    file_name = "duplicate_report.csv"

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow([
            "Group",
            "File Path",
            "File Size (Bytes)",
            "Duplicate Copies",
            "Potential Space Savings (Bytes)"
        ])

        for index, group in enumerate(duplicates, start=1):
            files = group["files"]
            file_size = group["size"]

            duplicate_count = len(files) - 1
            wasted_space = file_size * duplicate_count

            for file_path in files:
                writer.writerow([
                    index,
                    file_path,
                    file_size,
                    duplicate_count,
                    wasted_space
                ])

    print(f"\nReport exported successfully: {file_name}")


# Main program
folder_path = input("Enter folder path to scan: ").strip()

if os.path.isdir(folder_path):

    print("\nScanning files... Please wait.")

    duplicates = find_duplicates(folder_path)

    display_duplicates(duplicates)

    if duplicates:
        choice = input("\nDo you want to export the report to CSV? (yes/no): ").lower()

        if choice == "yes":
            export_csv(duplicates)

else:
    print("Invalid folder path.")
