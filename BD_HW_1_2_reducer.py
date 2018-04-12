#!/usr/bin/env python
'''
Abishek Ganesh
Quest 2:
Your task is to compute how many times every term occurs across titles, for each author.
For example, the author Alberto Pettorossi has the following terms occur in titles with 
the indicated cumulative frequencies (across all his papers): 
program:3, transformation:2, transforming:2, using:2, programs:2, and logic:2. 

Reducer: 
'''
import sys
import pprint
import json
import operator
class Reducer(object):
	def __init__(self, stream, sep='\t'):
		'''Initilization'''
		self.stream = stream
		self.sep = sep
	def emit(self, key, value):
		sys.stdout.write('{0}:{1}\n'.format(key,value))
		
	def __iter__(self):
		for line in self.stream:
			try:
				auth = line.split('\t')[0]
				word = line.split('\t')[1]
				count = int(line.split('\t')[-1])
				yield auth,word,count
			except:
				continue
			
	def reduce(self):
		publis_dict={}
		for auth, word, count in self:
			if auth in publis_dict:
				if word in publis_dict[auth]:
					publis_dict[auth][word]+=count
				else:
					 publis_dict[auth][word]=count
			else:
				publis_dict[auth]={word:count}
				
		for auth in publis_dict.keys():
			self.emit(auth, publis_dict[auth])
		
if __name__ == "__main__":
	reducer = Reducer(sys.stdin)
	reducer.reduce()
