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

    #def logwrite():
        #df2 = df2.to_csv('p0f.csv', index=None, encoding='utf-8')
