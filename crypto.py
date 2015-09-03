#!/usr/bin/env python3
# crypto.py
# Tutorial from jdege.us/crypto-python/ar01s04.html

import sys

# Text class for processing plaintext from a text file
class Text:
	# Main contstructor method
	def __init__(self, filename):
		self.load(filename)

	# load() for loading in the plaintext from text file
	def load(self, filename):
		fp = open(filename, "r")
		self.rawtext = fp.read()
		fp.close
		self.text = self.convert(self.rawtext)

	# convert() converts the plaintext to uppercase alpha characters
	def convert(self, txt):
		rval = ""
		for c in txt.upper():
			if c.isalpha():
				rval += c
		return rval

	# Output the text as a string, when called as a string, like print(text)
	# Format: Twelve 5 character groups per line (normal in cryptography)
	def __str__(self):
		rval = ""
		pos = 0
		for c in self.text:
			rval += c
			pos += 1
			if pos % 60 == 0:
				rval += '\n'
			elif pos % 5 == 0:
				rval += " "
		return rval

# If we are executing this script and not importing it
if __name__ == "__main__":

	# If the user has supplied a plaintext filename as an argument
	if len(sys.argv) == 2:
		# Create Text instance, passing the standard plaintext text file in the argument
		txt = Text(sys.argv[1])
	else:
		# Print argument usage and exit
		print("Usage: crypto.py <filename>")
		sys.exit(1)

	# Print our converted, formatted plaintext
	print(txt)