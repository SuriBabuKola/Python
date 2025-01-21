import re

text = "I am learning Python for DevOps"
pattern = r"Python"

search = re.search(pattern, text)

if search:
  print("Pattern Found:", search.group())   #Prints the matched text
  print("Start Position:", search.start())  #Start index of the match
  print("End Position:", search.end())      #End index of the match
else:
  print("Pattern not Found")