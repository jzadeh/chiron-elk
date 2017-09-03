import pandas as pd
#from pprint import pprint

#results = []
#with open('http.log') as inputfile:
#    for row in csv.reader(inputfile):
#        results.append(row)
#with pandas to pull stats if you want by higest nlargest lowest nsmallest

#class Chiron():
    #def BroHtttpParse(inFile):
df = pd.read_csv( 'benign1files.log',sep='\t', skiprows=[7], header=6)
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

    #def P0fParse(inFile):
df2 = pd.read_csv( 'p0f.txt',sep='|',header=0, engine='python')
df2.columns = ['time','client_ip','server_ip','d','connection','mtu','g','raw_ip']
df2['client_ip'] = df2['client_ip'].map(lambda x: str(x)[4:])
df2['server_ip'] = df2['server_ip'].map(lambda x: str(x)[4:])
df2['mtu'] = df2['mtu'].map(lambda x:  x.lstrip('raw_mtu=langEnglishnonefreqdistHz').rstrip('=Hz'))
df2['time'] = df2['time'].map(lambda x:  x.lstrip('').rstrip('mod=mtu,cli=mod=syn+ackmod=uptimemod=httpreqmod= httpmod=host chang'))

    #def NMapParse(inFile):
df3 = pd.read_csv('nmap.tsv', delimiter='\t',)
df3.columns = ['host+fp','port']
df3['host+fp'] = df3['host+fp'].map(lambda x:  x.lstrip('Host:').rstrip(''))
df3['port'] = df3['port'].map(lambda x:  x.lstrip('Ports:').rstrip(''))
#df3_modified = df3[df3.columns[:-1]]

print (df3.replace)

#df2['raw_ip'] = df2['raw_ip'].map(lambda x:  x.lstrip('asd').rstrip('mod=mtu,cli=mod=syn+ackmod=uptimemod=httpreqmod= httpmod=host chang'))

#df2_new = df2[df2['raw_ip'].notnull()] DONT USE *Null lines*
#df2['raw_ip'] = df2['raw_ip'].map(lambda x:  x.lstrip('').rstrip(''))

    #def logwrite():
#df_modified = df_modified.to_csv('bro.csv', index=None, encoding='utf-8')
#df2 = df2.to_csv('p0f.csv', index=None, encoding='utf-8')
#df3 = df3.to_csv('nmap.csv', index=None, encoding='utf-8')



#df2_pIp = df.groupby('b').count()
#df2['b'] = df.b.str.replace('cli=,?' , '')
#df2['b'] = df2['b'].apply(lambda x: rstrip('cli='))

    #dcf = df_modified.groupby([('tx_hosts')],as_index=False).count()
    #df_topIp = df_modified[('tx_hosts')]
    #.groupby([('')]).count()
    #df.drop(['#fields'], axis=1).hist()
    #s = df['id.orig_p'].groupby(df['id.orig_p']).value_counts() 'Doesnt work'

#rx_hosts
