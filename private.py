import hashlib


binary_input = '''
00001111111 00001111111 00001111111 00001111111
00001111111 00001111111 00001111111 00001111111
00001111111 00001111111 00001111111 00001111111
00001111111 00001111111 00001111111 00001111111
00001111111 00001111111 00001111111 00001111111
00001111111 00001111111 00001111111 000
'''


class PrivateKeyGenerator:
    def __init__(self, binary_input):
        self.binary_input = binary_input
        self.pre_processing()
        self.load_bip_mnemonic()

    def binary_to_sha256(self, binary_string):
        hex_string = hex(int(binary_string, 2))[2:]
        if len(hex_string) < 64:
            hex_string = hex_string.zfill(64)
        print(hex_string)
        binary_data = bytes.fromhex(hex_string)
        hashed_data = hashlib.sha256(binary_data).hexdigest()
        return hashed_data

    def pre_processing(self):
        self.binary_input = self.binary_input.replace(' ', '')
        self.binary_input = self.binary_input.replace('\n', '')

    def load_bip_mnemonic(self):
        with open("./bip-0039_english.txt", "r") as file:
            self.bip39_mnemonic = file.readlines()
        self.bip39_mnemonic = [line.strip() for line in self.bip39_mnemonic]
    
    def get_private_key(self):
        # get hash value
        hashed_value = self.binary_to_sha256(self.binary_input)
        print("Hash value:", hashed_value)

        # complete private key
        hex_string = hashed_value[:2]
        self.binary_input += bin(int(hex_string, 16))[2:]

        # get bip39-mnemonic
        binary_array = [self.binary_input[i:i+11] for i in range(0, len(self.binary_input), 11)]
        decimal_list = [self.bip39_mnemonic[int(binary, 2)] for binary in binary_array]

        # print mnemonic codes
        print("Your mnemonic codes:")
        for i in range(0, len(decimal_list), 3):
            for j in range(i, min(i+3, len(decimal_list))):
                print("{:>10}".format(decimal_list[j]), end="")
            print()


def main():
    pkey = PrivateKeyGenerator(binary_input).get_private_key()
    print(pkey)


if __name__ == "__main__":
    main()