from kidney_desiese_classifier.config.configuration import ConfigurationManager
from kidney_desiese_classifier.components.prepare_base_model import PrepareBaseModel
from kidney_desiese_classifier import logger

stage = "prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        parepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=parepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> {stage} stage started >>>>>>>>>")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {stage} stage completed >>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e