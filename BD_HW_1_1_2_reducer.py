#!/usr/bin/env python
'''
Abishek Ganesh
Quest 1 Part 2 :
2.Modify your map-reduce program (in 1) to display the number of times 
the word occurs in each file. A sample output is shown below:
'anger'	{'histories': 3, 'tragedies': 8}
'laugh'	{'comedies': 7, 'poems': 2, 'histories': 15}

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
				file_name = line.split('\t')[1]
				val = int(line.split('\t')[-1])
				yield key,file_name,val
			except:
				continue
			
	def reduce(self):
		word_dict={}
		for word,file_name, count in self:
			if word in word_dict:
				if file_name in word_dict[word]:
					word_dict[word][file_name]+=count
				else:
					 word_dict[word][file_name]=count
			else:
				word_dict[word]={file_name:count}
				
		for word in word_dict.keys():
			self.emit(word, word_dict[word])
		# For Part 1
		for word in word_dict.keys():
			self.emit(word, word_dict[word].keys())
		
if __name__ == "__main__":
	reducer = Reducer(sys.stdin)
	reducer.reduce()
