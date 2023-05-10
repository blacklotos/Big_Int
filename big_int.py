import numpy as np

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

    def INV(self):
        inv_data = np.bitwise_not(self.data)
        return BigInt(inv_data)

    def XOR(self, other):
        xor_data = np.bitwise_xor(self.data, other.data)
        return BigInt(xor_data)

    def OR(self, other):
        or_data = np.bitwise_or(self.data, other.data)
        return BigInt(or_data)

    def AND(self, other):
        and_data = np.bitwise_and(self.data, other.data)
        return BigInt(and_data)

    def shiftR(self, n):
        shifted_data = np.right_shift(self.data, n)
        return BigInt(shifted_data)

    def shiftL(self, n):
        shifted_data = np.left_shift(self.data, n)
        return BigInt(shifted_data)
    
    def ADD(self, other):
        result = BigInt()
        carry = 0
        max_len = max(len(self.data), len(other.data))

        for i in range(max_len):
            a = self.data[i] if i < len(self.data) else 0
            b = other.data[i] if i < len(other.data) else 0
            total = a + b + carry

            if total >= 0x100000000:
                carry = 1
                total -= 0x100000000
            else:
                carry = 0

            result.data = np.append(result.data, total)

        if carry > 0:
            result.data = np.append(result.data, carry)

        return result
