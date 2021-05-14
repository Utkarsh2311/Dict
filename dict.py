import json
import os
from difflib import get_close_matches

dir=os.path.abspath(os.path.dirname(__name__))
data=json.load(open(dir+'/data/data.json'))

def dict(word):
	word=word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
		
		yn=input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead,Enter Y if yes or N if no:")
		if yn=='Y'or yn=='y':
			return data[get_close_matches(word,data.keys())[0]]
		elif yn!='Y' or yn!='y':
			return 'we didnt get your query ,please enter again'
		    

		else:return 'Word is not in the Dictionary'
	else:
		return 'Word is not in the Dictionary,please enter another word'

def out():
	word=input('Enter the word: ')
	output=dict(word)
	if type(output)==list:
		for i in output:
			print(i)
	else: print(output)

if __name__=='__main__':
	out()