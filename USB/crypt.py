#!/usr/bin/python
count = 0
new = ""
user_file = raw_input("Please enter full path of the file to encrypt/decrypt: ")
password = open("password.txt", "r").read()
pas_len = len(password)
f = open(user_file, "r")
current = open(user_file, "r").read()
for i in current:
    if count == pas_len:
        count = 0
    new = new + chr(ord(i) ^ ord(password[count]))
    count += 1
open(user_file, "w+").write(new)
print("Cryption Completed")
    
