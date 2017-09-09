import pandas as pd
import logging, os
import ipaddress


log = logging.getLogger(__name__)


nmap_df = pd.read_csv('data/nmap/nmap.tsv', delimiter='\t')
nmap_df.columns = ['host_and_fp', 'port']
nmap_df['host_and_fp'] = nmap_df['host_and_fp'].map(lambda x: x.lstrip('Host:').rstrip(''))
nmap_df['port'] = nmap_df['port'].map(lambda x: x.lstrip('Ports:').rstrip(''))
df3_hostfp = nmap_df[['host_and_fp']]
#df3_hostfp_check = df3.applymap(lambda x: IP(df3_hostfp).iptype())
nmap_df['host'] = nmap_df['host_and_fp'].apply(lambda x: x.split('(')[0])
nmap_df['c_public'] = nmap_df['host'].apply(lambda x: ipaddress.ip_network(x).is_global)
nmap_df['c_private'] = nmap_df['host'].apply(lambda x: ipaddress.ip_network(x).is_private)
sprivate_nmap_df = nmap_df.loc[nmap_df['s_private'] == True]
spublic_nmap_df = nmap_df.loc[nmap_df['s_private'] == False]


print (nmap_df)

#def logwrite():
#df3 = df3.to_csv('nmap.csv', index=None, encoding='utf-8')
