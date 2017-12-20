# Chiron Home Based ML Intrusion Detection System

CHIRON is a home analytics based on ELK stack combined with Machine Learning threat detection framework AKTAION. CHIRON parses and displays data from P0f, Nmap, and BRO IDS. CHIRON is designed for home use and will give great visibility into home internet devices (IOT, Computers, Cellphones, Tablets, etc). 

Once you export the .ova or extract zip, make sure you have an interfaced bridged to your network and CHIRON will do the rest. Browse to KIBANA http://chironip:5601 click on dashboard or visualizations and you should be able to get a great deal of info on whats going on at your home network. 

It can be quite surprising to see how many services, ports and outbound connections to rare destinations home devices make. CHIRON is not designed for enterprise and its current form is not scalable, there are other things like JASK Trident (www.jask.ai) that scale to enterprise traffic loads. CHIRON is also configured to do its tasks automatically including maintenance. We have included a basic troubleshooting guide in case ELK fails which is common unfortunately. 

CHIRON is integrated with AKTAION which detects exploit delivery ransomware/phishing. Aktaion will run every 4 hours against bro logs and it has a benign training data set that it compares against environment data set, once AKTAION finishes it produces files with exploit microbehaviors that can be seen in a visualizations by going into the visualization menu and selecting them. We expect to add support to the following protocols in the future

bluetooth
Zigbee
Wifi (Via Kismet)

![Alt text](/docs/Chiron_Dashboard_V1.png?raw=true "Optional Title")

# Chiron VM Deployment Notes

VM Location: 
.Zip (Vmware) https://drive.google.com/open?id=14z5FtllSgkGng-gfRpw0A0GCyWlUnvN5
.ova https://drive.google.com/open?id=167aQ5gTX04l4b1bngp7cIJIDnTJjbggU

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
