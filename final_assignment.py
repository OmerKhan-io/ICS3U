Function to perform merge sort on two arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    r (int): Right index of the subarray.
"""
def mergeSort(arr, arr2, arr3, arr4, l, r):
    # Check if the subarray has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        # Avoids potential overflow for large values of l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)
        
"""
Function to merge two sorted arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    m (int): Middle index of the subarray.
    r (int): Right index of the subarray.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create temp arrays
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
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
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
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
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Open the file
file_name = "data.dat"
fh = open(file_name, 'r')


# Create lists for names, credit_card numbers, credit_cart types, and expiry dates
f_names = []
credit_cart types = []
credit_cart nums = []
expiry_dates = []

# Read all the lines in the file
line = fh.readlines();
# Exsempt the first line
# Remove first line from the list
first_line = lines.pop(0)

for x in lines:
    # Split each line into components
    given_name, surname, credit_card type, credit_card number, exp_mo, exp_yr = line.strip().split(',')
    # Add first and last name together
    name = given_name + ' ' + surname
    # Add name to names list
    names.append(name)
    # Add credit_card type to list
    credit_card types.append(credit_card type)
    # Add credit_card number to list
    credit_card nums.append(credit_card number)
    # Adds a leading zero to single digit month
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo
    # Adds month and year together into expiry_date
    expiry_date = exp_yr + exp_mo
    # Add expiry_date to list in type int
    expiry_dates.append(int(expiry_date))

    # Close the file
fh.close()
