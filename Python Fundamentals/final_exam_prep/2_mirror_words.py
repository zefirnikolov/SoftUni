import re

text = input()
search_pattern = r'((\@|\#)([A-Za-z]{3,})\2)(\2[A-Za-z]{3,}\2)'

results = re.findall(search_pattern, text)
if not results:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(results)} word pairs found!")
    mirror_words = []
    for element in results:
        compare = ''
        upload_mirrors = ''
        if "#" in element[3]:
            compare = element[3].strip("#")
        if '@' in element[3]:
            compare = element[3].strip('@')
        if compare[::-1] == element[2]:
            upload_mirrors = element[2] + " <=> " + compare
            mirror_words.append(upload_mirrors)
    if not mirror_words:
        print("No mirror words!")
    else:
        print(f'The mirror words are:')
        print(', '.join(mirror_words))


