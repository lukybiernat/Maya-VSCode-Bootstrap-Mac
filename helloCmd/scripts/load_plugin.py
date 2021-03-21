import sys
import telnetlib

port = 20200

if len(sys.argv) > 1:
    port = sys.argv[1]

try:
    tn = telnetlib.Telnet("localhost", port)
    tn.write('file -newFile -force;'.encode())
    tn.write('catchQuiet(`loadPlugin "helloCmd"`);'.encode())
    tn.close()
except:
    pass

