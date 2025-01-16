
# pip install pandas pdfplumber # Install required packages


import pandas as pd
import pdfplumber
import os

def merge_csv_files(csv_file1, csv_file2, output_file, merge_columns):
    """
    Merges two CSV files based on common columns and saves the output.
    """
    try:
        # Load CSV files into DataFrames
        df1 = pd.read_csv(csv_file1)
        df2 = pd.read_csv(csv_file2)

        # Merge on the specified columns
        merged_df = pd.merge(df1, df2, on=merge_columns, how="inner")

        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv(output_file, index=False)
        print(f"Merged CSV saved to {output_file}")
    except Exception as e:
        print(f"Error during CSV merge: {e}")

def parse_pdfs(pdf_folder, output_csv):
    """
    Parses all PDFs in a folder, extracts text, and saves the output to a CSV.
    """
    extracted_data = []

    try:
        # Iterate through all PDF files in the folder
        for pdf_file in os.listdir(pdf_folder):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder, pdf_file)
                with pdfplumber.open(pdf_path) as pdf:
                    for page_number, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        extracted_data.append({
                            "File": pdf_file,
                            "Page": page_number + 1,
                            "Content": text.strip() if text else ""
                        })

        # Convert extracted data to a DataFrame and save to CSV
        df = pd.DataFrame(extracted_data)
        df.to_csv(output_csv, index=False)
        print(f"PDF parsed data saved to {output_csv}")
    except Exception as e:
        print(f"Error during PDF parsing: {e}")

# Main Function
if __name__ == "__main__":
    # Input parameters
    csv_file1 = "names_addresses.csv"  # First CSV (names and addresses)
    csv_file2 = "donations_details.csv"  # Second CSV (donation details)
    merged_csv_output = "merged_output.csv"
    merge_columns = ["Name", "Address"]  # Columns to merge on

    pdf_folder_path = "pdfs"  # Folder containing PDF files
    parsed_pdfs_output = "parsed_pdfs.csv"

    # Merge CSV files
    merge_csv_files(csv_file1, csv_file2, merged_csv_output, merge_columns)

    # Parse PDFs and save to CSV
    parse_pdfs(pdf_folder_path, parsed_pdfs_output)
