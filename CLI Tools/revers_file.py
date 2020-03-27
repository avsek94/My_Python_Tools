import argparse

# build the parse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')

args = parser.parse_args()

with open(args.filename) as f:
    lines =  f.readlines()
    lines.reverse()
    
    if args.limit:
        lines = lines[:args.limt]
    
    for line in lines:
        print(line.strip().upper()[::-1])
        
    

# parse the arguments




# read the file and, reverse the contents and print