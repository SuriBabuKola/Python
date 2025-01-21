import re

text = "Git,Jenkins,Terraform,Docker,Kubernetes,Python"
pattern = r","

split_result = re.split(pattern, text)
print("Split Result:", split_result)