import re

text = "I am learning Python for DevOps"
pattern = r"Python"

match = re.match(pattern, text)

if match:
  print("Match Found=", match.group())
else:
  print("Match not Found")