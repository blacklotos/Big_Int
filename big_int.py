import numpy as np

def _add_with_carry(a, b, carry):
    sum_ = a + b + carry
    carry_out = (sum_ > np.uint64(np.iinfo(np.uint64).max))  # Check if there's a carry
    if carry_out:
        sum_ -= np.uint64(np.iinfo(np.uint64).max) + 1  # Reduce sum by the maximum value of np.uint64 + 1
    print("a: {}, b: {}, carry: {}, sum: {}, carry_out: {}".format(a, b, carry, sum_, carry_out))
    return sum_, carry_out

class BigInt:
    def __init__(self, hex_string=''):
        self.data = np.array([], dtype=np.uint64)
        self.setHex(hex_string)

    def setHex(self, hex_string):
        hex_string = hex_string.lstrip('0')
        if len(hex_string) % 16 != 0:
            hex_string = hex_string.zfill(16 * (len(hex_string) // 16 + 1))
        chunks = [hex_string[i:i+16] for i in range(0, len(hex_string), 16)]
        self.data = np.array([int(chunk, 16) for chunk in chunks], dtype=np.uint64)

    def getHex(self):
        if not self.data.size:
            return "0"
        hex_chunks = [format(num, '016x') for num in self.data]
        hex_string = "".join(hex_chunks)
        return hex_string.lstrip("0")
    
    # Operations
    def INV(self):
        inv_data = np.bitwise_not(self.data)
        inv_hex = ''.join(format(num, '016x') for num in inv_data)
        return BigInt(inv_hex)
    
    def XOR(self, other):
        xor_data = np.bitwise_xor(self.data, other.data)
        xor_hex = ''.join(format(num, '016x') for num in xor_data)
        return BigInt(xor_hex)

    def AND(self, other):
        and_data = np.bitwise_and(self.data, other.data)
        and_hex = ''.join(format(num, '016x') for num in and_data)
        return BigInt(and_hex)

    def OR(self, other):
        or_data = np.bitwise_or(self.data, other.data)
        or_hex = ''.join(format(num, '016x') for num in or_data)
        return BigInt(or_hex)

    def shiftR(self, n):
        shift_r_data = np.right_shift(self.data, n)
        shift_r_hex = ''.join(format(num, '016x') for num in shift_r_data)
        return BigInt(shift_r_hex)

    def shiftL(self, n):
        shift_l_data = np.left_shift(self.data, n)
        shift_l_hex = ''.join(format(num, '016x') for num in shift_l_data)
        return BigInt(shift_l_hex)
    
    def ADD(self, other):
        max_data_size = max(self.data.size, other.data.size)
        result_data = np.zeros(max_data_size, dtype=np.uint64)
        carry = 0

        for i in range(max_data_size):
            a = self.data[i] if i < self.data.size else 0
            b = other.data[i] if i < other.data.size else 0
            sum_, carry = _add_with_carry(a, b, carry)
            result_data[i] = sum_

        if carry:
            result_data = np.append(result_data, carry)

        result_hex = ''.join(format(num, '016x') for num in result_data)
        return BigInt(result_hex)

    
    def SUB(self, other):
        if self < other:
            raise ValueError("Result of subtraction would be negative")

        max_data_size = max(self.data.size, other.data.size)
        result_data = np.zeros(max_data_size, dtype=np.uint64)
        carry = 0

        for i in range(max_data_size):
            a = self.data[i] if i < self.data.size else 0
            b = other.data[i] if i < other.data.size else 0
            sub_ = a - b - carry
            carry = 0 if a >= b + carry else 1
            result_data[i] = sub_ & 0xFFFFFFFFFFFFFFFF

        return BigInt(''.join(format(num, '016x') for num in result_data))

