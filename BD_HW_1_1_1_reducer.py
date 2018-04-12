#!/usr/bin/env python


'''
Abishek Ganesh
Quest 1 Part 1 :
1.Write a map-reduce program that creates an
inverted list of words and the files that contain them. That is, for each word,
you will display a list of filesthat contain that word. A sample output is given below:
'anger'	['histories', 'tragedies']
'laugh'	['comedies', 'poems', 'histories']

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
				key = line.split('\t')[0]
				file_name = line.split('\t')[1].strip()
				yield key,file_name
			except:
				continue
			
	def reduce(self):
		word_dict={}
		for word,file_name in self:
			if word in word_dict:
				word_dict[word].append(file_name)
			else:
				word_dict[word]=[file_name]

		# For Part 1
		for word in word_dict.keys():
			self.emit(word, set(word_dict[word]))
		
if __name__ == "__main__":
	reducer = Reducer(sys.stdin)
	reducer.reduce()
