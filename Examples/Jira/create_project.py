# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "assigneeType": "PROJECT_LEAD",
  "avatarId": 10200,
  "categoryId": 10120,
  "description": "Cloud migration initiative",
  "issueSecurityScheme": 10001,
  "key": "EX",
  "leadAccountId": "5b10a0effa615349cb016cd8",
  "name": "Example",
  "notificationScheme": 10021,
  "permissionScheme": 10011,
  "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
  "projectTypeKey": "business",
  "url": "http://atlassian.com"
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))