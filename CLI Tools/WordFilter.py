#import the argparse from the standard library
import argparse
import sys

# create a parser

parser = argparse.ArgumentParser(description="Search the words in any given files including a partial words")
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

# Add arguments to the parser

args = parser.parse_args()
snippet = args.snippet.lower()

# logics of how to read and computer 
# opens the file 
try:
    with open('/usr/share/dict/words') as f:
        words = f.readlines()

except FileNotFoundError as err:
    print(f'Error : {err}')
    sys.exit(1)
    
# Below are 2 twos to do this logic first one is with list comprehension and second is the standard
else:
    matches =print([word.strip() for word in words if snippet in word.lower()])

    '''
    for word in words:
        if snippet in word.lower():
            matches.append(word.strip())
    print(matches)    
    '''    
  


