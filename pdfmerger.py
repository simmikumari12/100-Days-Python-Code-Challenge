from pypdf import PdfWriter

def main():
    merger = PdfWriter()


    for pdf in ["random_pdfs/cover1.pdf", "random_pdfs/CLETTER.pdf", "random_pdfs/coverLetter_app_support.pdf"]:
        merger.append(pdf)

    merger.write("random_pdfs/merged-pdf.pdf")
    merger.close()

if __name__ == "__main__":
    main()