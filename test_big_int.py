import unittest
from big_int import BigInt

class BigIntTest(unittest.TestCase):
    # Task test
    def test_xor(self):
        big_int_a = BigInt('51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4')
        big_int_b = BigInt('403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c')
        xor_big_int = big_int_a.XOR(big_int_b)
        self.assertEqual(xor_big_int.getHex(), '1182d8299c0ec40ca8bf3f49362e95e4ecedaf82bfd167988972412095b13db8')

    def test_add(self):
        big_int_a = BigInt('36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80')
        big_int_b = BigInt('70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb')
        sum_big_int = big_int_a.ADD(big_int_b)
        self.assertEqual(sum_big_int.getHex(), 'a78865c13b14ae4e25e90771b54963ee2d68c0a64d4a8ba7c6f45ee0e9daa65b')

    # def test_sub(self):
    #     big_int_a = BigInt('33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc')
    #     big_int_b = BigInt('22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03')
    #     xor_big_int = big_int_a.XOR(big_int_b)
    #     self.assertEqual(xor_big_int.getHex(), '10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9')

    # def test_mul(self):
    #     big_int_a = BigInt('7d7deab2affa38154326e96d350deee1')
    #     big_int_b = BigInt('97f92a75b3faf8939e8e98b96476fd22')
    #     xor_big_int = big_int_a.XOR(big_int_b)
    #     self.assertEqual(xor_big_int.getHex(), '4a7f69b908e167eb0dc9af7bbaa5456039c38359e4de4f169ca10c44d0a416e2')

    # General test
    # Test with zero value
    def test_empty_hex_string(self):
        big_int = BigInt('')
        self.assertEqual(big_int.getHex(), '0')
    
    # Test with an short string
    def test_short_hex_string(self):
        big_int = BigInt('1')
        self.assertEqual(big_int.getHex(), '1')

    # Test basic functionality
    def test_long_hex_string(self):
        big_int = BigInt('0123456789abcdef')
        self.assertEqual(big_int.getHex(), '123456789abcdef')

    # Test with leading zeros
    def test_zero_padding(self):
        big_int = BigInt('0000000000123456789abcdef')
        self.assertEqual(big_int.getHex(), '123456789abcdef')

    # We test the initialization of BigInt with one line, and then setting a new value via setHex
    def test_set_hex_twice(self):
        big_int = BigInt('0123456789abcdef')
        big_int.setHex('fedcba9876543210')
        self.assertEqual(big_int.getHex(), 'fedcba9876543210')
    
    def test_inv(self):
        big_int = BigInt('0123456789abcdef')
        inv_big_int = big_int.INV()
        self.assertEqual(inv_big_int.getHex(), 'fedcba9876543210')

    def test_or(self):
        big_int_a = BigInt('123456789abcdef')
        big_int_b = BigInt('fedcba987654321')
        or_big_int = big_int_a.OR(big_int_b)
        self.assertEqual(or_big_int.getHex(), 'fefcfef8fefcfef')

    def test_and(self):
        big_int_a = BigInt('123456789abcdef')
        big_int_b = BigInt('fedcba987654321')
        and_big_int = big_int_a.AND(big_int_b)
        self.assertEqual(and_big_int.getHex(), '121412181214121')

    def test_shift_r(self):
        big_int = BigInt('0123456789abcdef')
        shifted_big_int = big_int.shiftR(8)
        self.assertEqual(shifted_big_int.getHex(), '123456789abcd')

    def test_shift_l(self):
        big_int = BigInt('0123456789abcdef')
        shifted_big_int = big_int.shiftL(8)
        self.assertEqual(shifted_big_int.getHex(), '23456789abcdef00')

    # def test_mod(self):
    #     a = BigInt('123456789abcdef')
    #     b = BigInt('fedcba987654321')
    #     c = a.MOD(b)
    #     self.assertEqual(c.getHex(), '123456789abcdef')

    #     d = b.MOD(a)
    #     self.assertEqual(d.getHex(), 'd27f4d84e12a8e2')

    # def test_add_sub_edge_case(self):
    #     a = BigInt('ffffffff')
    #     b = BigInt('1')
    #     c = a.ADD(b)
    #     self.assertEqual(c.getHex(), '100000000')

    #     d = c.SUB(b)
    #     self.assertEqual(d.getHex(), 'ffffffff')

if __name__ == '__main__':
    unittest.main()