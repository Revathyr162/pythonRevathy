import PyPDF2
import os

def merge_pdfs(input_paths, output_path):
    merger = PyPDF2.PdfFileMerger()
    
    for path in input_paths:
        merger.append(path)
    
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

# Example usage
input_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # List of PDF files to merge
output_file = 'merged_file.pdf'  # Output file name

merge_pdfs(input_files, output_file)
print("PDFs merged successfully!")
