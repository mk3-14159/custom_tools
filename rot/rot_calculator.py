#!/usr/bin/env python3
import binascii
import codecs
import argparse

def rot(phrase):
  decoded = codecs.decode(phrase, 'rot_13')  
  return decoded

def main():
  parser = argparse.ArgumentParser(
  description='decode rot13 algorithm'
  )
  parser.add_argument(
  '-phrase', 
  '--phrase', 
  action='store', 
  dest='phrase', 
  help='Decode rot13 passphrase'
  )
  args = parser.parse_args()
  phrase = args.phrase
  print(rot(phrase))
 
if __name__ == "__main__":
  main()
  
