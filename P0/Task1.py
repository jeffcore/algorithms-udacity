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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# create set to store all unique numbers
num_set = set()

# add all numbers to set
for call in calls:
    num_set.add(call[0])
    num_set.add(call[1])

for text in texts:
    num_set.add(text[0])
    num_set.add(text[1])

print(f'There are {len(num_set)} different telephone numbers in the records.')
