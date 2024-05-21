"""
CV Data Management Script
==========================

Author: Hugo REIF FAUDEMER
Creation Date: 07/05/2023
Purpose: This script defines a class to handle operations related to Curriculum Vitae (CV) data stored in a YAML file. The class provides methods to retrieve various sections of the CV, such as personal information, work experience, education, personal projects, skills, and social links.

Description
-----------

The `CVData` class is designed to manage and extract data from a CV stored in a YAML file. It allows easy access to different sections of the CV, making it convenient to use this data for generating CVs in different formats or for further processing.

Modules and Functions
---------------------

- `__init__(self, file_path: str)`: Initializes the `CVData` object by loading data from the specified YAML file.
- `get_personal_info(self) -> Dict[str, Any]`: Retrieves personal information from the CV.
- `get_work_experience(self) -> List[Dict[str, Any]]`: Retrieves work experience entries from the CV.
- `get_education(self) -> List[Dict[str, Any]]`: Retrieves education history from the CV.
- `get_personal_projects(self) -> List[Dict[str, Any]]`: Retrieves personal projects from the CV.
- `get_skills(self) -> List[str]`: Retrieves a list of skills from the CV.
- `get_social_links(self) -> List[str]`: Retrieves social media and other relevant links from the CV.

Global Variables
----------------

None.

Usage
-----

To use this script, create an instance of `CVData` with the path to the YAML file containing the CV data. You can then call the provided methods to access different sections of the CV.

Example:
    cv = CVData('template.yml')
    print(cv.get_personal_info())
    print(cv.get_work_experience())
    print(cv.get_education())
    print(cv.get_personal_projects())
    print(cv.get_skills())
    print(cv.get_social_links())

"""
import yaml
from typing import List, Dict, Any


# =================== CLASSES ===================
class CVData:
    """
    A class to handle operations related to Curriculum Vitae (CV) data stored in a YAML file.

    Attributes:
        data (Dict[str, Any]): The CV data loaded from the YAML file.

    Methods:
        get_personal_info: Retrieves personal information from the CV.
        get_work_experience: Retrieves work experience entries from the CV.
        get_education: Retrieves education history from the CV.
        get_personal_projects: Retrieves personal projects from the CV.
        get_skills: Retrieves a list of skills from the CV.
        get_social_links: Retrieves social links from the CV.
    """

    def __init__(self, file_path: str):
        """
        Initializes the CVData object by loading data from the specified YAML file.

        :param file_path: The path to the YAML file containing the CV data.
        :type file_path: str
        """
        with open(file_path, 'r') as file:
            self.data = yaml.safe_load(file)

    def get_personal_info(self) -> Dict[str, Any]:
        """
        Retrieves personal information from the CV.

        :return: A dictionary containing personal information.
        :rtype: Dict[str, Any]
        """
        return self.data.get('cv', {}).get('personal_info', {})

    def get_work_experience(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of work experience entries from the CV.

        :return: A list of dictionaries, each representing a work experience entry.
        :rtype: List[Dict[str, Any]]
        """
        return self.data.get('cv', {}).get('work_experience', [])

    def get_education(self) -> List[Dict[str, Any]]:
        """
        Retrieves the education history from the CV.

        :return: A list of dictionaries, each representing an educational entry.
        :rtype: List[Dict[str, Any]]
        """
        return self.data.get('cv', {}).get('education', [])

    def get_personal_projects(self) -> List[Dict[str, Any]]:
        """
        Retrieves personal projects listed in the CV.

        :return: A list of dictionaries, each representing a personal project.
        :rtype: List[Dict[str, Any]]
        """
        return self.data.get('cv', {}).get('personal_projects', [])

    def get_skills(self) -> List[str]:
        """
        Retrieves a list of skills from the CV.

        :return: A list of skill names.
        :rtype: List[str]
        """
        return [skill['skill'] for skill in self.data.get('cv', {}).get('skills', [])]
    
    def get_hobbies(self) -> List[str]:
        """
        Retrieves a list of hobbies from the CV.

        :return: A list of hobbies names.
        :rtype: List[str]
        """
        return [hobbie['hobbie'] for hobbie in self.data.get('cv', {}).get('hobbies', [])]

    def get_social_links(self) -> List[str]:
        """
        Retrieves social media and other relevant links from the CV.

        :return: A list of URLs.
        :rtype: List[str]
        """
        return [link['url'] for link in self.data.get('cv', {}).get('social_links', [])]

