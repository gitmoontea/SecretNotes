import tkinter.messagebox
import base64

class EncryptWork():
    def __init__(self, ench_data: dict, filename: str):
        self.title = ench_data["title"]
        self.text = ench_data["text"].strip()
        self.masterkey = ench_data["masterkey"].strip()
        self.filename = filename
        self.mkey_ord_list = [ord(i) for i in self.masterkey]

    def saveEncryptMessage(self):
        char_list = []
        ord_list = []
        for (index, val) in enumerate(self.text):
            key_step = index % len(self.mkey_ord_list)
            ord_enc_letter = ord(val) + self.mkey_ord_list[key_step]
            char_list.append(chr(ord_enc_letter))
            ord_list.append(ord_enc_letter)

        self.text = "".join(char_list)
        enchMessage = base64.urlsafe_b64encode(self.text.encode()).decode()

        with open(f'{self.filename}.txt', 'a', encoding='utf-8') as f:
            f.write(self.title + "\n")

        with open(f'{self.filename}.txt', 'a') as f:
            f.write(enchMessage)
            tkinter.messagebox.showinfo("Kayıt", "Mesaj şifrelenmiş olarak kayıt edildi.")

        with open(f'{self.filename}.txt', 'a', encoding='utf-8') as f:
            f.write("\n")



def decrypt_process(masterEntry, textEntry) -> str:
    mkey = masterEntry.get().strip()
    text = textEntry.get("1.0", tkinter.END).strip()
    mkey_ord_list = [ord(i) for i in mkey]
    original_text_list = []
    dec_text = base64.urlsafe_b64decode(text).decode().strip()

    for (index, val) in enumerate(dec_text):
        key_step = index % len(mkey_ord_list)
        ord_value = ord(val) - mkey_ord_list[key_step]
        original_text_list.append(chr(ord_value))

    original_text = "".join(original_text_list)


    return original_text