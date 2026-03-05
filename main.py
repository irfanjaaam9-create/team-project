def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"

print(login("admin","1234"))