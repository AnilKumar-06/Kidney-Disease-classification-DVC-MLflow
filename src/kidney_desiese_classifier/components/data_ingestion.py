import os
import zipfile
import gdown
from kidney_desiese_classifier import logger
from kidney_desiese_classifier.utils.common import get_size
from kidney_desiese_classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def  __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self) -> str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.root_dir
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/file/d/export=download&id="
            
            gdown.download(prefix+file_id, zip_download_dir)
            
            logger.info(f"Download data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_data
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.data_file, 'r') as f:
            f.extractall(unzip_path)
