import hashlib

increment = 0
key = 'cxdnnyjw'
password = ''

while len(password) != 8:
    md5_hash = hashlib.md5((key + str(increment)).encode('utf-8')).hexdigest()
    increment += 1

    if md5_hash.startswith('00000'):
        password = password + md5_hash[5]

print('The password for the door is', password)
