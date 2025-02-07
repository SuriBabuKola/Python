# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/createjira', methods=['POST'])
def create_jira_ticket():
    
    url = "https://nagasuribabu.atlassian.net/rest/api/3/issue"

    email = "nagasuribabu.k@gmail.com"
    api_token = "<api_token>"

    auth = HTTPBasicAuth(email, api_token)

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    data = request.get_json()

    comment = data.get("comment", {}).get("body", "")

    if "/jira" in comment:
        payload = json.dumps( {
          "fields": {
            "description": {
              "content": [
                {
                  "content": [
                    {
                      "text": "This is my first Ticket created in SampleScrumProject.",
                      "type": "text"
                    }
                  ],
                  "type": "paragraph"
                }
              ],
              "type": "doc",
              "version": 1
            },
            "issuetype": {
              "id": "10024"
            },
            "project": {
              "key": "SSP"
            },
            "summary": "My first Jira Ticket",
          },
          "update": {}
        } )

        response = requests.request(
           "POST",
           url,
           data=payload,
           headers=headers,
           auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return jsonify({"message": "No Jira ticket created, '/jira' not found in comment"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)