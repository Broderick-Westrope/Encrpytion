from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
key_location = "my_key.bin" # A safe place to store a key. Can be on a USB or even locally on the machine (not recommended unless it has been further encrypted)

# Generate the key

salt = b'\x8a\xfe\x1f\xa7aY}\xa3It=\xc3\xccT\xc8\x94\xc11%w]A\xb7\x87G\xd8\xba\x9e\xf8\xec&\xf0' # Salt you generated
password = 'password123' # Password provided by the user, can use input() to get this
key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with
output_file = 'encrypted.bin'
data = b'Your data....'


# Save the key to a file
file_out = open(key_location, "wb") # wb = write bytes
file_out.write(key)
file_out.close()

# Later on ... (assume we no longer have the key)
file_in = open(key_location, "rb") # Read bytes
key_from_file = file_in.read() # This key should be the same
file_in.close()

# Since this is a demonstration, we can verify that the keys are the same (just for proof - you don't need to do this)
assert key == key_from_file, 'Keys do not match' # Will throw an AssertionError if they do not match



###ENCRYPTION
cipher = AES.new(key, AES.MODE_EAX) # EAX mode
ciphered_data, tag = cipher.encrypt_and_digest(data) # Encrypt and digest to get the ciphered data and tag

file_out = open(output_file, "wb")
file_out.write(cipher.nonce) # Write the nonce to the output file (will be required for decryption - fixed size)
file_out.write(tag) # Write the tag out after (will be required for decryption - fixed size)
file_out.write(ciphered_data)
file_out.close()



###DECRYPTION

input_file = output_file # Input file (encrypted)

file_in = open(input_file, 'rb')
nonce = file_in.read(16) # Read the nonce out - this is 16 bytes long
tag = file_in.read(16) # Read the tag out - this is 16 bytes long
ciphered_data = file_in.read() # Read the rest of the data out
file_in.close()

# Decrypt and verify
cipher = AES.new(key, AES.MODE_EAX, nonce)
original_data = cipher.decrypt_and_verify(ciphered_data, tag) # Decrypt and verify with the tag

print(original_data)