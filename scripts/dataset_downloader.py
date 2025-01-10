import os 
import subprocess
import zipfile
from pathlib import Path
current_folder = Path.cwd()
parent_folder = current_folder.parent
#TODO fix directory
#downloads the kaggle data set from: username/dataset-name
def download_kaggle_dataset(dataset_location): #currently only downloads kaggle dataset
    #ensuring kaggle.json is found
    kaggle_dir = os.path.join(os.path.expanduser('~'), '.kaggle')
    if not os.path.exists(kaggle_dir):
        raise FileNotFoundError(f"{kaggle_dir} does not exist. Place your kaggle.json file in this directory.")
    #
    dataset_dir = str(parent_folder) + '\\'+ "data\\"
    os.makedirs(dataset_dir+dataset_location.split('/')[-1], exist_ok = True)
    
    result = subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset_location, '-p', dataset_dir], capture_output = True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error downloading dataset: {result.stderr}")
    print(result.stdout)

    print(Path.iterdir(dataset_dir))

 