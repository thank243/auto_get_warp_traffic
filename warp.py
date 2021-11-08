import datetime
import json
import os
import random
import string
import time
import urllib.request


def digitString(string_len):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for _ in range(string_len)))
    except Exception as _:
        print(_)


def run():
    def genString(string_len):
        try:
            letters = string.ascii_letters + string.digits
            return ''.join(random.choice(letters) for _ in range(string_len))
        except Exception as _:
            print(_)

    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        return error


print('Getting WARP+ Traffic on Github Actions\n')
referrer = os.environ["DEVICEID"]
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
good = 0
bad = 0

while True:
    ret = run()
    if ret == 200:
        good = good + 1
        print(f"[-] WORK ON ID: {referrer}\n"
              f"[:)] {good} GB has been successfully added to your account.\n"
              f"[#] Total: {good} Good {bad} Bad")
        if good == 50:
            print("[*] Job completed!")
            break
        print("[*] After 18 seconds, a new request will be sent.\n")
        time.sleep(18)
    else:
        bad = bad + 1
        print(f"[:(] {ret}\n"
              f"[#] Total: {good} Good {bad} Bad\n"
              "[*] After 5 seconds, a new request will be sent.\n")
        time.sleep(5)
