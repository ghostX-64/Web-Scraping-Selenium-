import fitz  # PyMuPDF
import os

# Specify the folder path containing the PDF files
folder_path = 'E:\CnM Infotech\projects\project_2\pdf'

# Get a list of PDF files in the folder and sort them by date modified
pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')],
                   key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

# Create a PdfWriter object
pdf_writer = fitz.open()

# Iterate through the sorted PDF files
for filename in pdf_files:
    file_path = os.path.join(folder_path, filename)
    
    # Open each PDF file using PyMuPDF
    pdf_document = fitz.open(file_path)
    
    # Add all pages to the PdfWriter object
    pdf_writer.insert_pdf(pdf_document)

# Specify the output file path for the combined PDF
output_path = 'combined.pdf'

# Save the combined PDF to the output file
pdf_writer.save(output_path)
pdf_writer.close()
