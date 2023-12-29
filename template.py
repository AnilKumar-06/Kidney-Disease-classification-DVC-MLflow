import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

p_name = "kidney_desiese_classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{p_name}/__init__.py",
    f"src/{p_name}/components/__init__.py",
    f"src/{p_name}/utils/__init__.py",
    f"src/{p_name}/config/__init__.py",
    f"src/{p_name}/config/configuration.py",
    f"src/{p_name}/pipeline/__init__.py",
    f"src/{p_name}/entity/__init__.py",
    f"src/{p_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for f_path in list_of_files:
    f_path = Path(f_path)
    f_dir, f_name = os.path.split(f_path)
    
    if f_dir != "":
        os.makedirs(f_dir, exist_ok=True)
        logging.info(f"Creating directory: {f_dir} for the file: {f_name}")
        
    if(not os.path.exists(f_path)) or (os.path.getsize(f_path) == 0):
        with open(f_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {f_path}")
    else:
        logging.info(f"{f_name} is already exists!")
        