import hashlib

binary_input = '''
11001111101 01110110000 00000001010 11110010011
00101011011 10000101100 00010011101 11101001011
00101110110 11101011000 01111011011 11010000010
11010110011 10000001111 10000011010 10001000100
10101011100 01011101010 10001010100 11101010111
11111001101 10101111111 01001101111 001
'''

def binary_to_sha256(binary_string):
    binary_string = binary_string.replace('\n', '')
    binary_string = binary_string.replace(' ', '')
    hex_string = hex(int(binary_string, 2))[2:]
    binary_data = bytes.fromhex(hex_string)
    hashed_data = hashlib.sha256(binary_data).hexdigest()
    return hashed_data

hashed_value = binary_to_sha256(binary_input)
print("해시 값:", hashed_value)