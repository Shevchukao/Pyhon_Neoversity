for i in range(10):  # for loop itteration from 0 to 9
    print(
        f"int: {i:d}; hex: {i:#4x}; oct: {i:^#5o}; bin: {i:#<8b}; float: {i:>10f}; float_2: {i:5.2f}"
    )

"""

f-string with format specifiers: The text after the colon : inside the curly braces {} defines how the number should be formatted.

[d = decimal format[Base_10]], [#x = hexedecimal [Base_16]], [#o = octal [Base_8]],
[#b = binary[Base_2]], [f = float[floating-point number with 6 decimal places by default]], [.2f = float[floating-point number with 2 decimal places]], 
nuber before format say about spaces for symbols for this format, "<" for left alignment, ">" for right alignment, "^" for center allignment.

int: 0; hex:  0x0; oct:  0o0 ; bin: 0#######; float:   0.000000; float_2:  0.00
int: 1; hex:  0x1; oct:  0o1 ; bin: 1#######; float:   1.000000; float_2:  1.00
int: 2; hex:  0x2; oct:  0o2 ; bin: 10######; float:   2.000000; float_2:  2.00
int: 3; hex:  0x3; oct:  0o3 ; bin: 11######; float:   3.000000; float_2:  3.00
int: 4; hex:  0x4; oct:  0o4 ; bin: 100#####; float:   4.000000; float_2:  4.00
int: 5; hex:  0x5; oct:  0o5 ; bin: 101#####; float:   5.000000; float_2:  5.00
int: 6; hex:  0x6; oct:  0o6 ; bin: 110#####; float:   6.000000; float_2:  6.00
int: 7; hex:  0x7; oct:  0o7 ; bin: 111#####; float:   7.000000; float_2:  7.00
int: 8; hex:  0x8; oct: 0o10 ; bin: 1000####; float:   8.000000; float_2:  8.00
int: 9; hex:  0x9; oct: 0o11 ; bin: 1001####; float:   9.000000; float_2:  9.00
  
"""
