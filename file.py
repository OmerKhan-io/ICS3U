"""
Author: Omer Khan
Student Number: 753619
Revision date: 16 June 2025
Program: Credit Card Report
Description: Report of all credit cards in the customer database that have expired or are about to expire.

VARIABLE DICTIONARY:
    data_file (str) - Name of the input data file ("data.dat")
    file_reader (file object) - File handle used for reading the input file
    content_lines (list) - Raw lines read from the input file (including header)
    header_line (str) - Header line from the file, to be excluded from processing
    card_data (list) - List of lists containing card info fields per line (excluding header)
    customer_names (list) - List of full names (first + last) of cardholders
    card_brands (list) - List of credit card types (e.g., VISA, Mastercard)
    card_numbers (list) - List of credit card numbers as strings
    exp_codes (list) - List of expiry dates as integers in YYYYMM format
    x (int) - Index variable used in loops for processing entries
    first_name (str) - First name extracted from a card entry
    last_name (str) - Last name extracted from a card entry
    full_name (str) - Concatenated full name (first + last) of cardholder
    card_type (str) - Credit card type extracted from a card entry
    card_number (str) - Credit card number extracted from a card entry
    expiry_date (int) - Expiry date formatted as integer YYYYMM
    validity (str) - Validation status string ("VALID" or "INVALID") from Luhn check
    status_msg (str) - String message indicating expiry status (e.g., "EXPIRED", "RENEW IMMEDIATELY")
"""

"""
Function to reverse a given string.
Parameters:
    string (str): Text input that needs to be reversed.
    reversed_str (str): Accumulates characters in reverse order.
    i (int): Index tracker used during reverse iteration.
Returns:
    str: The reversed version of the input string.
"""
def reverse(string):
    reversed_str = ""  # Initialize empty string to hold reversed result
    for i in range(len(string) - 1, -1, -1):  # Iterate backwards over string
        reversed_str += string[i]  # Append characters in reverse order
    return reversed_str  # Return the reversed string

"""
Function to validate a card number using the Luhn algorithm.
Parameters:
    card_number (str): Sequence of digits representing the credit card number.
    total (int): Sum accumulator used in validation logic.
    digit (int): Digit extracted and used in calculations.
    doubled (int): Doubled value of every second digit (adjusted if necessary).
    i (int): Loop control variable to determine digit position.
Returns:
    bool: True if the card number passes the Luhn check, False otherwise.
"""
def luhn_check(card_number):
    card_number = reverse(card_number)  # Reverse the card number string for processing
    total = 0  # Initialize total sum for checksum calculation
    for i in range(len(card_number)):  # Loop through each digit by index
        digit = int(card_number[i])  # Convert current character to integer
        if i % 2 == 1:  # Double every second digit starting from index 1
            doubled = digit * 2  # Double the digit
            if doubled > 9:  # If result is greater than 9, subtract 9
                doubled -= 9
            total += doubled  # Add adjusted doubled digit to total
        else:
            total += digit  # Add digit directly to total if not doubled
    return total % 10 == 0  # Return True if total modulo 10 is zero (valid)

"""
Function to ensure a single-digit month is formatted as two digits for date consistency.
Parameters:
    n (int): A date in the form YYYY[M], where M may be a single-digit month.
    n_str (str): String form of the date used for formatting.
Returns:
    int: Reformatted date in the proper 6-digit YYYYMM format.
"""
def format_expiry_date(n):
    n_str = str(n)  # Convert integer date to string
    return int(n_str[:4] + "0" + n_str[4:])  # Insert zero before single-digit month and convert back to int

"""
Merge sort function to sort multiple parallel arrays based on expiry dates.
Parameters:
    arr (list): List of expiry dates to sort.
    arr2 (list): Corresponding full names list.
    arr3 (list): Corresponding card numbers list.
    arr4 (list): Corresponding card types list.
    l (int): Left index for current sorting segment.
    r (int): Right index for current sorting segment.
"""
def merge_sort(arr, arr2, arr3, arr4, l, r):
    if l < r:  # Base case: continue if left index is less than right index
        m = l + (r - l) // 2  # Calculate midpoint of current segment
        merge_sort(arr, arr2, arr3, arr4, l, m)  # Recursively sort left half
        merge_sort(arr, arr2, arr3, arr4, m + 1, r)  # Recursively sort right half
        merge(arr, arr2, arr3, arr4, l, m, r)  # Merge sorted halves

"""
Helper function to merge two sorted halves of arrays in merge_sort.
Parameters:
    arr (list): Expiry dates array.
    arr2 (list): Full names array.
    arr3 (list): Card numbers array.
    arr4 (list): Card types array.
    l (int): Left index of first half.
    m (int): Middle index dividing halves.
    r (int): Right index of second half.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1  # Length of first half
    n2 = r - m  # Length of second half

    # Create temporary arrays for merging
    L = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2

    # Copy data to temporary arrays
    for i in range(n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]

    i = 0  # Initial index for left subarray
    j = 0  # Initial index for right subarray
    k = l  # Initial index for merged array

    # Merge temporary arrays back into original arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    # Copy remaining elements of left arrays, if any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copy remaining elements of right arrays, if any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Initialize list to store card data read from file (excluding header)
card_data = []

try:
    # Open the data file for reading
    file_handle = open("data.dat", "r")
    end_of_file = False  # Flag to detect end of file

    while not end_of_file:
        line = file_handle.readline().strip()  # Read line and remove whitespace
        end_of_file = (line == "")  # Check if line is empty, indicating EOF
        if not end_of_file:
            card_data.append(line.split(","))  # Split line by commas and append as list

    file_handle.close()  # Close the file after reading

except OSError:  # Handle OS errors such as file not found
    print("OSError")
except EOFError:  # Handle unexpected EOF errors
    print("EOFError")

# Remove header row from the data list
card_data.remove(card_data[0])

# Initialize lists for organized card information
full_names = []
card_types = []
card_numbers = []
expiry_dates = []

# Process each card entry and extract relevant fields
for x in range(len(card_data)):
    first_name = card_data[x][0]  # Extract first name
    last_name = card_data[x][1]   # Extract last name
    full_name = first_name + ' ' + last_name  # Concatenate full name
    card_type = card_data[x][2]   # Extract card type (e.g., VISA)
    card_number = card_data[x][3]  # Extract card number as string

    # Combine year and month parts of expiry date
    # Handle single-digit months by formatting with a leading zero
    if len(card_data[x][5] + card_data[x][4]) == 5:
        expiry_date = int(format_expiry_date(card_data[x][5] + card_data[x][4]))
    else:
        expiry_date = int(card_data[x][5] + card_data[x][4])

    # Append extracted data to respective lists
    full_names.append(full_name)
    card_types.append(card_type)
    card_numbers.append(card_number)
    expiry_dates.append(expiry_date)

# Sort all lists based on expiry dates using merge sort
merge_sort(expiry_dates, full_names, card_numbers, card_types, 0, len(expiry_dates) - 1)

# ANSI escape codes for colored output in terminal
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\u001b[32m"
RESET = "\033[0m"

# Display the credit card report with expiry and validation status
for x in range(len(expiry_dates)):
    # Validate card number using Luhn algorithm
    if luhn_check(card_numbers[x]):
        validity = "VALID"
    else:
        validity = "INVALID"

    # Print cardholder info with color-coded expiry warnings
    if expiry_dates[x] < 202505:  # Expired cards
        print(('%-37s %-15s %-20s %-10s %-25s %-5s') %
              (full_names[x] + ':', "\U0001F4B3" + " " + card_types[x],
               '#' + card_numbers[x], expiry_dates[x], RED + "EXPIRED" + RESET,
               " | " + GREEN + validity + RESET))
    elif expiry_dates[x] == 202505 or expiry_dates[x] == 202506:  # Renew immediately
        print(('%-37s %-15s %-20s %-10s %-25s') %
              (full_names[x] + ':', "\U0001F4B3" + " " + card_types[x],
               '#' + card_numbers[x], expiry_dates[x],
               YELLOW + "RENEW IMMEDIATELY" + RESET + " | " + GREEN + validity + RESET))
    else:
        # Cards not expired and not in immediate renewal period - no printout
        continue
