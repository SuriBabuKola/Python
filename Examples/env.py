import os

user_name = os.getenv("username")
password = os.getenv("password")

print(f"Username: {user_name}")
print("Password:", password)