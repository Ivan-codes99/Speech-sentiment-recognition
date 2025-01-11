import os 
import subprocess
import zipfile
from pathlib import Path

#TODO: Add support for non-kaggle datasets
#TODO: Add function to unzip dataset.zip file
script_location = Path(__file__).resolve().parent
parent_folder = script_location.parent

#*Kaggle datasets can have the same name, but only from different users, so including the username to prevent duplicates
def verify_kaggle_credentials():
    #ensuring kaggle.json is found
    kaggle_dir = os.path.join(os.path.expanduser('~'), '.kaggle')
    if not os.path.exists(kaggle_dir):
        raise FileNotFoundError(f"{kaggle_dir} does not exist. Place your kaggle.json file in this directory.")

def kaggle_dataset_exists(dataset_name): #*checks for dataset on kaggle
    result = subprocess.run(['kaggle', 'datasets', 'list', '-s', dataset_name], capture_output=True, text=True)
    if result.returncode != 0:
        error_message = result.stderr if result.stderr else "Unknown error occurred"
        raise Exception(f"Error checking if dataset exists: {error_message}")
    
    # Parsing the table-like output manually
    datasets = result.stdout.strip().split('\n')
    for dataset in datasets[1:]:  # Skip the header line
        columns = dataset.split()
        if columns[0] == dataset_name:
            return True
    return False

#downloads the kaggle data set from: https://www.kaggle.com/datasets/kaggleuser/dataset
def download_kaggle_dataset(dataset_name): #*dataset_name is in the format kaggleuser/dataset
    try:
        verify_kaggle_credentials()
        if not kaggle_dataset_exists(dataset_name):
            raise Exception(f"Dataset {dataset_name} does not exist on Kaggle.")
        dataset_dir = str(parent_folder) + "\\" + "data\\"
        dataset_dir += dataset_name.replace('/','-')
    
        os.makedirs(dataset_dir)
        os.makedirs(dataset_dir+"\\raw", exist_ok= True)
        os.makedirs(dataset_dir+"\\processed", exist_ok= True)
        os.makedirs(dataset_dir+"\\sample", exist_ok= True)

        result = subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', dataset_dir + "\\raw"], capture_output = True, text=True)
        if result.returncode != 0:
            error_message = result.stderr if result.stderr else "Unknown error occurred."
            raise Exception(f"Error downloading dataset: {error_message}")
        print(result.stdout)
    except FileExistsError as e:
        print(f"This dataset already exists: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Exception caught: {e}")
    
    