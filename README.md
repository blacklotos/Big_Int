# BigInt

BigInt is a custom data type in Python for handling large integers. This implementation supports various arithmetic and bitwise operations on large numbers. BigInt stores numbers as an array of unsigned 32-bit integers.

## Features

- Initialize BigInt from a hex string
- Convert BigInt back to a hex string
- Bitwise operations:
  - INV (bitwise inversion)
  - XOR (bitwise exclusive OR)
  - OR (bitwise OR)
  - AND (bitwise AND)
  - Shift left (shiftL)
  - Shift right (shiftR)
- Arithmetic operations:
  - ADD (addition)

## Usage

First, import the `BigInt` class from the `big_int` module:

from big_int import BigInt

Create BigInt objects by initializing them with hex strings:

a = BigInt("123456789abcdef")
b = BigInt("fedcba987654321")

Perform bitwise operations:

c = a.AND(b)
d = a.XOR(b)
e = a.shiftL(8)
f = a.shiftR(8)

Perform arithmetic operations:

g = a.ADD(b)

Get the hex string representation of a BigInt:

hex_string = a.getHex()

Testing
To run the test suite, execute the following command:

python -m unittest test_big_int.py
The test suite includes tests for initialization, bitwise operations, and arithmetic operations.