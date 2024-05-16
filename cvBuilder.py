"""
SmartCVBuilder Script
======================

Author: Hugo REIF FAUDEMER
Creation Date: 07/05/2023
Purpose: This script generates a SmartCV in HTML format using provided CV data. The script initializes the HTML structure, adds personal information, and outputs the final HTML content to a file.

Description
-----------

This script is designed to create a professional CV in HTML format. It takes in various sections of a CV, such as personal information, skills, work experience, education, and projects, and compiles them into a well-structured HTML document. The HTML content is styled using an external CSS file.

Modules and Functions
---------------------

- `init_html_structure(css_file)`: Initializes the HTML structure with basic HTML tags and includes a CSS file for styling.
- `add_content_to_page(content)`: Appends HTML content to the global HTML content variable.
- `adding_profile_content(personal_info)`: Adds personal profile information to the HTML content, including name, job title, email, phone number, and photo.
- `generate_html(cv, css_file)`: Main function that generates the complete HTML CV by combining all sections and writing the final HTML to a file.
- `to continue`:....
Global Variables
----------------

- `G_HTML_CONTENT`: A string containing the entire HTML page to be created.
- `G_CONFIG_HTML`: A dictionary configuring HTML generation settings, such as page size, margin, encoding, and local file access.

Usage
-----

To use this script, create an instance of `CVData` with the necessary CV information and call the `generate_html` function with the instance and the path to the CSS file.

"""
import sys
from cvDataClass import CVData


# =================== VARIABLES ===================
"""
G_HTML_CONTENT: str
    String containing the entire html page to be created
"""
G_HTML_CONTENT = f''' '''

"""
G_CONFIG_HTML: dict

A dictionary configuring html generation settings.

Attributes:
    page_size (str): The size of the page for the html, set to 'A4'.
    margin (str): The margins around the content of the html, set to '0mm' indicating no margin.
    encoding (str): The character encoding used in the html, set to 'UTF-8' to support a wide range of characters.
    enable_local_file_access (bool): A flag to determine whether local file access is permitted, set to True.
"""
G_CONFIG_HTML = {
    'page_size': 'A4',
    'margin': '0mm',
    'encoding': 'UTF-8',
    'enable_local_file_access': True,
}

# =================== FUNCTIONS ===================

def add_content_to_page(content):
    """Adds specific HTML content to the global HTML content variable.
    
    :param content: The HTML content to add to the global content.
    """
    global G_HTML_CONTENT
    G_HTML_CONTENT += content

   
def init_html_structure(css_file):
    """Initializes the global HTML content variable with a basic HTML structure using add_content."""
    global G_CONFIG_HTML
    initial_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="{encoding}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmartCVBuilder Generation</title>
        <link rel="stylesheet" href="{css}">
    </head>
    <body>
    """.format(encoding=G_CONFIG_HTML['encoding'], css=css_file)
    add_content_to_page(initial_html)


def adding_profile_content(personal_info):
    """Adds personal profile content to the HTML page using the provided information, omitting email, phone number, or photo if not provided.
    
    :param personal_info: Dictionary containing personal data such as name, photo URL, email, and phone number.
    """
    # Elements for email and phone number, shown only if provided
    email_html = f'<a href="mailto:{personal_info["email"]}">{personal_info["email"]}</a>' if 'email' in personal_info and personal_info['email'] else ''
    phone_html = personal_info['phone_number'] if 'phone_number' in personal_info and personal_info['phone_number'] else ''

    # Composing the contact details with proper separators
    contact_details = []
    if email_html:
        contact_details.append(email_html)
    if phone_html:
        contact_details.append(phone_html)
    contact_html = ' | '.join(contact_details)  # Joins parts with separator only if both parts exist

    # Element for the profile photo, shown only if the photo URL is provided
    photo_html = f"""
        <div class="profile-photo">
            <img src="{personal_info['photo_url']}" alt="{personal_info['name']}" class="profile-picture">
        </div>
    """ if 'photo_url' in personal_info and personal_info['photo_url'] else ''

    profile_html = f"""
    <section>
        <header>
            <div class="profile">
                {photo_html}
                <div class="profile-info">
                    <h1>{personal_info['name']}</h1>
                    <p>{personal_info['job']}{( ' | ' + contact_html if contact_html else '')}</p>
                </div>
            </div>
        </header>
    </section>
    """
    add_content_to_page(profile_html)


def generate_html(cv,css_file):
    personal_info = cv.get_personal_info()
    skills = cv.get_skills()
    work_experience = cv.get_work_experience()
    education = cv.get_education()
    projects = cv.get_personal_projects()

    init_html_structure(css_file)
    adding_profile_content(personal_info)

    # Creating file name from user name
    base_filename = "CV_" + personal_info['name'].replace(" ", "_")
    html_file = f"{base_filename}.html"

    # Writing HTML content to a file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(G_HTML_CONTENT)
