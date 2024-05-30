from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageDraw, ImageFont
import emoji
import io

# Function to render text (including emojis) to an image
def render_text_to_image(text, font_path, font_size=20):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a dummy image to get the bounding box
    dummy_image = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(dummy_image)
    bbox = draw.multiline_textbbox((0, 0), text, font=font)
    width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Create a new image with a transparent background
    image = Image.new("RGBA", (max(width, 1), max(height, 1)), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Render the text including emojis
    draw.multiline_text((-bbox[0], -bbox[1]), text, font=font, fill=(0, 0, 0, 255))
    
    return image



# Function to convert a text file to a PDF
def text_to_pdf(text_file, pdf_file, font_path):
    # Create a canvas object
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Read the text file with the correct encoding
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Define the initial y position
    y = height - 40
    line_height = 30  # Adjusted to match the larger font size

    # Add each line to the PDF
    for line in lines:
        if y < 40:  # Check if the y position is close to the bottom of the page
            pdf.showPage()  # Add a new page
            y = height - 40  # Reset y position

        # Render the line to an image
        image = render_text_to_image(line.strip(), font_path)
        # Save the image to a byte stream
        byte_stream = io.BytesIO()
        image.save(byte_stream, format='PNG')
        byte_stream.seek(0)
        img_reader = ImageReader(byte_stream)

        # Draw the image on the PDF
        pdf.drawImage(img_reader, 40, y - image.height, mask='auto')
        y -= (image.height + 2)

    # Save the PDF
    pdf.save()

# Convert the text file to PDF
text_file = 'example.txt'  # Replace with your text file
pdf_file = 'output.pdf'    # Replace with your desired PDF file name
font_path = 'Symbola.ttf'  # Path to the emoji-supporting font file
text_to_pdf(text_file, pdf_file, font_path)
