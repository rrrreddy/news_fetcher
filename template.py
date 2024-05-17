import os
from pathlib import Path
import logging

# Setting up logging to track the creation of directories and files
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "news_fetcher"

# List of directories and files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "tests/__init__.py",
    "tests/test_data_ingestion.py",
    "README.md",
    "setup.py",
    "LICENSE",
    "requirements.txt"
]

# Function to create directories and files
def setup_project(files):
    for filepath in files:
        filepath = Path(filepath)
        if not filepath.parent.exists():
            os.makedirs(filepath.parent, exist_ok=True)
            logging.info(f"Creating directory: {filepath.parent}")
        
        if not filepath.exists():
            filepath.touch()
            logging.info(f"Creating file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

# Run the setup function
setup_project(list_of_files)