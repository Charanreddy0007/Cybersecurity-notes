
# .encode() converts the string to bytes (required for hashing)
# .sha256() applies the Secure Hash Algorithm 256
# .hexdigest() converts the resulting binary data into a readable hex string
# os.urandom(16) creates 16 bytes of cryptographically strong random data.

import hashlib
import os

password = input("Enter your password: ") #Ask the user to enter password (plain Text)

# --- UNSALTED HASHING ---
unsalted_hash = hashlib.sha256(password.encode()).hexdigest()
print(f"Unsalted Hash : {unsalted_hash}")

# --- SALTED HASHING ---
salt = os.urandom(16) # Generate the salt


salted_password = password.encode() + salt # The salt is in bytes so we need to convert the password to bytes to add


salted_hash = hashlib.sha256(salted_password).hexdigest()

print(f"Salt : {salt}") # You must store the salt to verify the password later!
print(f"Salted Hash   : {salted_hash}")