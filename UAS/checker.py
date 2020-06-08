import os.path
import sys
import hashlib
from os import path


me = '0001-mytest.txt'
sebela1 = '/noviarmdnfg/0001-mytest.txt/'
sebela2 = '/UAS/nugrahaa878/0001-mytest.txt/'

def CEKSAYA(me):
	fp = open(me)
	lines = fp.readlines()

	start = lines[0]
	last_line = lines[-1]
	day = ""

	print(start)

	for word in start:
		if "0" in word:
			idx_day = start.index(word, 0)
			first = start[idx_day]
			sec = start[idx_day + 1]
			day = str(first + sec)
			pass

	rec_time = "202006" + day
	print(rec_time)

	for time in start:
		if ":" in time:
			idx_col = start.index(time, 0)
			h1 = start[idx_col-2]  
			h2 = start[idx_col-1]
			hour = str(h1 + h2)
			min1 = start[idx_col+1]
			min2 = start[idx_col+2]
			minute = str(min1+min2)
			m1 = start[idx_col+4]
			m2 = start[idx_col+5]
			mili = str(m1+m2)
			pass

		if "P" in time:
			int_hour = int(hour) + 12
			hour = str(int_hour)

	string = "jsadbjasbdajsb"
	sha1(me)
	fp.close()

def sha1(str):
	sha1sum = hashlib.sha1(str.encode())
	result = print(sha1sum.hexdigest()[0:7])

print("Hai")

CEKSAYA(me)
