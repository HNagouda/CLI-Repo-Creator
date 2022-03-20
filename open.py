#! SHEBANG

"""
Lists all projects in the project directory
Opens user selected project in VSCode
"""

import os
import yaml

class project_opener():
    def __init__(self):
        # Get Configs from YAML file
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(os.path.join(dir_path, 'configs.yaml'), 'r') as f:
            cfgs = yaml.safe_load(f)
            cfgs = cfgs['REPO_CREATOR_CONFIGS']

            self.projects_dir = cfgs['PROJECTS_DIR']
            self.github_username = cfgs['GITHUB_USERNAME']

    def welcome_user(self):
        print(f"""\n=============== Welcome Back, {self.github_username}! =============== \n""")

    def open_project(self):
        # Displaying all the languages in the directory
        print("Folders in your project directory:")
        languages = [f.name for f in os.scandir(self.projects_dir) if f.is_dir()]
        for i, lang in enumerate(languages):
            print(f"\t{i}. {lang}")

        chosen_lang_index = int(input("\nWhich language is your project using? [number]: "))
        chosen_lang = languages[chosen_lang_index]
        chosen_lang_path = os.path.join(self.projects_dir, chosen_lang)

        print(f"\nThese are your current {chosen_lang} projects: ")
        projects = [f.name for f in os.scandir(chosen_lang_path) if f.is_dir()]
        for i, project in enumerate(projects):
            if os.path.isdir(os.path.join(chosen_lang_path, project)): 
                print(f"\t{i}. {project}")

        # Gathering info for opening the project
        project_number = int(input("\nWhich project would you like to open? [number]: "))
        project_name = projects[project_number]
        project_path = os.path.join(chosen_lang_path, project_name)
        print(project_path)

        os.system(f"cd {project_path} && code .")
    
    def run_all(self):
        functions = [
            self.welcome_user,
            self.open_project
        ]

        for function in functions:
            function()

            
if __name__ == "__main__":
    project_opener().run_all()

    

