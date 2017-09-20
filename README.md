# USBCrypt
Use bitwise encryption to encrypt a file where the password and encryption/decryption program are stored on a USB device.

## Set up

Clone this rep and place the contents of the USB directory onto a USB drive.
Now change the value in password.txt to the passsword you want. This must remain the same when you run the code to encrypt as it is when you run the code to decrypt.

## Usage
Run the program from the USB drive.
It will encrypt/decrypt the selected file using the password in password.txt. By using bitwise encryption the same operation and password can be used to encrypt and decrypt the file.
Therefore to decrypt and encrypt a file you run the same code against it and aslong as the password remains the same it will encrypt and decrypt.
