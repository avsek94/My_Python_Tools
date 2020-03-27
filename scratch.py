#! usr/bin/env python3.7

message = input(f"Enter the message here:")
count =   int(input(f"Enter the number of times to display message:"))
#count1 = int(count)



#print(count1)

if count:
    count = int(count)
else:
    count = 1

def multi_echo(count, message):
    while 2 > 0 :
        print(message)
        count -= 1

multi_echo(message,count)
