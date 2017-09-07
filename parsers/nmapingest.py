import pandas as pd
import logging, os
import IPy as IP

log = logging.getLogger(__name__)

df3 = pd.read_csv('data/nmap/nmap.tsv', delimiter='\t')
df3.columns = ['host_and_fingerprint', 'port']
df3['host_and_fingerprint'] = df3['host_and_fingerprint'].map(lambda x: x.lstrip('Host:').rstrip(''))
df3['port'] = df3['port'].map(lambda x: x.lstrip('Ports:').rstrip(''))
#df3_hostfp_check = df3.applymap(lambda x: IP(df3_hostfp).iptype())
df3['ip'] = df3['host_and_fingerprint'].apply(lambda x: x.split(' ')[1])
#df3['host_and_fingerprint'] = df3['host_and_fingerprint'].apply(lambda x: IP(df3_hostfp).iptype())

print (df3)

#def logwrite():
#df3 = df3.to_csv('nmap.csv', index=None, encoding='utf-8')
