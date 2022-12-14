number_of_pages_from_book = int(input())
pages_read_for_1_hour = int(input())
days_needed_to_read_the_book = int(input())

sum_of_time_for_reading = number_of_pages_from_book / pages_read_for_1_hour
hours_needed_for_day = sum_of_time_for_reading / days_needed_to_read_the_book

print(int(hours_needed_for_day))
