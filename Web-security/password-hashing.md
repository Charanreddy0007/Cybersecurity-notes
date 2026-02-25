#How passwords are saved in web applications
## The wrong way (plane text)

username | admin
password | password123

This is called plane text storage.

If the database gets leaked, all the passwords are get exposed.
This is very insecure.

## The correct way (Hashing)

Instead of storing the password itself, website store a HASH of the password.

Example:

username: admin
password: password123

The hash of "password123" will be "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
(After hashing in SHA-256)

In the data base it willbe stored as

username | admin
password | ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

## what is hasing?

Hashing 
- Is a one-way function 
- Converts the data into fixed length output (SHA256 is 64)
- cannot be reversed easily

You cannot "decrypt" a hash

Whana try Hashing use the python code to genrate SHA256 Hash in the same File named as "Hash.py"

## How Hackers can know the passwords in plaintext?

- Using the Rainbow table attack.
- Using the dictionary attack
- Brute-Force attack

To Prevent and slowdown this attacks devlopers use salt

## What is salt ?

salt is a random data genrated during the sign up and added to the password

Example:

password: Helloworld1234
salt: F#%^#B&D

Now the password will be "Helloworld1234F#%^#B&D"
The Hashing will be done to this new password 

# Why salting is important 

If two user have the same passowred:

Without Salt:
They will have identical hashs.

With Salt:
They will have different hashs

which increase the security 

## what i have learned

- Passwords should never be stored in plain text
- Hashing protects passwords
- Salting makes hashing stronger
- Common hashing algorithms: SHA256, bcrypt, Argon2, etc.