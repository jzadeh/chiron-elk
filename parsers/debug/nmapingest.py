import pandas as pd
import logging, os
import IPy as IP


log = logging.getLogger(__name__)


df3 = pd.read_csv('nmap.tsv', delimiter='\t')
df3.columns = ['host&fp', 'port']
df3['host&fp'] = df3['host&fp'].map(lambda x: x.lstrip('Host:').rstrip(''))
df3['port'] = df3['port'].map(lambda x: x.lstrip('Ports:').rstrip(''))
df3_hostfp = df3[['host&fp']]
#df3_hostfp_check = df3.applymap(lambda x: IP(df3_hostfp).iptype())
df3['host&fp'] = df3['host&fp'].apply(lambda x: IP(df3_hostfp).iptype())

print (df3_hostfp_check)

#def logwrite():
#df3 = df3.to_csv('nmap.csv', index=None, encoding='utf-8')
