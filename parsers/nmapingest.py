import pandas as pd
import logging, os
#from pprint import pprint

class nmap_ingestion:
"""Parse nmap related data

  Attributes:
  directory_to_parse: path to nmap data
  move_files_after_parsing: set to false if we want to retain files after parsing
  delog: to remove files in set directory
  inFile: to read data in log"""

    def __init__(self, directory_to_parse, move_files_after_parsing = true):
        self.directory = directory_to_parse
        self.flag = move_files_after_parsing

    def move_data(delog):
#excute an os command to read all files in directory and delete
        os.system('rm '+delog)

    def nmap_parse(inFile):
        df3 = pd.read_csv( inFile, delimiter='\t',)
        df3.columns = ['host+fp','port']
        df3['host+fp'] = df3['host+fp'].map(lambda x:  x.lstrip('Host:').rstrip(''))
        df3['port'] = df3['port'].map(lambda x:  x.lstrip('Ports:').rstrip(''))
        #df3_modified = df3[df3.columns[:-1]]
        return (df3)
    #def logwrite():
        #df3 = df3.to_csv('nmap.csv', index=None, encoding='utf-8')
