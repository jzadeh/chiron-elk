import pandas as pd
import logging, os
#from pprint import pprint

#results = []
#with open('http.log') as inputfile:
#    for row in csv.reader(inputfile):
#        results.append(row)
#with pandas to pull stats if you want by higest nlargest lowest nsmallest

log = logging.getLogger(__name__)

class bro_ingestion:
    """Parse nmap related data

      Attributes:
      directory_to_parse: path to nmap data
      move_files_after_parsing: set to false if we want to retain files after parsing
      delog: to remove files in set directory
      inFile: to read data in log"""
    def __init__(self, directory_to_parse, move_files_after_parsing = True):
        self.directory = directory_to_parse
        self.flag = move_files_after_parsing

    def move_data(delog):
        #excute an os command to read all files in directory and delete
        os.system('rm '+delog)

    def bro_parse(inFile):
        df = pd.read_csv( inFile ,sep='\t', skiprows=[7], header=6)
        df_modified = df[df.columns[:-1]]
        df_modified.columns = df.columns[1:]
        tx_host = df_modified.groupby('tx_hosts')['ts'].count().sort_values().nlargest(25)
        rx_host = df_modified.groupby('rx_hosts')['ts'].count().sort_values()
        mime_type = df_modified.groupby('mime_type')['ts'].count().sort_values()
        md5 = df_modified.groupby('md5')['ts'].count().sort_values()
        txsumvalues = df_modified.groupby('tx_hosts')['seen_bytes'].sum().sort_values()
        txuniquevalues = df_modified.groupby('tx_hosts')['mime_type'].nunique().sort_values()
        rxsumvalues = df_modified.groupby('rx_hosts')['seen_bytes'].sum().sort_values()
        rxuniquevalues = df_modified.groupby('rx_hosts')['mime_type'].nunique().sort_values()
        txrx_sb = df_modified.groupby(['tx_hosts', 'rx_hosts'])['seen_bytes'].sum().sort_values()
    # def logwrite(bro):
        # df_modified = df_modified.to_csv('bro.csv', index=None, encoding='utf-8')
        return (df.modified)
