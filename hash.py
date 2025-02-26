from flask_bcrypt import bcrypt
import math

password = "SecretPassword55"

def encode(password):
    password = password.encode()
    salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"
    return bcrypt.hashpw(password=password, salt=salt)

def check_password(hashed, entered):
    entered = entered.encode()

    if bcrypt.checkpw(entered, hashed) :
        return True
    else:
        return False

print(encode("test"))

print(check_password(encode("test"), "hi"))





'''
print(f"How actual password will appear in logs etc: {encoded_password.hex()}")

print(f"Actual Password: {encoded_password.decode()}")

print(f"Hashed Password: {hashed.decode()}")

print(f"Are they the same password: {bcrypt.checkpw(encoded_password, hashed)}")

#username = request.form.get("username") # Or email
#password = request. form.get ("password"). encode ("utf-8")

#Look user up in DB using username

if bcrypt. checkpw(password, hashed) :
    print("It matches!")
    #return redirect(url_for("user_profile"))
else:
    print ("Didn't match")
# flash("Invalid credentials", "warning")
'''
