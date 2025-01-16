# CSV and PDF Processing Tool

This script provides a unified solution for merging CSV files and extracting text from PDF files. It performs the following tasks:

1. **CSV Merging**: Merges two CSV files based on specified columns (e.g., `Name` and `Address`).
2. **PDF Parsing**: Extracts text from all pages of PDF files in a specified folder and saves the content to a CSV.

## Features
- Merges two CSV files on common columns using Pandas.
- Extracts text from PDF files using `pdfplumber`.
- Saves the outputs to separate CSV files for easy analysis.

## Prerequisites

1. Python 3.6+
2. Install the required libraries:
   ```bash
   pip install pandas pdfplumber
   ```

## File Structure

```
project_folder/
|-- script_name.py        # The main script file
|-- names_addresses.csv   # First CSV file with names and addresses
|-- donations_details.csv # Second CSV file with donation details
|-- pdfs/                 # Folder containing PDF files
|-- output/
    |-- merged_output.csv   # Output file for merged CSV
    |-- parsed_pdfs.csv     # Output file for parsed PDF data
```

## Usage

### 1. Merging CSV Files

To merge two CSV files:
- Ensure the first CSV (`names_addresses.csv`) contains columns for `Name` and `Address`.
- Ensure the second CSV (`donations_details.csv`) contains the same `Name` and `Address` columns along with additional details.

The script will merge these files on the `Name` and `Address` columns and save the output as `merged_output.csv` in the `output` folder.

### 2. Parsing PDF Files

To parse PDFs:
- Place all PDF files in a folder (e.g., `pdfs/`).
- The script will extract text from each page of every PDF and save the results in `parsed_pdfs.csv` in the `output` folder.

### Running the Script

1. Update the file paths and folder names in the script if necessary.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Outputs will be saved in the specified locations.

## Configuration

Modify the following variables in the script to fit your data:
- `csv_file1`: Path to the first CSV file.
- `csv_file2`: Path to the second CSV file.
- `merged_csv_output`: Path to save the merged CSV output.
- `merge_columns`: List of columns to merge on (e.g., `['Name', 'Address']`).
- `pdf_folder_path`: Path to the folder containing PDFs.
- `parsed_pdfs_output`: Path to save the parsed PDF output.

## Example Output

### Merged CSV
| Name           | Address         | Donation Amount | Date       |
|----------------|-----------------|-----------------|------------|
| John Doe       | 123 Elm St      | $100            | 2025-01-01 |
| Jane Smith     | 456 Oak Ave     | $200            | 2025-01-02 |

### Parsed PDFs
| File          | Page | Content                     |
|---------------|------|-----------------------------|
| file1.pdf     | 1    | Sample text from page 1     |
| file1.pdf     | 2    | Sample text from page 2     |

## Notes
- Ensure that the column names in both CSV files match exactly.
- The script assumes all PDF files in the specified folder are valid and readable.
- Handle large PDF files or CSV datasets with appropriate hardware resources.

## License
This tool is open-source and free to use under the MIT License.

## Contact
For any issues or feature requests, please open an issue on the GitHub repository or contact the developer at [your-email@example.com].
