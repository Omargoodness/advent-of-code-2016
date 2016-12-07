import re

def check_abba(string):
    ''' (str) > bool
    Takes in a string and four-character sequence which consists of
    a pair of two different characters followed by the reverse
    of that pair. Return True if found.

    The pair of character must be unique.

    >>> check_abba('aaaa')
    False
    >>> check_abba('trzkfmggmbeaejun')
    True
    >>> check_abba('trzkfoooobeaejun')
    False
    '''

    for x in range(len(string)-3):
        if string[x] != string[x+1]: # skips if the next char is identical
            if (string[x] + string[x+1]) == (string[x+3] + string[x+2]):
                return True

    return False

def split_addresses(string):
    ip_addresses = re.split(r'\[.+?]', string)
    hypernets = re.findall(r'\[(.+?)]', string)

    return ip_addresses, hypernets

count = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        is_hypernet = False

        hypernets = re.findall(r'\[(.+?)]', line) # stores all hypernet strings
        ip_addresses = re.split(r'\[.+?]', line) # stores all valid ips


        for x in hypernets:
            if check_abba(x):
                is_hypernet = True

        if is_hypernet == False:
            for ip in ip_addresses:
                    if check_abba(ip):
                        count += 1
                        break

                


print(count)

''' 
# This returns a tuple of 2 lists that are in a tuple.
# First list is ip addresses and 2nd list is hypernets
def f():
    return [1, 2, 3], ["a", "b", "c"]

ip_addresses, hypernets = f() 
'''
