from PIL import Image

class ImageToPDFConverter:
    def __init__(self, image_path, output_pdf_path):
        self.image_path = image_path
        self.output_pdf_path = output_pdf_path

    def convert_image_to_pdf(self):
        try:
            # Open the image file
            image = Image.open(self.image_path)

            # Convert image to RGB mode (necessary for some image formats to avoid errors)
            image = image.convert("RGB")

            # Save image as PDF
            image.save(self.output_pdf_path, "PDF", resolution=100.0)

            print("Image converted to PDF successfully!")
        except Exception as e:
            raise ImageToPDFConversionError(f"Error converting image to PDF: {str(e)}")

class ImageToPDFConversionError(Exception):
    pass

# Example usage:
if __name__ == "__main__":
    try:
        image_path = "input_image.jpg"  # Path to your input image
        output_pdf_path = "output_pdf.pdf"  # Path to save the PDF file
        
        converter = ImageToPDFConverter(image_path, output_pdf_path)
        converter.convert_image_to_pdf()
    except ImageToPDFConversionError as e:
        print(f"Image to PDF conversion failed: {e}")