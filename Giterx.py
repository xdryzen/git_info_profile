import requests
import json
import os
os.system('clear')
on="""
\033[33mauthor: DEVLLNOOB\033[0m
"""
print on
print
zie=raw_input("users : ")
url="https://api.github.com/users/"+zie+""
R=requests.get(url).text
H=json.loads(R)
if "Not Found" in R:
        print "\033[31mid not found\033[0m"
else:
        print "name :", H["name"]
        print "user :", H["login"]
        print "id   :", H["id"]
        print "company :", H["company"]
        print "location :", H["location"]
        print "followers :", H["followers"]
        print "following :", H["following"]
