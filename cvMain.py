# --------------------------------------------------------------
# Creation:    07/05/2023
# Author:      Hugo REIF FAUDEMER
# --------------------------------------------------------------
import sys
from cvBuilder import generate_html, CVData  

# =================== VARIABLES ===================
"""
G_CONFIG_PDF: dict

A dictionary configuring PDF generation settings.

Attributes:
    pdf_options (dict): A nested dictionary containing specific PDF generation options.
        Attributes:
            page-size (str): Specifies the page size within the PDF options, mirroring the outer page_size setting.
            margin-top (str): The top margin of the PDF pages, set to '0mm'.
            margin-right (str): The right margin of the PDF pages, set to '0mm'.
            margin-bottom (str): The bottom margin of the PDF pages, set to '0mm'.
            margin-left (str): The left margin of the PDF pages, set to '0mm'.
            encoding (str): Specifies the character encoding for the PDF, consistent with the outer encoding setting.
            enable-local-file-access (str): Intended to specify whether local file access is enabled for PDF generation, but currently has an empty string which should ideally be either 'True' or 'False'.
"""
G_CONFIG_PDF = {
    'page_size': 'A4',
    'margin': '0mm',
    'encoding': 'UTF-8',
    'enable_local_file_access': True,
    'pdf_options': {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': 'UTF-8',
        'enable-local-file-access': ""
    }
}


# =================== MAIN ===================
if __name__ == "__main__":
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else 'template.yml'
    css_file = sys.argv[2] if len(sys.argv) > 2 else 'template.css'
    cv = CVData(yaml_file)
    generate_html(cv, css_file)
