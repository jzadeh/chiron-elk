import pandas as pd
import logging, os
import ipaddress
#from pprint import pprint


bro_df = pd.read_csv('data/bro/benign1files.log' ,sep='\t', skiprows=[7], header=6)
bro_df_modified = bro_df[bro_df.columns[:-1]]
bro_df_modified.columns = bro_df.columns[1:]
#tx_host = df_modified.groupby('tx_hosts')['ts'].count().sort_values().nlargest(25)
#rx_host = df_modified.groupby('rx_hosts')['ts'].count().sort_values()
#mime_type = df_modified.groupby('mime_type')['ts'].count().sort_values()
#md5 = df_modified.groupby('md5')['ts'].count().sort_values()
#txsumvalues = df_modified.groupby('tx_hosts')['seen_bytes'].sum().sort_values()
#txuniquevalues = df_modified.groupby('tx_hosts')['mime_type'].nunique().sort_values()
#rxsumvalues = df_modified.groupby('rx_hosts')['seen_bytes'].sum().sort_values()
#rxuniquevalues = df_modified.groupby('rx_hosts')['mime_type'].nunique().sort_values()
#txrx_sb = df_modified.groupby(['tx_hosts', 'rx_hosts'])['seen_bytes'].sum().sort_values()
bro_df_modified['c_public'] = bro_df['tx_hosts'].apply(lambda x: ipaddress.ip_address(x).is_global)
bro_df_modified['c_private'] = bro_df['tx_hosts'].apply(lambda x: ipaddress.ip_address(x).is_private)
bro_df_modified['s_private'] = bro_df['rx_hosts'].apply(lambda x: ipaddress.ip_address(x).is_private)

print (bro_df_modified)