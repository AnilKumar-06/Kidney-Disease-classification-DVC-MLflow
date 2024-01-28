from kidney_desiese_classifier import logger
from kidney_desiese_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_desiese_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidney_desiese_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline

stage1 = "Data ingestion stage"

try:
    logger.info(f">>>>>>> {stage1} started >>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> {stage1} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


stage2 = 'Prepare Base model stage '

try:
    logger.info(f">>>>>>>>> {stage2} started >>>>>>>>>>>")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {stage2} completed >>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    
    
stage3 = "Model Training Stage"

try:
    logger.info(f">>>>>>>>>>{stage3} started >>>>>>>>>>")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {stage3} completed >>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e