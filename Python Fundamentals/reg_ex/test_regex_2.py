import re
# in text - always use the positive lookbehind - (?<=) ex.: (^|(?<=\s)) - looking if there is beginning or whitespace.
# positive lookahead - (?="enter search") - will look for it after the match. ($|(?=\s)) -  end or whitespace

# search is finding only the 1st possible match.
txt = "The rain in Spain The asd rain in Spain"

x = re.search('^The.*Spain', txt)  # this is finding all text because it's *
print(x)

x = re.findall('ain', txt)

print(x)

data = ['software', 'developer']
text = 'software is a set of instructions'

for pattern in data:
    if re.search(pattern, text):
        matched = re.search(pattern, text)
        print(matched.group())
    else:
        print('Not match')

# How to use .search method - regex exercise - problem number 6 - 2 - search method
