import json
import logging
import os
import os.path
import sys

import kaggle
import pandas as pd
import regex as re
import simplejson  # fix for the "ValueError: Value is too big" error
from pandas import json_normalize
from sklearn import preprocessing
from tabulate import tabulate

logger = logging.getLogger(__name__)


def data_prep(data_dir, data_file):
    """[summary]
    """
    if not os.path.exists(data_dir):
        logger.info("Making data directory")
        print("Creating data diretory.")
        os.makedirs(data_dir)

    if os.path.exists(data_dir + data_file):
        logger.info("Found your dataset.")
        print("Found existing dataset.")
    else:
        logger.info("Downloading the dataset")
        print("Downloading the dataset.")
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            "apache-training-datajson", path=data_dir, unzip=True
        )


def parse_data(data):
    """[summary]

    Args:
        data ([type]): [description]
    """
    patterns = ['\r\n\r\n', '\\r\\n\\r\\n', '\r\r' '\n\n']
    for pattern in patterns:
        if pattern in data:
            headers = data.split(pattern)[0]
            html = data.replace(headers, "").strip()
            return({'headers': headers, 'html': html})


def parse_headers(headers):
    """[summary]

    Args:
        headers ([type]): [description]
    """
    output = {}
    patterns = ['\r\n', '\\r\\n', '\r' '\n']
    for pattern in patterns:
        if pattern in headers:
            header_lines = headers.split(pattern)
            for header_line in header_lines:
                key = header_line.split(":")[0].lower()
                value = header_line.replace(key, "").strip()
                output[key] = value
    return output


def read_data(data_dir, data_file):
    """[summary]

    Args:
        data_dir ([type]): [description]
        data_file ([type]): [description]

    Returns:
        [type]: [description]
    """
    rows = [] # send back these results

    try:
        file_object = open((data_dir + data_file), 'r')
        file_lines = file_object.readlines()
    except Exception as error:
        print(error)
        sys.exit(1)
    
    if file_lines is not None:
        for file_line in file_lines:
            service_data = json.loads(file_line)
            ip = service_data.get('ip_str')
            port = service_data.get('port')
            transport = service_data.get('transport')
            data = service_data.get('data')
            
            parsed_data = parse_data(data)
            #print(parsed_data)
            if parsed_data is not None:
                headers = parsed_data.get('headers')
                parsed_headers = parse_headers(headers)
                server = parsed_headers.get('server', '').split(' ')
                server.pop(0)
                rows.append([ip, transport, port, server])

    return rows


if __name__ == "__main__":
    """Prepare."""
    data_dir = "./data/"
    data_file = "Apache_Training_Data.json"
    pd.io.json._json.loads = lambda s, *a, **kw: pd.json_normalize(
        simplejson.loads(s)
    )  # fix for the "ValueError: Value is too big" error

    data_prep(data_dir, data_file)
    dataset = read_data(data_dir, data_file)

    df = pd.DataFrame(dataset,  columns = ['ip', 'transport', 'port', 'server'])

    print ("Count:", df.count())
    print ("\nData sample: \n", tabulate(df.head(), headers = 'keys', tablefmt = 'psql'))
