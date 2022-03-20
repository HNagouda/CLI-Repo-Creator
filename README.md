# CLI-Repo-Creator

Saves the hassle of manually creating repositories and pushing with SSH.

Built for Linux.

# Features
- Initializes a github repository locally
- Uses the pygithub library to create a repository online (i.e, on GitHub)
- Links both repos with a validated SSH token
- Copies templates (for example, a readme file) from your templates folder to the newly created repository folder. 
- Organizes projects by primary language used or category (ex, WebDev, ML, etc)

    ### All with a ***SINGLE*** CLI command

---

# How To Use: 

> ## Preperation
1. Make sure you have a valid and authenticated SSH key for GitHub 
   - More information can be found here: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

2. Make sure you have a vaild Personal Access token for GitHUB
   - More information can be found here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

---

> ## Setup

1. Clone the repository:
    ```bash
    $ git clone "https://github.com/HNagouda/Project-Creation-Automation.git"
    $ cd Project-Creation-Automation
    $ pip install -r requirements.txt 
    ```
    - **Note: It is recommended to create a new pip/conda env for the scripts to use.**
  
2. Open the `configs.yaml` file in the cloned repository and enter your credentials and paths in the given spaces - this includes your `PROJECTS_DIR`, `TEMPLATES_DIR`, `GITHUB_USERNAME` and `GITHUB_ACCESS_TOKEN`
   - **Note: If you do not have a templates folder, you may leave the `TEMPLATES_DIR` environment variable empty**

3. Copy the `configs.yaml` file to your scripts folder or any other folder you choose
   - **Note: This program could use an already existing `configs.yaml` file. If you wish to merge the variables in this particular file with your own variables, then copy the contents of this file to your `configs.yaml` file.**
  
4. Copy the two files; `create.exe` and `open.exe` into your scripts folder
   - **Note: This is essential for the scripts to work! The scripts and the `c`onfigs.yaml` files must be in the same directory.**

5. Add the scripts folder to your `PATH` by adding  the following lines to your `.bashrc` and/or `.zshrc`:
    ```bash
    PATH="/path/to/scripts:${PATH}"
    export PATH
    ```

6. If you have a new or already existing python environment, open the `creator.py` and `open.py` files and replace the `SHEBANG` in the first line with the path to your env's python executable

7. Give the scripts executable priveleges:
   ```bash
   $ chmod +x creator.py
   $ chmod +x open.py
   ```


> ## Usage
***Note: Following commands can be executed from any directory, as long as the scripts folder has been added to `PATH`.***

To get quick overview on the CLI arguments, run:
   ```bash
   $ creator.py -h 
   
   # usage: creator.py [-h] [-l [Lang]] -n Name [-t [{y,n}]]
   ```

To create a new repository, type the following from any directory in your shell:
   ```bash
   $ creator.py -l python -n project_name 
   
   # project directory will be created at /PROJECT_DIR/Python/Project-Name
   
   # Note: if you like organizing your projects by categories, then specify your category instead of a language for the `-l` argument
   
   # examples: 
   # creator.py -l WebDev -n project_name
   # creator.py -l ML -n project_name
   ```

If you wish to create a new project without a category or language, run:
   ```bash
   $ creator.py -n project_name

   # project directory will be created at /PROJECT_DIR/Project-Name
   ```


To open a folder/repository from your projects folder:
   ```bash
   $ open.py
   ```

## **Note: Feel free to rename the exe files to something of your preference!**

## Base Requirements

Python 3.0+  
Visual Studio Code 
