from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to convert text file to PDF
def text_to_pdf(text_file, pdf_file):
    # Create a canvas object
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    pdf.setFont("Helvetica", 12)

    # Read the text file with the correct encoding
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Define the initial y position
    y = height - 40
    line_height = 14

    # Add each line to the PDF
    for line in lines:
        if y < 40:  # Check if the y position is close to the bottom of the page
            pdf.showPage()  # Add a new page
            pdf.setFont("Helvetica", 12)
            y = height - 40  # Reset y position

        pdf.drawString(40, y, line.strip())
        y -= line_height

    # Save the PDF
    pdf.save()

# Convert the text file to PDF
text_file = 'example.txt'  # Replace with your text file
pdf_file = 'output.pdf'    # Replace with your desired PDF file name
text_to_pdf(text_file, pdf_file)
