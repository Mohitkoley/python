import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid ammount of Argument \n Enter the IP")

print("_" * 50)
print("Scanning Target:" + target)
t1=datetime.now()
print("Scanning started at:" + str(t1))
print("_"* 50)



try:
    for port in range(1,100):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result ==0:
            print("port {} is open".format(port))
        s.close()
    t2=datetime.now()
    time_taken = t2-t1
    print("total time taken"+str(time_taken))

except KeyboardInterrupt:
    print("\n Excititng Program!!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could not be resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding")
    sys.exit()

