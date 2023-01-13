import re

names = 'Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett'
search_pattern = r"\b[A-Z][a-z]+\ [A-Z][a-z]+\b"
matches = re.findall(search_pattern, names, re.UNICODE)  # Unicode - ASCII only - Flag!
print(' '.join(matches))  # Returns list

results = re.finditer(search_pattern, names)
for match in results:
    print(match.group(), end=" ")  # returns objects, which can be found with .group method.
    # If more groups use for ex.: group(2)
print()

first_occurrence = re.search(search_pattern, names)  # search method returns the 1st occurrence it detects
print(first_occurrence.group())

# Reuse the 1st group of a regex with \1 searching for exactly the same as in the 1st group.
