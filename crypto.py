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

# MonomeDinome class
class MonomeDinome:
	# Initialize with two keys
	def __init__(self, dkw, lkw):
		self.digitsKey = self.digitsScramble(dkw)
		self.lettersKey = self.lettersScramble(lkw)

	# digitsScramble() - 
	def digitsScramble(self, dkw):
		# Create a list with the digitsKeyword given, adding characters if necessary to make it 10 characters long
		dkl = list((dkw.upper() + "ZZZZZZZZZZ")[0:10])

		for i in "0123456789":
			pos = self.findLowestLetter(dkl)
			if pos != -1:
				dkl[pos] = i

		return "".join(dkl)

	# findLowestLetter() - finds the lowest letter, alphabetically, in a list
	def findLowestLetter(self, list):
		pos = -1
		lowest = ''

		for i in range(len(list)):
			if list[i].isalpha():
				if (lowest == '') or (list[i] < lowest):
					lowest = list[i]
					pos = i

		return pos

	# lettersScramble() - combines W with/to V and J with/to I, outputs the whole alphabet with those combinations made??
	def lettersScramble(self, lkw):
		rlist = []
		for a in lkw.upper():
			if a == "W":
				a = "V"
			if a == "J":
				a = "I"
			if not a in rlist and a.isalpha():
				rlist.append(a)

		for a in "ABCDEFGHIKLMNOPQRSTUVXYZ":
			if not a in rlist:
				rlist.append(a)

		return "".join(rlist)

	# If the object is output as a string, return the two keys
	def __str__(self):
		return "digitsKey = " + self.digitsKey + "\n" + \
			   "lettersKey = " + self.lettersKey

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