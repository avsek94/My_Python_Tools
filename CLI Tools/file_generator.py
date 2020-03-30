''' On this sciprt i am trying to create a test data,
which can be used for testing

'''
#import the random lib from python standard library which
import random 
# import os module to interact with operating system
import os
# import json lib to work with json files.
import json
import subprocess

# Variables defining to hold initial data 
count = int(os.getenv("FILE_COUNT") or 100)


words = [words.strip() for words in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content ={
        'topic':random.choice(words),
        'value': "%.2f" % amount
              }
    
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content,f)

    
    