import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

if response.status_code == 200:
    pull_requests = response.json()

    pr_creators_list = {}

    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators_list:
            pr_creators_list[creator] += 1
        else:
            pr_creators_list[creator] = 1
    
    print("PR Creators and Counts: ")

    for creator, count in pr_creators_list.items():
        print(f"{creator}: {count} PRs")