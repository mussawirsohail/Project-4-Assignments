import hashlib

# Function to hash the password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login(email, password_to_check, stored_logins):
    stored_hash = stored_logins.get(email)
    if stored_hash is None:
        return False
    return stored_hash == hash_password(password_to_check)
stored_logins = {
    "mussawir@example.com": hash_password("securePassword123"),
    "john.doe@example.com": hash_password("mySafePass!"),
    "jane@example.com": hash_password("qwerty")
}

print(login("mussawir@example.com", "securePassword123", stored_logins))  # True
print(login("john.doe@example.com", "wrongPassword", stored_logins))      # False
print(login("unknown@example.com", "anything", stored_logins))            # False
