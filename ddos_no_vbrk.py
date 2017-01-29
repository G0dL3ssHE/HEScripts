# DDOS NO VBRK REQUIRED #
import requests
sessID = input("PHPSESSID >> ")
cookies = dict(PHPSESSID=sessID)
r = requests.post("https://legacy.hackerexperience.com/DDoS", data = {'ip':'147.92.224.218'}, cookies=cookies)
