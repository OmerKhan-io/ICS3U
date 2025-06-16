"""
Author : Omer Khan
Student Number: 753619
Revision date : 15 Jan 2025
Program : Credit Card Report
Description : Report of all credit cards in the customer database that have expired or are about to expire.

VARIABLE DICTIONARY :
    data_file: str - Name of the input file
    file_reader: file object - File handle
    customer_names: list - List of full names
    card_numbers: list - List of credit card numbers
    card_brands: list - List of credit card types
    exp_codes: list - List of expiry dates in YYYYMM integer format
    content_lines: list - Raw lines read from file
    header_line: str - Header line to be ignored
    report_file: file object - File handle for the output report
    status_msg: str - Message to indicate expiry status
"""

def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
    i = 0
    j = 0
    k = l
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
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1


# Open the input data file
data_file = "data (2).dat"
file_reader = open(data_file, 'r')

# Initialize lists for storing customer data
customer_names = []
card_numbers = []
card_brands = []
exp_codes = []

# Read all lines from the file
content_lines = file_reader.readlines()

# Remove the header line from data (assumed first line)
header_line = content_lines.pop(0)

# Parse each line into data fields
for entry in content_lines:
    # Split each entry by comma and unpack fields
    first_name, last_name, brand, number, exp_month, exp_year = entry.strip().split(',')

    # Combine first and last names
    full_name = first_name + ' ' + last_name

    # Append customer data to respective lists
    customer_names.append(full_name)
    card_brands.append(brand)
    card_numbers.append(number)

    # Ensure month is two digits by padding zero if needed
    if len(exp_month) == 1:
        exp_month = '0' + exp_month

    # Combine year and month to create integer YYYYMM expiry code
    expiry_code = exp_year + exp_month
    exp_codes.append(int(expiry_code))

# Close the input file after reading
file_reader.close()

# Sort all lists by expiry code using merge sort
mergeSort(exp_codes, customer_names, card_numbers, card_brands, 0, len(exp_codes) - 1)

# Open the output file for writing the report


# Iterate through all expiry dates to check if they need output
for i in range(len(exp_codes)):
    # Skip cards that expire June 2025 or later (no output needed)
    
    # Determine status message:
    # Expired if expiry before January 2025
    if exp_codes[i] < 202505:
        status_msg = "EXPIRED"
    elif exp_codes[i] == 202505 or exp_codes[i] == 202506:
        status_msg = "RENEW IMMEDIATELY"
    elif exp_codes[i] > 202506:
        continue


    # Print formatted info to console
    print("%-35s %-15s %-20s %-10s %-15s" % (
        customer_names[i] + ':', card_brands[i], '#' + card_numbers[i], exp_codes[i], status_msg))

