"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART ONE
import re

print(re.match('^\(080\)', '(080)'))

def get_code(number):
    """
    finds and returns area code in phone number
    """   
    if number[0] == '(':
        code =  re.match('^\(.*\)', number)
        return code[0]
    elif number[0:3] == '140':
        return number[:3]
    else:
        return number[:4]

def is_bangalore_code(phone):
    """
    returns boolean if number has a bangalore code (080)
    """
    if phone[:5] == '(080)':
        return True   
    else:
        return False

# create set to store all codes called by banglore numbers
area_codes = set()
total_sender_bang_calls = 0
total_reciever_bang_calls = 0
for call in calls:
    if is_bangalore_code(call[0]):
        total_sender_bang_calls += 1
        call1_code = get_code(call[1])
        # print(f'{call[1]} its code {call1_code}')
        if call1_code == '(080)':
            total_reciever_bang_calls += 1
        area_codes.add(call1_code)

print('The numbers called by people in Bangalore have codes:')
for code in sorted(area_codes):
    print(code)

print(f'{total_reciever_bang_calls/total_sender_bang_calls *100:.2f} percent of calls from fixed lines in Bangalore are calls to other' \
    ' fixed lines in Bangalore.')