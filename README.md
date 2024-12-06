# PDF Scan Automation
## Context
At my current role, I was tasked with the secure document archival and destruction process. This involved scanning documents before sending them to a shredding company.
- Scanned documents were sent to my workspace in the H: drive via a printer.
- I noticed that this process was time-consuming due to frequent printer jams.
- To minimize the impact of jams, I split documents into smaller stacks, reducing the number of pages needing rescanning if a jam occurred.
- However, the task of combining the multiple PDF files into one was also time-consuming. To address this, I developed a [Python script](https://github.com/pauljang3/PDFScanAutomation/blob/main/scanscript.py) that automated the combining process.

The script reduced this process of combining PDF files, moving to the archived file server, and clearing the H: drive from 1 minute to 9 seconds, resulting in a 85% improvement in efficiency.

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
