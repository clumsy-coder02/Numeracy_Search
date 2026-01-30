print() # spacing
print("Command Line Numeracy Search")
print("\"Find certain numbers given a certain range\"")
print() # spacing

# list available
print("\nEnter 1 for:Even Numbers\nEnter 2 for:Odd Numbers"
      "\nEnter 3 for:Prime Numbers\nEnter 4 for:Composite Numbers\nEnter 5 for:Exit")
print() # spacing

# user selection
user_choice = int(input("What would you like to find? "))

# main function,the function to call first
def option_selection():
    if user_choice == 1: # call the even numbers func
        even_numbers()
    elif user_choice == 2: # call the odd numbers func
        odd_numbers()
    elif user_choice == 3: # call the prime numbers func
        prime_numbers()
    elif user_choice == 4: # call the composite numbers func
        composite_numbers()
    elif user_choice == 5: # call the exit func
        exit_program()

# functions
# even numbers function
def even_numbers():
    print() # spacing
    print("Finding even numbers:")
    print() # spacing

    print("\"Enter the range(lowest and highest number) e.g 0-10 (zero to ten)\"")
    print() # spacing
    # enter ranges
    lower_bound = int(input("Enter the lowest number: "))
    upper_bound = int(input("Enter the highest number: "))
    print() # spacing

    # storage for results
    even_numbers_list = []

    # find the even numbers
    # add 1 to upper_bound to include the highest number
    for number in range(lower_bound,upper_bound + 1, 1):
        if number % 2 == 0: # check if it's even
            even_numbers_list.append(number)
    
    print() # spacing
    # display the results
    message = print(f"Even numbers between {lower_bound} & {upper_bound}: {even_numbers_list}")
    print() # spacing
    return message

# odd numbers function
def odd_numbers():
    print() # spacing
    print("Finding odd numbers:")
    print() # spacing

    print("\"Enter the range(lowest and highest number) e.g 0-10 (zero to ten)\"")
    print() # spacing

    # enter ranges
    lower_bound = int(input("Enter the lowest number: "))
    upper_bound = int(input("Enter the highest number: "))
    print() # spacing

    # storage for results
    odd_numbers_list = []

    # find the odd numbers
    # add 1 to upper_bound to include the highest number
    for number in range(lower_bound,upper_bound + 1, 1):
        if number % 2 == 1: # check if it's odd
            odd_numbers_list.append(number)
    
    print() # spacing
    # display the results
    message = print(f"Odd numbers between {lower_bound} & {upper_bound}: {odd_numbers_list}")
    print() # spacing
    return message

# prime numbers function
def prime_numbers():
    print() # spacing
    print("Finding prime numbers:")
    print() # spacing

    print("\"Enter the range(lowest and highest number) e.g 0-10 (zero to ten)\"")
    print() # spacing

    # enter ranges
    lower_bound = int(input("Enter the lowest number: "))
    upper_bound = int(input("Enter the highest number: "))
    print() # spacing

    # storage for multiples
    multiple_list = []
    # storage for prime numbers
    prime_numbers_list = []

    # find the multiples for the numbers within the range
    for each_number in range(lower_bound, upper_bound + 1, 1):
        # multiply the number you're in from the ranges
        # by the numbers running from 1 to upper_bound
        for number in range(1, upper_bound + 1, 1):
            multiple = each_number * number
            # add the answers to a list
            multiple_list.append(multiple)
    
    # find prime numbers now
    # loop through the ranges again
    for prime_number in range(lower_bound, upper_bound + 1, 1):
        # check if the  number you're in appeared only 2 times in the multiples,
        # if so it's a prime number
        if multiple_list.count(prime_number) == 2:
            prime_numbers_list.append(prime_number)
    
    print() # spacing
    # display the results
    message = print(f"Prime numbers between {lower_bound} & {upper_bound}: {prime_numbers_list}")
    print() # spacing
    return message

# composite numbers function
def composite_numbers():
    print() # spacing
    print("Finding composite numbers:")
    print() # spacing

    print("\"Enter the range(lowest and highest number) e.g 0-10 (zero to ten)\"")
    print() # spacing

    # enter ranges
    lower_bound = int(input("Enter the lowest number: "))
    upper_bound = int(input("Enter the highest number: "))
    print() # spacing

    # storage for multiples
    multiple_list = []
    # storage for composite numbers
    composite_numbers_list = []

    # find the multiples for the numbers within the range
    for each_number in range(lower_bound, upper_bound + 1, 1):
        # multiply the number you're in from the ranges
        # by the numbers running from 1 to upper_bound
        for number in range(1, upper_bound + 1, 1):
            multiple = each_number * number
            # add the answers to a list
            multiple_list.append(multiple)

    # find composite numbers now
    # loop through the ranges again
    for composite_number in range(lower_bound, upper_bound + 1, 1):
        # check if the number you're in appeared more than 2 times in the multiples,
        # if so it's a composite number
        if multiple_list.count(composite_number) > 2:
            composite_numbers_list.append(composite_number)
    
    print() # spacing
    # display the results
    message = print(f"Composite numbers between {lower_bound} & {upper_bound}: {composite_numbers_list}")
    print() # spacing
    return message


# exit option function
def exit_program():
    # exit the program
    exit()


# what function to call first,
# at the start of the program
if __name__ == "__main__": # don't delete
    option_selection()

