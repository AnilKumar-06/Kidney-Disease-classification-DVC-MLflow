import os
from box.exceptions import BoxValueError
import yaml
from kidney_desiese_classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {yaml_path} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty!")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(directory_path: list, verbose=True):
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            

@ensure_annotations
def save_json(path:Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    
    
    
@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path, 'r') as f:
        content = json.load(f)
        
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at : {path}")
    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    size = round(os.path.getsize(path)/1024)
    return f"~{size} KB"


def decodeImage(imgstr, fName):
    img_data = base64.b64decode(imgstr)
    with open(fName, 'wb') as f:
        f.write(img_data)


def encodeImage(cropImagPath):
    with open(cropImagPath, 'rb') as f:
        return base64.b64encode(f.read())