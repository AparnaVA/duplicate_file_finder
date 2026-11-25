# Duplicate File Finder

## Project Description
Duplicate File Finder is a simple Python application that scans a folder and its subfolders to identify duplicate files.

It identifies files with identical content even if they have different names. The program uses SHA-256 hashing to compare file contents, groups duplicate files, calculates potential storage savings, and allows users to export the report as a CSV file.

The program also provides an option to select duplicate files for removal after reviewing them. Files are never deleted automatically.

## Features
- Accepts a folder path from the user.
- Scans all files, including files inside subfolders.
- Identifies duplicate files based on their content.
- Finds duplicates even when they have different names.
- Groups duplicate files together.
- Displays file paths and file sizes.
- Calculates the number of duplicate copies.
- Calculates potential storage space savings.
- Exports duplicate reports to CSV.
- Allows users to select duplicate files for removal.
- Requires confirmation before deleting files.

## Technologies Used
- Python
- OS module
- Hashlib module
- CSV module

## How It Works
1. The user enters the folder path to scan.
2. The program scans the folder and its subfolders using `os.walk()`.
3. It checks the file sizes to identify files that could potentially be duplicates.
4. It calculates SHA-256 hash values for files of the same size.
5. Files with matching hash values are grouped as duplicates.
6. The program displays the duplicate file paths, file size, duplicate copies, and potential space savings.
7. The user can export the report to a CSV file.
8. The user can select duplicate files for removal after reviewing the list.

## How to Run

### 1. Clone the Repository
```bash
git clone <repository-url>
```

### 2. Navigate to the Project Folder
```bash
cd duplicate-file-finder
```

### 3. Run the Python Program
```bash
python duplicate_file_finder.py
```

### 4. Enter the Folder Path
Provide the folder path you want to scan when prompted.

## Example Output
```text
Duplicate Group 1:
Documents/report.pdf
Backup/report_copy.pdf
OldFiles/document_01.pdf

File Size: 2.50 MB
Duplicate Copies: 2
Potential Space Savings: 5.00 MB

Total Potential Space Savings: 5.00 MB
```

## CSV Report
The program can export the duplicate file report to a CSV file named `duplicate_report.csv`.

The report contains:
- Duplicate group number
- File path
- File size in bytes
- Number of duplicate copies
- Potential space savings in bytes

