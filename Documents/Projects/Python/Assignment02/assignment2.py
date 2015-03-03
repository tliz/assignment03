
#Assignment two: 27 - Feb - 2015

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#List of only even numbers 

def even_numbers(my_list):
	even_list = []

	for number in my_list:
		if (number % 2) == 0:
			even_list.append(number)

	return even_list

print even_numbers(number_list)

#List of only odd numbers
def odd_numbers(my_list):
	odd_list = []

	for number in my_list:
		if number % 2 != 0:
			odd_list.append(number)
	return odd_list

print odd_numbers(number_list)

#Total list of even numbers in even list above
def sum_even_numbers(my_list):
	return sum(even_numbers(my_list))

print sum_even_numbers(number_list)

#Total of only odd numbers in odd list above
def sum_odd_numbers(my_list):
	return sum(odd_numbers(my_list))

print sum_odd_numbers(number_list)

#Find highest/biggest even number in even list above
def max_of_even_numbers(my_list):
	return max(even_numbers(my_list))

print max_of_even_numbers(number_list)

#Find highest/biggest odd number in odd list above
def max_of_odd_numbers(my_list):
	return max(odd_numbers(number_list))

print max_of_odd_numbers(number_list)