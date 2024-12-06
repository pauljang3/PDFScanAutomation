"""
PDF Combining Automation Script

Description: 
This script automates the process of:
1. Retrieving all PDF files from a specified directory (H: drive in this case).
2. Combining the retrieved PDF files into a single PDF file.
3. Saving the combined PDF in a target directory (Z: drive in this case).
4. Deleting the original individual PDF files from the source directory (H: drive).

Usage:
Run this script with a document number as an argument to specify the filename of the combined PDF.
Example: python script_name.py 12345

Arguments:
- document_number: A unique identifier for the output file (e.g., "12345").

Author: 
Paul Jang
"""
import os
import shutil
import argparse
from PyPDF2 import PdfMerger

def get_all_pdfs(directory):
    # Retrieve all PDF files in the specified directory.
    pdf_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    return pdf_files

def combine_pdfs(pdf_files, output_dir, document_number):
    # Combine multiple PDF files into a single PDF. 
    merger = PdfMerger()
    
    # Add each PDF file to the merger
    for pdf in pdf_files:
        merger.append(pdf)

    # Save the combined PDF with the document number as filename
    output_file = os.path.join(output_dir, f"{document_number}.pdf")
    merger.write(output_file)
    merger.close()
    
    return output_file

def move_and_delete(h_drive_path):
    # Move the combined PDF to the Z drive and delete all individual PDFs from the H drive.
    pdf_files = get_all_pdfs(h_drive_path)
    
    # Delete each individual PDF in H Drive
    for file in pdf_files:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except FileNotFoundError:
            print(f"File not found for deletion: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

def automate_pdf_processing(h_drive_path, z_drive_path, document_number):
    # Step 1: Get all PDF files in the H: drive folder
    pdf_files = get_all_pdfs(h_drive_path)
    
    # Step 2: Combine PDFs into a single file in Z drive
    if pdf_files:  # Proceed if there are PDFs to combine
        combined_pdf = combine_pdfs(pdf_files, z_drive_path, document_number)
        
        # Step 3: Delete original files from H: drive
        move_and_delete(h_drive_path)
    else:
        print("No PDF files found to combine.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Combine PDFs and move to archive with a specified document number.")
    parser.add_argument("document_number", type=str, help="The document number for the combined PDF filename.")
    
    args = parser.parse_args()
    
    # Paths using UNC for network drives
    h_drive_path = r"\\servername\path"
    z_drive_path = r"\\servername\path"
    
    # Run the automation with the document number provided as an argument
    automate_pdf_processing(h_drive_path, z_drive_path, args.document_number)
