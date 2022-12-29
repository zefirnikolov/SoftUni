strings_input = input()
word = input()

palindromes = [x for x in strings_input.split() if x == x[::-1]]
palindromes_counter = palindromes.count(word)

print(palindromes)
print(f"Found palindrome {palindromes_counter} times")
