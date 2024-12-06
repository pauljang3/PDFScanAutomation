# PDF Scan Automation

## Overview
This Python script automates the process of managing scanned PDF files. It:
1. Combines all PDF files in a specified directory into a single PDF file.
![h](https://github.com/user-attachments/assets/19392678-073c-4aef-8a82-4cf10a50e285)
2. Saves the combined PDF file to a designated network share (another drive).
![z](https://github.com/user-attachments/assets/73cc9145-1c4b-4d07-bf04-5b5db93bd799)
3. Deletes the original PDF files from the source directory after processing.
![empty](https://github.com/user-attachments/assets/e0138b91-365e-4d7d-ad63-fe5e7b7aebe3)

## Features
- Automatically scans a directory for all PDF files.
- Combines PDFs into a single document with a user-specified filename.
- Moves the final combined file to a secure network archive.
- Cleans up the source directory by deleting the individual PDF files.

## Usage
Run the script from the command line, passing the document number as an argument. 
### Example
```bash
python scanscript.py 8993
```
![cmd](https://github.com/user-attachments/assets/3f0cf9b1-a2b5-4791-b46d-aebe675ccd1a)




This will:
- Combine all PDFs in the source directory.
- Save the resulting file as `8993.pdf` in the network archive.
- Delete the original PDF files from the source directory.

## Prerequisites
- **Python Version**: Python 3.7 or higher
- **Dependencies**: Install required Python packages using pip:
```bash
  pip install PyPDF2
```
