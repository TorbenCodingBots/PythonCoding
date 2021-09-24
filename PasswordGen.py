#!/bin/python3
import random

chars = 'ABCDEFGHIJKLOMPQRSTUVWXYZabcdefghijklomnpqrstuvwxyz1234567890~!@#$%^&*()_+?<>-'

length = input('gennerated password length:')
length = int(length)

passwords = input('amount of passwords to geenerate:')
passwords = int(passwords)

for p in range(passwords):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)

