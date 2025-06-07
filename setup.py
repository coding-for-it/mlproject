# Importing necessary functions from setuptools
# setup → used to define package details
# find_packages → auto-discovers Python packages in the project folder
from setuptools import find_packages, setup

# For type hinting the return type of get_requirements()
from typing import List

# A special string that appears in requirements.txt to indicate "editable mode"
HYPHEN_E_DOT = '-e .'

# Function to read dependencies from requirements.txt
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of required packages
    by reading from the given file (usually requirements.txt)
    '''
    requirements = []
    
    # Open and read all lines from the file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
        # Remove newline characters from each line
        requirements = [req.replace("\n", "") for req in requirements]

        # If "-e ." is present, remove it (not a real package)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    # Return the clean list of requirements
    return requirements

# Now, we call the setup function to define the package details
setup(
    name='mlproject',                          # Package/project name
    version='0.0.1',                           # Version of your project
    author='Nimisha',                          # Author name
    author_email='nvrajendra42@gmail.com',     # Author email
    packages=find_packages(),                  # Automatically find all packages in this project folder
    install_requires=get_requirements('requirements.txt')  # Install dependencies from requirements.txt
)
