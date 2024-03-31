import tkinter as tk
from tkinter import messagebox
import hashlib


# GUI 창 그래픽 및 입력
class MnemonicGenerator:
    entry_grid = []  # 입력 창과 label을 관리하기 위한 grid

    def __init__(self):
        # PrivateKeyGenerator 클래스의 인스턴스 생성
        self.keygen = PrivateKeyGenerator()
        # Tkinter 루트 창 생성
        self.root = tk.Tk()
        self.root.title("Mnemonic Generator")  # GUI 창 제목 설정
        self.root.iconphoto(False, tk.PhotoImage(file="./bitcoin.png"))  # 아이콘 설정

        # 제목 label 생성
        label = tk.Label(self.root, text="11자리 이진수 24개를 입력하세요. (마지막은 3자리 이진수)")
        label.grid(row=0, column=0, columnspan=3)

        count = 0
        # 입력 창과 label을 grid에 배치
        for i in range(0, 16, 2):
            row = []
            for j in range(3):
                validate_input = self.root.register(self.validate_binary_input)
                entry = tk.Entry(self.root, validate='key', validatecommand=(validate_input, '%P'))
                entry.grid(row=i+1, column=j, padx=5)
                row.append(entry)
                
                numbering = f"{3*count+j+1}. "  # label 번호 부여
                entry_label = tk.Label(self.root, text=numbering)
                entry_label.grid(row=i+2, column=j, padx=5)
                row.append(entry_label)
                entry.bind('<KeyRelease>', lambda event, label=entry_label, number=numbering: self.on_entry_change(event, label, number))
            self.entry_grid.append(row)
            count += 1

        # 확인 버튼 생성
        self.submit_button = tk.Button(self.root, text="Checksum 계산", command=self.submit)
        self.submit_button.grid(row=20, column=1, pady=5)

    def run(self):
        self.root.mainloop()

    # 입력값이 이진수인지 확인하는 함수
    def validate_binary_input(self, new_value):
        for char in new_value:
            if char not in ('0', '1'):
                return False

        current_entry = self.root.focus_get()
        last_entry = self.entry_grid[7][4]
        if current_entry == last_entry:
            return len(new_value) <= 3

        return True

    # 이진수를 십진수로 변환하는 함수
    def binary_to_decimal(self, binary_str):
        decimal = int(binary_str, 2)
        return decimal

    # 입력값이 유효한지 확인하는 함수
    def check_input(self):
        for entry_row in self.entry_grid:
            for entry in entry_row:
                if isinstance(entry, tk.Entry):
                    if entry == self.entry_grid[7][4]:
                        if len(entry.get()) != 3: # 마지막은 3자리
                            return False
                    else:
                        if len(entry.get()) != 11: # 그외 11자리
                            return False
        return True

    # 입력값이 변경될 때 호출되는 함수
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

    # 확인 버튼 클릭 시 호출되는 함수
    def submit(self):
        if self.check_input():
            input_text = ""
            for entry_row in self.entry_grid:
                for entry in entry_row:
                    if isinstance(entry, tk.Entry):
                        input_text += entry.get()

            # 입력값의 hash값 계산
            hashed_value = self.keygen.binary_to_sha256(input_text)

            # SHA-256 hasing한 16진수 결과의 첫 두 자리를 이진수로 변환
            hex_string = hashed_value[:2]
            binary_string = bin(int(hex_string, 16))[2:]
            formatted_binary_string = format(int(binary_string, 2), '08b')

            # 마지막 입력값에 formatted_binary_string 이진수를 추가하여 24번째 니모닉 단어를 완성
            decimal = self.binary_to_decimal(self.entry_grid[7][4].get() + formatted_binary_string)
            self.last_entry_label.config(text='24.' + self.keygen.get_mnemonic_word(decimal))

        else:
            messagebox.showwarning("Error", "모든 칸에 이진수를 입력하세요.")


# 키 생성 클래스
class PrivateKeyGenerator:
    def __init__(self):
        # BIP-0039 단어장 로드
        self.load_bip_mnemonic()

    # 입력값의 이진수를 hash값으로 변환하는 함수
    def binary_to_sha256(self, binary_string):
        hex_string = hex(int(binary_string, 2))[2:]
        if len(hex_string) < 64:
            hex_string = hex_string.zfill(64)
        print(hex_string)
        binary_data = bytes.fromhex(hex_string)
        hashed_data = hashlib.sha256(binary_data).hexdigest()
        return hashed_data

    # BIP-0039 단어장 로드하는 함수
    def load_bip_mnemonic(self):
        with open("./bip-0039_english.txt", "r") as file:
            self.bip39_mnemonic = file.readlines()
        self.bip39_mnemonic = [line.strip() for line in self.bip39_mnemonic]

    # 십진수에 해당하는 단어 반환
    def get_mnemonic_word(self, number):
        return self.bip39_mnemonic[number]


# 메인 함수
def main():
    MnemonicGenerator().run()


# 메인 함수 실행
if __name__ == "__main__":
    main()
