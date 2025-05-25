# code for zigzag conversion of a given string

def zifzag_convert(s, num_rows, print_rows  = False):
    if num_rows == 1 or num_rows >= len(s):
        return s

    # Initialise rows
    rows = [''] * num_rows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        # Change direction
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    if print_rows:
        print("\n Zigzag pattern (Row by Row):")
        for i, row in enumerate(rows):
            print(f"Row {i + 1}: {row}")

    #final result by combining rows
    return ''.join(rows)

# Test Cases
s1 = "PAYPALISHIRING"
rows1 = 3
result1 = zifzag_convert(s1, rows1, print_rows = True)
print("\nFinal Zigzag Conversion Output : ", result1)

s2 = "HELLOZIGZAG"
rows2 = 4
result2 = zifzag_convert(s2, rows2, print_rows = True)
print("\nFinal zigzag conversion output : ", result2)
