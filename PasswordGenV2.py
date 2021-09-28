import random

fh = open('passwords.txt', 'w')
chars = 'ABCDEFGHIJKLOMPQRSTUVWXYZabcdefghijklomnpqrstuvwxyz1234567890~!@#$%^&*()_+?<>-'

length = input('gennerated password length:')


websitename = input('Website for password')
username = input('Username')

fh.write('WebsiteName: ')
fh.write(websitename)
fh.write('\n')
fh.write('Username: ')
fh.write(username)
fh.write('\n')

# passwords = input('amount of passwords to geenerate:')
length = int(length)

# for p in range(passwords):
password = ''

for c in range(length):
  password += random.choice(chars)

fh.write('Password: ')
fh.write(password)
fh.close()
