
from steps.data_ingestion_step import data_ingestion_step
from steps.handling_missing_value_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outliers_detection_step import outlier_detection_step
from steps.data_splitter_step import data_splitter_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step





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
    
    engineered_data = feature_engineering_step(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )
    
    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")
    
    X_train, X_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")
    
    # Model Building Step
    model = model_building_step(X_train=X_train, y_train=y_train)
    
    evaluation_metrics, mse = model_evaluator_step(
        trained_model=model, X_test=X_test, y_test=y_test
    )








