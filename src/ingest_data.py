import os
import zipfile
from abc import ABC,abstractmethod
import pandas as pd

## Define a abstract class for data ingestion 
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path:str) -> pd.DataFrame :
        """abstract method to ingest data from a give file"""
        pass
    

# implementation of concrete class for zip ingestion 
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path:str):
        """extract a .zip file and returns a content as pandas DF"""
        if not file_path.endswith(".zip"):
            raise ValueError("The provided path is not a .zip file")
        
        with zipfile.ZipFile(file_path, "r") as zip_ref :
            zip_ref.extractall("extracted_data")
            
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files) ==  0 :
            raise FileNotFoundError("No csv files where found in the extracted data")
        if len(csv_files)> 1:
            raise ValueError("found multiple csv files, please specify which one you need to use")
        
        # Read the CSV into a DataFrame
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        # Return the DataFrame
        return df




# Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")


# Example usage:
if __name__ == "__main__":
    # # Specify the file path
    file_path = r"C:\Users\amil\OneDrive\Documents\end-to-end-house_prediction\data\archive.zip"

    # # Determine the file extension
    file_extension = os.path.splitext(file_path)[1]

    # # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest(file_path)

    # # Now df contains the DataFrame from the extracted CSV
    print(df.head())  # Display the first few rows of the DataFrame
    pass