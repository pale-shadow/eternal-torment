#import logging
#import logging.config
import os
from tabulate import tabulate

import pandas as pd

from lib import helpers

def main():

    inputdir = os.getcwd() + "/../data/" # leave the leading slash
    data = helpers.Data(inputdir)

    for f in os.listdir(data.input_path):
        if f.endswith(".txt"):
            data.txt_files.append(f)
        if f.endswith(".json"):
            print("Found data file: {}".format(f))
            data.json_files.append(f)

    df = pd.DataFrame()

    for json_file in data.json_files:
        this_file = inputdir + json_file
        this_json = data.read_json_file(this_file)
        #data.pp_json(this_json) # pretty print for debug

        try:
            df = pd.read_json(this_file, orient="columns")
            print("Updated the data frame from file {}".format(this_file))
            #logger.debug("Updated the data frame from file {}".format(this_file))
        except Exception as e:
            #logger.error(e)
            print(e)

        df.info()

        test_df = pd.DataFrame()
        new_df = pd.DataFrame()

        element = 'name'
        if element in df.columns and not (df[element].empty):
            new_df = df.explode(element)

        for line in new_df[element]:
            try:
                print ("Found a column: {}".format(line))
                if 'domain' in line and not (new_df['data'].empty):
                    test_df = new_df['data']
            except Exception as e:
                print(e)
        rows = test_df.shape[0]
        exit (0)
        i = 0
        while i < rows:
            if test_df[i]:
                print(test_df[i])
            i += 1


if __name__ == "__main__":
    main()
