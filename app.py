import sys


def parse_csv(filename):
    header_columns = []
    rows = []

    file = open(filename, "r")

    # Read in the header and each line. Strip the newline.
    # Put each line into an array (split on the comma)
    header_columns = file.readline().strip().split(',')
    for line in file.readlines():
        rows.append(line.strip().split(','))
    
    file.close()

    return header_columns, rows


def write_csv(filename, header, rows):
    file = open(f"output/{filename}", "w")

    # Join the array of rows (strings) back into single
    # string with commas between each item. Add a newline at the end of each line.
    file.writelines(",".join(header) + "\n")
    file.writelines(",".join(r) + "\n" for r in rows)

    file.close()

def bubble_sort(index, rows):
    length = len(rows)
    sorted_rows = rows.copy()
    
    # Looping through each index of rows. 
    for a in range(length):
        # Comparing the current array and next array (arrays after length-a-1 have been sorted)
        for b in range(0, length-a-1):
            # Use the header index to compare the corresponding string in each row
            # If the string at b is less than its neighbor at b+1,
            # swap the two ("bubble" b+1 towards the top)
            if sorted_rows[b][index] < sorted_rows[b+1][index]:
                sorted_rows[b], sorted_rows[b+1] = sorted_rows[b+1], sorted_rows[b]

    return sorted_rows

if __name__== "__main__":
    sort_column = sys.argv[1]

    header, rows = parse_csv("input.csv")

    # Case insensitive search for which index the sort column is.
    # If sort_column is not in the header list, catch exception and exit (with humor)
    try:
        sort_index = [h.lower() for h in header].index(sort_column.lower())
    except ValueError as ve:
        print(f"\nYou and I both know '{sort_column}' is not a column in the header!")
        exit(1)

    sorted_rows = bubble_sort(sort_index, rows)
    write_csv("output.csv", header, sorted_rows)
