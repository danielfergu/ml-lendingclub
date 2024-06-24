import requests
import gzip
import shutil

def download_and_unzip_gz(url, download_path, output_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(download_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    with gzip.open(download_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

url = 'https://dfgwebpersonal.s3.amazonaws.com/dataset_half.csv.gz'
download_path = 'dataset.gz'
output_path = 'dataset.csv'

# Call the function to download and unzip the file
download_and_unzip_gz(url, download_path, output_path)
