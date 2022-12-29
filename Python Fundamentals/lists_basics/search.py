number_of_words_in_the_list_eq_loops = int(input())
word_check = input()

created_list = []
list_in_which_the_word_is_present = []

for _ in range(number_of_words_in_the_list_eq_loops):
    current_add = input()
    created_list.append(current_add)

for sentence_eq_element in created_list:
    if word_check in sentence_eq_element:
        list_in_which_the_word_is_present.append(sentence_eq_element)

print(created_list)
print(list_in_which_the_word_is_present)
