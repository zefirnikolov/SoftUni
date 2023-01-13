# See all the flags at regex101.com - python - Quick Reference - Flags and open with Code generator
import re

text = 'MARIO is Python developer at a BioPharmacy, Mario\'s age is 32.'

result = re.findall(r"Mario", text)
print(result)
# USING A FLAG:
result = re.findall(r'Mario', text, re.IGNORECASE)
print(result)

result = re.search(r'''(^\w{5})# match 5 letters 
.+(\d{2}\.$)# match 2 digits and a dot''', text, re.X)  # re.X - allows comments in regex

print(result.group(1))
print(result.group(2))
