
from steps.data_ingestion_step import data_ingestion_step
from steps.handling_missing_value_step import handle_missing_values_step

from zenml import Model,pipeline, step


@pipeline(
    model =Model(
    # the name uniquely identify the mode
    name="the-price-predictor"),
)

def ml_pipeline():
    # end-to-end ml pipeline
    raw_data = data_ingestion_step(file_path =
                                   r"C:\Users\amil\OneDrive\Documents\end-to-end-house_prediction\data\archive.zip")
    
    #next step is handling the missing values 
    
    filled_data = handle_missing_values_step(raw_data)
    







