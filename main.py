import tkinter as tk
import hashlib


class MnemonicGenerator:
    entry_grid = []

    def __init__(self):
        self.keygen = PrivateKeyGenerator()
        self.root = tk.Tk()
        self.root.title("Mnemonic Generator")
        self.root.iconphoto(False, tk.PhotoImage(file="./bitcoin.png"))

        label = tk.Label(self.root, text="11자리 이진수 24개를 입력하세요. (마지막은 3자리 이진수)")
        label.grid(row=0, column=0, columnspan=3)

        count = 0
        for i in range(0, 16, 2):
            row = []
            for j in range(3):
                validate_input = self.root.register(self.validate_binary_input)
                entry = tk.Entry(self.root, validate='key', validatecommand=(validate_input, '%P'))
                entry.grid(row=i+1, column=j, padx=5)
                row.append(entry)
                
                numbering = f"{3*count+j+1}. "
                entry_label = tk.Label(self.root, text=numbering)
                entry_label.grid(row=i+2, column=j, padx=5)
                row.append(entry_label)
                entry.bind('<KeyRelease>', lambda event, label=entry_label, number=numbering: self.on_entry_change(event, label, number))
            self.entry_grid.append(row)
            count += 1

        self.submit_button = tk.Button(self.root, text="Checksum 계산", command=self.submit)
        self.submit_button.grid(row=20, column=0, columnspan=3)

        self.hash_label = tk.Label(self.root)
        self.hash_label.grid(row=22, column=0, columnspan=3, pady=2)

    def run(self):
        self.root.mainloop()

    def validate_binary_input(self, new_value):
        for char in new_value:
            if char not in ('0', '1'):
                return False

        current_entry = self.root.focus_get()
        last_entry = self.entry_grid[7][4]
        if current_entry == last_entry:
            return len(new_value) <= 3

        return True

    def binary_to_decimal(self, binary_str):
        decimal = int(binary_str, 2)
        return decimal

    def check_input(self):
        for entry_row in self.entry_grid:
            for entry in entry_row:
                if isinstance(entry, tk.Entry):
                    if entry == self.entry_grid[7][4]:
                        if len(entry.get()) != 3:
                            return False
                    else:
                        if len(entry.get()) != 11:
                            return False
        return True

    def on_entry_change(self, event, entry_label, numbering):
        binary_str = event.widget.get()
        if event.widget == self.entry_grid[7][4]:
            self.last_entry_label = entry_label
        if event.widget == self.entry_grid[7][4] and len(binary_str) > 3:
            return
        entry_label.config(text=numbering + binary_str)
        
        if len(binary_str) == 11:
            decimal = self.binary_to_decimal(binary_str)
            entry_label.config(text=numbering + self.keygen.get_mnemonic_word(decimal))
            event.widget.tk_focusNext().focus()

    def submit(self):
        if self.check_input():
            input_text = ""
            for entry_row in self.entry_grid:
                for entry in entry_row:
                    if isinstance(entry, tk.Entry):  # Entry 위젯인 경우에만 값을 읽어옴
                        input_text += entry.get()

            hashed_value = self.keygen.binary_to_sha256(input_text)
            self.hash_label.config(text=hashed_value)

            hex_string = hashed_value[:2]
            binary_string = bin(int(hex_string, 16))[2:]
            formatted_binary_string = format(int(binary_string, 2), '08b')
            print(formatted_binary_string)

            decimal = self.binary_to_decimal(self.entry_grid[7][4].get() + formatted_binary_string)
            self.last_entry_label.config(text='24.' + self.keygen.get_mnemonic_word(decimal))

        else:
            print('error')


class PrivateKeyGenerator:
    def __init__(self):
        self.load_bip_mnemonic()

    def binary_to_sha256(self, binary_string):
        hex_string = hex(int(binary_string, 2))[2:]
        if len(hex_string) < 64:
            hex_string = hex_string.zfill(64)
        print(hex_string)
        binary_data = bytes.fromhex(hex_string)
        hashed_data = hashlib.sha256(binary_data).hexdigest()
        return hashed_data

    def load_bip_mnemonic(self):
        with open("./bip-0039_english.txt", "r") as file:
            self.bip39_mnemonic = file.readlines()
        self.bip39_mnemonic = [line.strip() for line in self.bip39_mnemonic]

    def get_mnemonic_word(self, number):
        return self.bip39_mnemonic[number]
    

def main():
    MnemonicGenerator().run()


if __name__ == "__main__":
    main()