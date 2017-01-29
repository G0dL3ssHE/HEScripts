# DDOS NO VBRK REQUIRED #
import requests
sessID = input("PHPSESSID >> ")
target = input("TARGET IP >> ")
cookies = dict(PHPSESSID=sessID)
r = requests.post("https://legacy.hackerexperience.com/DDoS", data = {'ip':target}, cookies=cookies)
