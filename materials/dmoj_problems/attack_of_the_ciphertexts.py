# Attack of the CipherTexts
# https://dmoj.ca/problem/ccc06s2
# Stub

# Get the first two messages
plaintext = input()
ciphertext = input()

# A dictionary of cipher: plain
key = {}

# Map the relationship between cipher and plain letters
for i in range(len(plaintext)):
    plain = plaintext[i]
    cipher = ciphertext[i]
    key[cipher] = plain
    
# Get the new message to be decoded
new_ciphertext = input()
new_plaintext = ''

# Decipher the new plaintext
for char in new_ciphertext:
    if char in key:
        new_plaintext += key[char]
    else:
        new_plaintext += '.'

print(new_plaintext)
