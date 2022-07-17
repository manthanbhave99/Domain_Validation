#/usr/bin/python3
__author__ = "Contributed by Manthan & Omprakash"

import subprocess as sp
import sys
import argparse
import requests, mmh3, codecs


parser = argparse.ArgumentParser(description="THIS IS Domain Validation Tool")
parser.add_argument("-d" , type= str,help="Type Domain" , required  = True)
p = parser.parse_args()
op = sp.getoutput("subfinder -silent -d "+ p.d)
print("\n" + op + "\n")
#	print(type(op))
f = open("subdomains.txt", "w")
f.write(op)

f = open("subdomains.txt", "r")
for i in f.readlines():
	try:
		h = "https://" + i.strip()
		h_s_code = requests.get(h).status_code
		g = "http://" + i.strip()
		g_s_code = requests.get(g).status_code

		f = open("alive.txt", "a")

		if int(h_s_code) == 200:
			f.write(h + " " + "[200]\n")
			f.close()
		if int(g_s_code) == 200:
			f.write(g + " " + "[200]\n")
			f.close()
	except:
		pass
f.close()


f = open("alive.txt" , "r")
for i in f.readlines():
	d = i.split()[0].strip() + "/favicon.ico"

	with open("hash.txt","w") as fav:
		favicon = codecs.encode(requests.get(d).content, "base64")
		hash = mmh3.hash(favicon)
		fav.write(d + str(hash) + '\n')
	fav.close()
f.close()

