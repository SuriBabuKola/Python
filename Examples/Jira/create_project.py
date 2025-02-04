# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nagasuribabu.atlassian.net/rest/api/3/project"

email = "nagasuribabu.k@gmail.com"
api_token = "<api_token>"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "description": "My First Project",
  "key": "SSP",
  "leadAccountId": "712020:c03445fc-2b47-4515-9481-5c5af5f695b1",
  "name": "SampleScrumProject",
  "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum",
  "projectTypeKey": "software"
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))