from pypdf import PdfWriter

def main():
    merger = PdfWriter()

    for pdf in ["random_pdfs/3.pdf", "random_pdfs/4.pdf"]:
        merger.append(pdf)
    merged_pdf_name = input("Name Your Pdf: ")
    merger.write(f"random_pdfs/{merged_pdf_name}.pdf")
    merger.close()

if __name__ == "__main__":
    main()