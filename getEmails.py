import datetime
import json
import eml_parser
import os
from pprint import pprint
from itertools import filterfalse	

def unique_everseen(iterable, key=None):
	"List unique elements, preserving order. Remember all elements ever seen."
	seen = set()
	seen_add = seen.add
	if key is None:
		for element in filterfalse(seen.__contains__, iterable):
			seen_add(element)
			yield element
	else:
		for element in iterable:
			k = key(element)
			if k not in seen:
				seen_add(k)
				yield element

def unique_words(string, ignore_case=False):
	key = None
	if ignore_case:
		key = str.lower
	return "\n".join(unique_everseen(string.split(), key=key))

def json_serial(obj):
	if isinstance(obj, datetime.datetime):
		serial = obj.isoformat()
		return serial

def readAddress(emlFile):
	error = False
	with open(emlFile, 'rb') as fhdl:
		raw_email = fhdl.read()
	try:
		parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email)
	except:
		print("Error decoding the eml file")
		print("[!] Skipping...")
		error = True
	if not error:
		with open('mails.txt', 'a') as f:
			#pprint(parsed_eml["header"])
			# this is to avoid printing empty strings because of #27257 https://bugs.python.org/issue27257
			if hasattr(parsed_eml["header"],"from"):
				if parsed_eml["header"]["from"]:
					print(parsed_eml["header"]["from"], file=f)
			elif hasattr(parsed_eml["header"],"return-path"):
				print(parsed_eml["header"]["return-path"], file=f)
			if parsed_eml["header"]["to"]:
				print(*parsed_eml["header"]["to"], sep='\n', file=f)
			if hasattr(parsed_eml["header"], "cc"):
				print(*parsed_eml["header"]["cc"], sep='\n', file=f)
			if hasattr(parsed_eml["header"], "bcc"):
				print(*parsed_eml["header"]["bcc"], sep='\n', file=f)


for root, dirs, files in os.walk("./"):
	for file in files:
		if file.endswith(".eml"):
			print("Scanning {}/{}...".format(root,file))
			readAddress(os.path.join(root, file))

with open('mails.txt', 'r') as mailsFile:
	mails=mailsFile.read()
	uniqueMails = unique_words(mails)

with open('mails.txt', 'w') as mailsFile:
	mailsFile.write(uniqueMails)