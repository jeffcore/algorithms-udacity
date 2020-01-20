"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# dictinary to store { number : total_seconds}
longest_calls = {}

# iterate through all calls total up call time
for call in calls:
    if call[0] in longest_calls:
        longest_calls[call[0]] += int(call[3])
    else:
        longest_calls[call[0]] = int(call[3])

    if call[1] in longest_calls:
        longest_calls[call[1]] += int(call[3])
    else:
        longest_calls[call[1]] = int(call[3])

# iterate through dictionary to get longest call
total_time = 0
longest_number = ''
for k, v in longest_calls.items():
    if int(v) > total_time:
        total_time = int(v)
        longest_number = k

print(f'{longest_number} spent the longest time, {total_time} seconds, on the phone during September 2016.')
