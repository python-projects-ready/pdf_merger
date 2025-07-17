import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    # Create a PdfMerger object
    merger = PdfMerger()
    
    # Loop through the input PDFs
    for pdf in pdf_list:
        if os.path.exists(pdf):
            # Add each PDF to the merger
            merger.append(pdf)
            print(f"Added: {pdf}")
        else:
            print(f"File not found: {pdf}")
    
    # Write the merged PDF to the output file
    try:
        merger.write(output_path)
        print(f"Merged PDF saved as: {output_path}")
    except Exception as e:
        print(f"Error writing merged PDF: {e}")
    
    # Close the merger
    merger.close()

if __name__ == "__main__":
    # Specify the input PDF files and the output PDF file
    input_files = [
        "D:\\github files\\pdf_merger\\NumPy Universal Functions.pdf", 
        "D:\\github files\\pdf_merger\\Stop_Words_Stemming_Lemmatization_NLP.pdf"
    ]
    output_file = "D:\\github files\\pdf_merger\\output.pdf"  # Output file path

    # Call the merge_pdfs function
    merge_pdfs(input_files, output_file)
