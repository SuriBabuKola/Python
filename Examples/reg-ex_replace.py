import re

text = "I am learning Python for DevOps"
pattern = r"DevOps"

replacement = "Company Requirement"

new_text = re.sub(pattern, replacement, text)
print("Modified Text:", new_text)