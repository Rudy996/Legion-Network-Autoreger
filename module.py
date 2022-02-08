import urllib.request
import requests
import random
import string
import time
import sys
import re
import os
from bs4 import BeautifulSoup
import names
import undetected_chromedriver.v2 as uc



refferalCode = "8nJsXlZ"
global countOfSuc
countOfSuc = 5
chrome = uc.Chrome()
def request_api_legionnetwork_io():
	global countOfSuc
	req = urllib.request.Request("https://api.legionnetwork.io/api1/user/create")

	req.add_header("Content-Type", "application/json")
	req.add_header("cf-visitor", "https")
	req.add_header("User-Agent", "Legion/5.2 CFNetwork/1209 Darwin/20.2.0")
	req.add_header("Connection", "keep-alive")
	req.add_header("Accept", "application/json, text/plain, */*")
	req.add_header("Accept-Language", "ru")
	req.add_header("x-forwarded-proto", "https")
	req.add_header("Accept-Encoding", "gzip, deflate, br")
	name = string.ascii_lowercase + string.digits
	username = ''.join(random.choice(name) for i in range(10))
	nameOfAcc = names.get_first_name(gender='male')
	valueRandom1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(8))
	valueRandom2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(4))
	valueRandom3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(4))
	valueRandom4 = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(4))
	valueRandom5 = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(12))
	password = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(9))
	udid = f"{valueRandom1}-{valueRandom2}-{valueRandom3}-{valueRandom4}-{valueRandom5}"
	body = b"{\"password\":\""+str(password).encode('ascii') +b"!\",\"email\":\""+str(username).encode('ascii') +b"@oosln.com\",\"name\":\""+str(nameOfAcc).encode('ascii') +b"\",\"udid\":\""+str(udid).encode('ascii') +b"\",\"referralCode\":\""+str(refferalCode).encode("ascii")+b"\"}"
	try:
		response = urllib.request.urlopen(req, body)
		if(response.getcode()==200):
			print("Успешная регестрация спим на 5 сек, количество регистраций: "+str(countOfSuc))
			countOfSuc=countOfSuc+1
			time.sleep(5)
			f = open("LegionAccounts.txt", "a+", encoding="utf-8")
			f.write(f"{str(password)}!|{str(username)}@oosln.com|{str(nameOfAcc)}|{str(udid)}\n") 
			print(f"{str(password)}!|{str(username)}@oosln.com|{str(nameOfAcc)}|{str(udid)}")
			f.close()
			link = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain=oosln.com"
			r = requests.get(link)
			print(r.text)
			r_json = r.json()
			lenOfMail = len(r_json)
			while lenOfMail==0:
				print("Нету писем! спим на 3 сек")
				time.sleep(3)
				link = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain=oosln.com"
				r = requests.get(link)
				print(r.text)
				r_json = r.json()
				lenOfMail = len(r_json)
			latest_mail = r_json[0].get('id')
			print("Письмо!!!: "+str(r_json))
			req = requests.get(f"https://www.1secmail.com/mailbox/?action=mailBody&id={latest_mail}&login={username}&domain=oosln.com")
			bss = BeautifulSoup(req.text,'lxml')
			urlVerify = bss.find_all("a", href=True)[1]
			chrome.get(urlVerify.get("href"))
		else:
			print("Error!! : "+str(response.getcode()))
		response.close()
	except:
		print("Ошибка!!! Новый цикл!")
while True:
	request_api_legionnetwork_io()
	time.sleep(4)
