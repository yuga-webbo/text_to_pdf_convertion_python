from fpdf import FPDF

# Function to convert text file to PDF
def text_to_pdf(text_file, pdf_file):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Read the text file with explicit encoding
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Add each line to the PDF
    for line in lines:
        # Encode the line explicitly to avoid encoding issues
        encoded_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, encoded_line)

    # Save the PDF
    pdf.output(pdf_file)

# Convert the text file to PDF
text_file = 'example.txt'  # Replace with your text file
pdf_file = 'output.pdf'    # Replace with your desired PDF file name
text_to_pdf(text_file, pdf_file)
