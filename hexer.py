#!/usr/bin/python3

#Coded By Mhammad Al Abdullah (0xsecurity.com)

word2 = input('Enter a word: ')

def hex(string):
  word_bytes = string.encode('utf-8')
  word_bytes.decode('utf-8')
  ['{:x}'.format(b) for b in word_bytes]
  def bytes2hex(bytes):
      return '0x'+''.join('{:x}'.format(b) for b in bytes)
  return bytes2hex(string.encode('utf-8'))


print(hex(word2))
