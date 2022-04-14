#!/usr/bin/env python3
import argparse
import base64


def base64(phrase):
  phrase_bytes = phrase.encode('ascii')
  print(phrase_bytes)
  return phrase_bytes





if __name__ == "__main__":
  parser = argparse.ArgumentParser(
  description='decoding string into base64'
  )
  parser.add_argument(
  '-phrase',
  '--phrase',
  action='store',
  dest='phrase',
  help='Decode into base64'
  )
  args = parser.parse_args()
  phrase = args.phrase
  base64(phrase)

