import requests

url = "https://sandboxapicem.cisco.com/api/v1/ticket"

payload = "{\n\t\"username\": \"devnetuser\",\n\t\"password\": \"Cisco123!\"\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "3b644803-5bff-45bb-bf21-e42ce62c2594,a6db5946-58a2-4a03-ada8-772690191337",
    'Host': "sandboxapicem.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "55",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)