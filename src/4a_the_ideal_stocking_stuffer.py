import hashlib

secret_key = 'ckczppom'
hex_md5 = ''
num_tries = 0

while not hex_md5.startswith('00000'):
  num_tries += 1
  hex_md5 = hashlib.md5(secret_key + str(num_tries)).hexdigest()

print(num_tries)
print(hex_md5)
