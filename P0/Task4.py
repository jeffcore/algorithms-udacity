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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# create set to store all sending phone numbers
outgoing_numbers = set()

# add all sender phone numbers from calls array
for call in calls:
    outgoing_numbers.add(call[0])

# remove receiving call phone numbers from outgoing_numbers set
for call in calls:
    if call[1] in outgoing_numbers:
        outgoing_numbers.remove(call[1])

# remove sending & receiving text phone numbers from outgoing_numbers set
for text in texts:
    if text[0] in outgoing_numbers:
        outgoing_numbers.remove(text[0])
    if text[1] in outgoing_numbers:
        outgoing_numbers.remove(text[1])

# numbers remaining in set will be telemarketers
print('These numbers could be telemarketers:')
for number in sorted(outgoing_numbers):
    print(number)

