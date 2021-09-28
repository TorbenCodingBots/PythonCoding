import random

fh = open('passowrd.txt', 'w')
chars = 'ABCDEFGHIJKLOMPQRSTUVWXYZabcdefghijklomnpqrstuvwxyz1234567890~!@#$%^&*()_+?<>-'

length = input('gennerated password length:')
length = int(length)
websitename = input('Website for password')
username = input('Username')

fh.write('Website: ' websitename '/n')
fh.write('Username: ' username '/n')

# passwords = input('amount of passwords to geenerate:')
# passwords = int(passwords)

# for p in range(passwords):
password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
  fh.write('Password:' password '/n'

fh.write('/n')  
fh.close()
