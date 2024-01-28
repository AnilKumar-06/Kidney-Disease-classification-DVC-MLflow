from kidney_desiese_classifier.config.configuration import ConfigurationManager
from kidney_desiese_classifier.components.model_training import Training
from kidney_desiese_classifier import logger

stage = "Training stage"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_trainig_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> {stage} started >>>>>>>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> {stage} completed >>>>>>>>")
        
    except Exception as e:
        logger.exception(e)
        raise e