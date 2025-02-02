from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import os

tarball_path = Path("datasets/housing.tgz")
def download_dataset():

    if not tarball_path.is_file():
        path = Path("https://github.com/ageron/data/raw/main/housing.tgz")
        url="https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return Path("datasets/housing")

housing_data = download_dataset()
if housing_data.is_dir():
    if 'housing.csv' in os.listdir(housing_data):
        print("Dataset already downloaded")
    else:
        print("Extracting the dataset")
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
housing = pd.read_csv(housing_data / "housing.csv")
print(housing.head())