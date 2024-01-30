import requests

blocked_url = "http://unsafewebsite.com" #this is a website that securly always blocks
x = requests.get(blocked_url, verify=False)
print(x.text) #will return the HTML of the blocked website
