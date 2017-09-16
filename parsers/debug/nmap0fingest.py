import pandas as pd
import logging, os
import ipaddress
#from pprint import pprint



pof_df = pd.read_csv('data/p0f/p0f.txt',sep='|',header=0, engine='python')
pof_df.columns = ['time','client_ip','server_ip','d','connection','mtu','g','raw_ip']
pof_df['client_ip'] = pof_df['client_ip'].map(lambda x: str(x)[4:])
pof_df['server_ip'] = pof_df['server_ip'].map(lambda x: str(x)[4:])
pof_df['mtu'] = pof_df['mtu'].map(lambda x:  x.lstrip('raw_mtu=langEnglishnonefreqdistHz').rstrip('=Hz'))
pof_df['time'] = pof_df['time'].map(lambda x:  x.lstrip('').rstrip('mod=mtu,cli=mod=syn+ackmod=uptimemod=httpreqmod= httpmod=host chang'))
pof_df['cip'] = pof_df['client_ip'].apply(lambda x: x.split('/')[0])
pof_df['c_public'] = pof_df['cip'].apply(lambda x: ipaddress.ip_address(x).is_global)
pof_df['c_private'] = pof_df['cip'].apply(lambda x: ipaddress.ip_address(x).is_private)
pof_df['sip'] = pof_df['server_ip'].apply(lambda x: x.split('/')[0])
pof_df['s_private'] = pof_df['sip'].apply(lambda x: ipaddress.ip_address(x).is_private)
sprivate_pof_df = pof_df.loc[pof_df['s_private'] == True]
spublic_pof_df = pof_df.loc[pof_df['s_private'] == False]


print (pof_df)


log = logging.getLogger(__name__)


nmap_df = pd.read_csv('data/nmap/nmap.tsv', delimiter='\t')
nmap_df.columns = ['host_and_fp', 'port']
nmap_df['host_and_fp'] = nmap_df['host_and_fp'].map(lambda x: x.lstrip('Host:').rstrip(''))
nmap_df['port'] = nmap_df['port'].map(lambda x: x.lstrip('Ports:').rstrip(''))
df3_hostfp = nmap_df[['host_and_fp']]
#df3_hostfp_check = df3.applymap(lambda x: IP(df3_hostfp).iptype())
nmap_df['host'] = nmap_df['host_and_fp'].apply(lambda x: x.split('(')[0])
nmap_df['host'] = nmap_df['host'].map(lambda x: x.lstrip().rstrip())
nmap_df['c_public'] = nmap_df['host'].apply(lambda x: ipaddress.ip_network(x).is_global)
nmap_df['c_private'] = nmap_df['host'].apply(lambda x: ipaddress.ip_network(x).is_private)
sprivate_nmap_df = nmap_df.loc[nmap_df['c_private'] == True]
spublic_nmap_df = nmap_df.loc[nmap_df['c_private'] == False]


print (nmap_df)

nmap0f_merged = pd.merge(pof_df, nmap_df, left_on=['name_indexcolumn_p0f_here'],right_on=['name_indexcolumn_nmap_here'], how='inner')