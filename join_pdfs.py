import os
from pypdf import PdfWriter

def merge_specific_pdfs(pdf_list, output_filename):
    writer = PdfWriter()
    
    print(f"Merging the following files: {pdf_list}")
    
    for filename in pdf_list:

        if os.path.exists(filename):
            writer.append(filename)
        else:
            print(f"Warning: Could not find '{filename}'. Skipping.")

    with open(output_filename, "wb") as output_file:
        writer.write(output_file)
        
    print(f"Successfully created: {output_filename}")

files_to_join = ["1_EDA.pdf", "3_Model_Classification.pdf"]

output_filename = "Final Project - Team 4 - Code.pdf"

merge_specific_pdfs(files_to_join, output_filename)