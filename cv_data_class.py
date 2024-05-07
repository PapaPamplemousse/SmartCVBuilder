import yaml
from typing import List, Dict, Any, Optional

class CVData:
    def __init__(self, file_path: str):
        with open(file_path, 'r') as file:
            self.data = yaml.safe_load(file)

    def get_personal_info(self) -> Dict[str, Any]:
        """Retourne les informations personnelles."""
        return self.data.get('cv', {}).get('personal_info', {})

    def get_work_experience(self) -> List[Dict[str, Any]]:
        """Retourne l'expérience professionnelle."""
        return self.data.get('cv', {}).get('work_experience', [])

    def get_education(self) -> List[Dict[str, Any]]:
        """Retourne la formation scolaire."""
        return self.data.get('cv', {}).get('education', [])

    def get_personal_projects(self) -> List[Dict[str, Any]]:
        """Retourne les projets personnels."""
        return self.data.get('cv', {}).get('personal_projects', [])

    def get_skills(self) -> List[str]:
        """Retourne les compétences."""
        return [skill['skill'] for skill in self.data.get('cv', {}).get('skills', [])]

    def get_social_links(self) -> List[str]:
        """Retourne les liens sociaux."""
        return [link['url'] for link in self.data.get('cv', {}).get('social_links', [])]

# Usage
cv = CVData('template.yml')
print(cv.get_personal_info())
print(cv.get_work_experience())
print(cv.get_education())
print(cv.get_personal_projects())
print(cv.get_skills())
print(cv.get_social_links())
