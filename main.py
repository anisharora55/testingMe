import requests

url = 'https://hookb.in/G90xNbkeW2HE2xPP2o0O'

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 95.0.4638.69 Safari/537.36 OPR/81.0.4196.61",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9x"
        }
res = requests.get("https://in.indeed.com/jobs?l=India&sort=date&limit=50&fromage=1", headers = headers, verify = False)
print(res.content) 
#return "Done!"

print("ok1")




data = res.content

r = requests.post(url, verify=False, data=data)
