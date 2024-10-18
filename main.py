from PyPDF2 import PdfReader, PdfWriter, PageObject

def crop_pdf(input_pdf, output_pdf, left_margin, right_margin, top_margin, bottom_margin):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        media_box = page.mediabox

        # Adjust the margins as needed
        page.mediabox.lower_left = (
            media_box.lower_left[0] + left_margin,
            media_box.lower_left[1] + bottom_margin
        )
        page.mediabox.upper_right = (
            media_box.upper_right[0] - right_margin,
            media_box.upper_right[1] - top_margin
        )

        writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    # Usage
    # 1 inch = 72 points, so 1 inch = 72, 0.5 inch = 36 points
    crop_pdf('input.pdf', 'output_cropped.pdf', 
            left_margin=36, right_margin=36, top_margin=72, bottom_margin=72)
