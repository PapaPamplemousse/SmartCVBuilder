"""
CV Main Script
===============

Author: Hugo REIF FAUDEMER
Creation Date: 07/05/2023
Purpose: This script serves as the main entry point for generating a CV in HTML format from a YAML file containing the CV data. It uses the `cvBuilder` module to process the data and create the HTML output.

Description
-----------

The script reads the CV data from a specified YAML file and applies a CSS file for styling. It then generates the HTML content of the CV and writes it to a file. The script also includes configurations for PDF generation, though this is not currently implemented.

Modules and Functions
---------------------

- `generate_html(cv, css_file)`: Function from `cvBuilder` that generates the HTML CV.
- `CVData(file_path: str)`: Class from `cvBuilder` that handles loading and accessing CV data from a YAML file.

Global Variables
----------------

- `G_CONFIG_PDF`: A dictionary configuring PDF generation settings.

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

Usage
-----

To use this script, run it from the command line with the YAML file and CSS file as arguments. If no arguments are provided, it defaults to 'template.yml' and 'template.css'.

Example:
    python cvMain.py my_cv.yml my_style.css

"""
import sys
import os
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
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else '../templates/template.yml'
    css_file = sys.argv[2] if len(sys.argv) > 2 else '../styles/style01.css'


    # Check and create output directory if it doesn't exist
    output_dir = '../output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cv = CVData(yaml_file)
    generate_html(cv, css_file, output_path=output_dir)
