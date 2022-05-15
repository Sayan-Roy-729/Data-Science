import requests
import json

URL = "https://www.way2sms.com/api/v1/sendCampaign"


# get request
def send_post_request(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        "apikey": apiKey,
        "secret": secretKey,
        "usetype": useType,
        "phone": phoneNo,
        "message": textMessage,
        "senderid": senderId
    }
    return requests.post(reqUrl, req_params)


# get response
response = send_post_request(URL, "", "", "stage", "", "", "")
"""
Note:-
    You must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then request to api
"""

# print response
print(response.text)
