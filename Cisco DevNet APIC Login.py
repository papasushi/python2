import requests

url = "https://sandboxapicem.cisco.com/api/v1/ticket"

payload = "{\n\t\"username\": \"devnetuser\",\n\t\"password\": \"Cisco123!\"\n}"
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)