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

# Merge Sort Function to sort expiry dates and corresponding info
def mergeSort(arr, arr2, arr3, arr4, left, right):
    if left < right:
        mid = left + (right - left) // 2  # Find midpoint to split array
        mergeSort(arr, arr2, arr3, arr4, left, mid)        # Recursively sort left half
        mergeSort(arr, arr2, arr3, arr4, mid + 1, right)   # Recursively sort right half
        merge(arr, arr2, arr3, arr4, left, mid, right)     # Merge sorted halves

# Merge helper function merges two sorted subarrays into one
def merge(arr, arr2, arr3, arr4, left, mid, right):
    size1 = mid - left + 1  # Size of left subarray
    size2 = right - mid     # Size of right subarray

    # Create temporary lists to hold values for merging
    L = [0] * size1
    L2 = [0] * size1
    L3 = [0] * size1
    L4 = [0] * size1

    R = [0] * size2
    R2 = [0] * size2
    R3 = [0] * size2
    R4 = [0] * size2

    # Copy data to left subarrays
    for i in range(size1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
        L3[i] = arr3[left + i]
        L4[i] = arr4[left + i]

    # Copy data to right subarrays
    for j in range(size2):
        R[j] = arr[mid + 1 + j]
        R2[j] = arr2[mid + 1 + j]
        R3[j] = arr3[mid + 1 + j]
        R4[j] = arr4[mid + 1 + j]

    i = j = 0  # Initial indexes for left and right subarrays
    k = left   # Initial index for merged array

    # Merge the temp arrays back into original arrays
    while i < size1 and j < size2:
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

    # Copy remaining elements of left subarrays, if any
    while i < size1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarrays, if any
    while j < size2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open the input data file
data_file = "data.dat"
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
report_filename = "output.txt"
report_file = open(report_filename, "w")

# Iterate through all expiry dates to check if they need output
for i in range(len(exp_codes)):
    # Skip cards that expire June 2025 or later (no output needed)
    if exp_codes[i] >= 202506:
        continue

    # Determine status message:
    # Expired if expiry before January 2025
    if exp_codes[i] < 202501:
        status_msg = "EXPIRED"
    else:
        # Near expiry cards between Jan and May 2025
        status_msg = "RENEW IMMEDIATELY"

    # Print formatted info to console
    print("%-35s %-15s %-20s %-10s %-15s" % (
        customer_names[i] + ':', card_brands[i], '#' + card_numbers[i], exp_codes[i], status_msg))

    # Write formatted info to output report file
    report_file.write("%-35s %-15s %-20s %-10s %-15s\n" % (
        customer_names[i] + ':', card_brands[i], '#' + card_numbers[i], exp_codes[i], status_msg))

# Close the output report file after writing
report_file.close()

# Confirm output file location to user
print("\nOutput sent to %s" % report_filename)
