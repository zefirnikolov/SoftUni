word_input = input()

vowels_removed_list = [x for x in word_input if x != 'a' and x != 'o' and x != 'u' and x != 'e' and x != 'i']
removed_vowels_string = ''
for element in vowels_removed_list:
    removed_vowels_string += element
print(removed_vowels_string)
