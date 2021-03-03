#!/usr/bin/python3

import csv 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source_file', type=str, required=True, help='The file you are appending a row to')
parser.add_argument('--new_file', type=str, required=True, help='The file containing the data used to append')
args = parser.parse_args()

os.chdir(os.path.expanduser('~/data/fred_data'))

def append_csv_as_row(source_file, new_file):

    with open(source_file,'a') as sourceFile:
        fileWriter = csv.writer(sourceFile)
        with open(new_file,'r') as newFile:
            fileReader = csv.reader(newFile)
            next(fileReader, None) # skip header row
            for row in fileReader:
                fileWriter.writerow(row)

append_csv_as_row(args.source_file, args.new_file)