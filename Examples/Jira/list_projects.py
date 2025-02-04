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
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

print("Project Names:")
for project in output:
    print(f" - {project["name"]}")