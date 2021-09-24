#!/bin/python3
import random

chars = 'abcdefghijklomnpqrstuvwxyz1234567890~!@#$%^&*()_+?<>-'

length = input('gennerated password length:')
length = int(length)

for p in range(3):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
