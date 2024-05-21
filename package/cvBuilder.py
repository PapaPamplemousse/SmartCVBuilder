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
import os
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
    """
    add_content_to_page(profile_html)

def adding_work_experience(work_experience):
    """Adds work experience content to the HTML page using the provided information.

    :param work_experience: List of dictionaries containing work experience data.
    """
    experience_html = """
    <section class="experience">
        <h2>Experience</h2>
    """

    for job in work_experience:
        job_title = job.get('job_title', 'Job Title')
        company_name = job.get('company_name', 'Company Name')
        employment_dates_start = job.get('employment_dates_start', 'Start Date')
        employment_dates_end = job.get('employment_dates_end', 'End Date')
        job_description = job.get('job_description', 'Description of the role.')

        experience_html += f"""
        <article>
            <h3>{job_title} - <span class="company">{company_name}</span></h3>
            <p class="subdetails">{employment_dates_start} - {employment_dates_end}</p>
            <p>{job_description}</p>
        """

        # Check if there are any projects associated with the job
        projects = job.get('projects', [])
        if projects:
            for project in projects:
                project_name = project.get('project_name', 'Project Name')
                client = project.get('client', 'Client')
                project_description = project.get('project_description', 'Description of the project.')

                experience_html += f"""
                <div class="project">
                    <h4>{project_name}</h4>
                    <p><strong>Client:</strong> {client}</p>
                    <p>{project_description}</p>
                </div>
                """
        experience_html += "</article>"
    experience_html += "</section>"
    add_content_to_page(experience_html)


def adding_education_content(education):
    """Adds education content to the HTML page using the provided information.

    :param education: List of dictionaries containing education data.
    """
    education_html = """
    <section class="education">
        <h2>Education</h2>
    """
    for entry in education:
        degree = entry.get('degree', 'Degree')
        university_name = entry.get('university_name', 'University Name')
        attendance_dates_start = entry.get('attendance_dates_start', 'Start Date')
        attendance_dates_end = entry.get('attendance_dates_end', 'End Date')
        study_description = entry.get('study_description', 'Description of studies.')

        education_html += f"""
        <article>
            <h3>{degree}</h3>
            <p class="subdetails">{university_name} - {attendance_dates_start} - {attendance_dates_end}</p>
            <p>{study_description}</p>
        </article>
        """
    
    education_html += "</section>"

    add_content_to_page(education_html)


def adding_projects_content(projects):
    """Adds personal projects content to the HTML page using the provided information.

    :param projects: List of dictionaries containing project data.
    """
    projects_html = """
    <section class="projects-achievements">
        <h2>Projects & Achievements</h2>
    """

    for project in projects:
        project_title = project.get('project_title', 'Project Title')
        project_description = project.get('project_description', 'Description of the project.')
        project_link = project.get('project_link', '')

        projects_html += f"""
        <article>
            <h3>{project_title}</h3>
            <p>{project_description}</p>
        """
        
        if project_link:
            projects_html += f'<p><a href="{project_link}">View Project</a></p>'
        
        projects_html += "</article>"
    
    projects_html += "</section>"

    add_content_to_page(projects_html)


def adding_sidebar_content(skills, hobbies):
    """Adds sidebar content to the HTML page using the provided skills and hobbies lists.

    :param skills: List containing skill names.
    :param hobbies: List containing hobby names.
    """
    # Creating HTML list items for skills
    skill_items = ''.join([f'<li>{skill}</li>' for skill in skills if skill is not None])
    
    # Creating HTML list items for hobbies
    hobby_items = ''.join([f'<li>{hobby}</li>' for hobby in hobbies if hobby is not None])

    # Composing the sidebar section
    sidebar_html = """
    <div class="container">
        <aside class="sidebar">
    """

    if skills:
        sidebar_html += f"""
            <section class="skills">
                <h2>Skills</h2>
                <ul>
                    {skill_items}
                </ul>
            </section>
        """
    if hobbies:
        sidebar_html += f"""
            <section class="hobbies">
                <h2>Hobbies</h2>
                <ul>
                    {hobby_items}
                </ul>
            </section>
        """

    sidebar_html += """
        </aside>
        <main class="main-content">
    """

    add_content_to_page(sidebar_html)

def adding_social_links(social_links):
    NotImplemented

def ending_html_page():
    """
    Adds the closing HTML tags to the page.

    This function appends the necessary closing tags for the main content section,
    the body, and the HTML document. It ensures that the HTML structure is properly
    terminated.
    """
    ending_html= """
    </main>
    </div>
    </section>
    </body>
    </html>
    """
    add_content_to_page(ending_html)

def generate_html(cv,css_file,output_path):
    """
    Generates the complete HTML CV page and writes it to a file.

    This function orchestrates the creation of a complete HTML CV page by
    gathering personal information, skills, work experience, education, and projects
    from the provided CV object. It initializes the HTML structure, adds various
    sections to the page, and then writes the final HTML content to a specified file.

    :param cv: Object containing the CV data, including personal info, skills, work experience, education, and projects.
    :param css_file: Path to the CSS file to be linked in the HTML for styling.
    :param output_path: Directory path where the generated HTML file will be saved.
    """
    personal_info = cv.get_personal_info()
    skills = cv.get_skills()
    work_experience = cv.get_work_experience()
    education = cv.get_education()
    projects = cv.get_personal_projects()
    hobbies = cv.get_hobbies()
    social_link = cv.get_social_links()

    
    #create the html page 
    init_html_structure(css_file)
    adding_profile_content(personal_info)
    adding_sidebar_content(skills, hobbies)
    adding_work_experience(work_experience)
    adding_education_content(education)
    adding_projects_content(projects)
    #not implemented yet 
    adding_social_links(social_link)
    ending_html_page()

    # Creating file name from user name
    base_filename = "CV_" + personal_info['name'].replace(" ", "_")
    html_file = f"{base_filename}.html"

    html_output_path = os.path.join(output_path, html_file)

    # Writing HTML content to a file
    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(G_HTML_CONTENT)
