from kidney_desiese_classifier.constants import *
from kidney_desiese_classifier.utils.common import read_yaml, create_directories
from kidney_desiese_classifier.entity.config_entity import (DataIngestionConfig,
                                                            PrepareBaseModelConfig,
                                                            TrainingConfig)
import os

class ConfigurationManager:
    def __init__(self,
                config_filepath = Config_file_path,
                params_filepath = params_file_path):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            data_file = config.data_file,
            unzip_data = config.unzip_data
        )
        
        return data_ingestion_config
    
    def get_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model = Path(config.updated_base_model_path),
            params_image_size = self.params.Image_size,
            params_learning_rate = self.params.Learning_rate,
            params_include_top = self.params.Include_top,
            params_weights = self.params.Weights,
            params_classes = self.params.Classes
        )
        
        return prepare_base_model_config
    
    def get_trainig_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_data, "unzip_data")
        
        create_directories([
            Path(training.root_dir)
        ])
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            parmas_epochs=params.Epochs,
            params_batch_size=params.Batch_size,
            params_is_augmented=params.Augmentation,
            params_image_size=params.Image_size
        )
        
        return training_config