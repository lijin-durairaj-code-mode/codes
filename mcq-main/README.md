<!-- import steps to follow -->

<!-- 1. add .env file to .gitignore file  -->
<!-- 2. in the requirements.txt file add all the package which u need to install -->
<!-- 3. add -e . at the bottom of the requirements.txt file so that it wud install all the packages inside the local environment -->
<!-- 4. add the following code inside setup.py file 
from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version=0.0.1,
    author='Lijin Durairaj', 
    author_email='durairaj.lijin@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
) -->

<!-- 5. run -> pip install -r requirements.txt -->