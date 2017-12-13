# Chiron Home Based ML Intrusion Detection System

![Alt text](/docs/Chiron_Dashboard_V1.png?raw=true "Optional Title")

# Chiron VM Deployment Notes

VM Location: https://drive.google.com/open?id=18RgqJDFomkX6ZaXauqcADAtPHjFvdBfN

VM User Name: elk

VM Password: Elasticsearch5

Supporting Slides For Our Original Derbycon 2017 Prezi: https://docs.google.com/a/hackmiami.info/presentation/d/1ReyoUCfgMgQnygSR0XHuRrAQ3eUijM1q67riK1IIyHc/edit?usp=sharing


Notes for the OVA Image

1. The VM needs to be run with VirutalBox or VMWare and the .ova is built using virutal box.
2. After importing click on settings, then network. Make sure adapter 1 is selected and the Enable Network Adapter is checked. For the attached to option select Bridged Adapter.

/usr/share/elasticsearch/ /usr/share/kibana/ /usr/share/logstash/

3. Version Info 

Linux chironv1 4.10.0-28-generic #32~16.04.2-Ubuntu SMP Thu Jul 20 10:19:48 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux Ubuntu 16.04 LTS python3

Kibana 5.52 Elastic Search 5.5.2 Logstash 5.5.2

Nmap 7.01 p0f 2.08 scapy netcat-traditional


## Setting Development Environment For Editing The Chiron Source:

All python dependencies can be installed via pip3 and the included requirements.txt.
    
  pip3 install -r requirements.txt
 
These dependencies are also helpful to install (example via brew on OS X):

  brew install nmap

  brew install p0f
 
## 
