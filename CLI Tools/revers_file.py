import argparse
import sys

# build the parse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
parser.add_argument('snippet', help='partial or (complete) string to search for in words')

args = parser.parse_args()


# parse the arguments

# try statement starts here to start the exception. 
try:
    f = open(args.filename)
    limit = args.limit

#here we are handling the trace back

except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
 
else:
    with f:
        lines =  f.readlines()
        lines.reverse()
        if args.limit:
            lines = lines[:args.limit]
        

# read the file and, reverse the contents in uppercase and print
        for line in lines:
            print(line.strip().upper()[::-1])
        