import tkinter as tk
from tkinter import ttk
from currency import Currency


VALID_CODES = ["BRL", "EUR", "USD"]


class CurrencyWidget(tk.Widget):
    def __init__(self, master, **kw) -> None:
        super().__init__(master, "ttk::frame", kw)

        self.currency_entry =  ttk.Entry(self)
        self.currency_entry.pack(side='left')
        self.top_box = ttk.Combobox(self, values=VALID_CODES)
        self.top_box.pack(side='left')

    def get(self):
        return Currency(self.currency_entry.get(), self.top_box.get())


def main():
    # def convert():
    #     value = currency_entry.get()
    #     code = top_box.get()
    #     currency = Currency(value, code)
    #     to_code = bot_box.get()
    #     converted = currency.convert(to_code)
    #     conv_label['text'] = f"{converted.value:.2f}"
    #     print("TESTE, FUNCIONOU")

    def convert():
        currency = currency_widget.get()
        to_code = bot_box.get()
        converted = currency.convert(to_code)
        conv_label['text'] = f"{converted.value:.2f}"
        print("TESTE, FUNCIONOU")

    window = tk.Tk()
    window.title("Conversor de Moedas")

    # Widgets
    # top_frame = ttk.Frame(window, padding=10)
    # top_frame.pack()
    # currency_entry =  ttk.Entry(top_frame)
    # currency_entry.pack(side='left')
    # top_box = ttk.Combobox(top_frame, values=VALID_CODES)
    # top_box.pack(side='left')
    currency_widget = CurrencyWidget(window, padding="10")
    currency_widget.pack()

    bottom_frame = ttk.Frame(window)
    bottom_frame.pack()
    conv_label = ttk.Label(bottom_frame, text="...")
    conv_label.pack(side='left')
    bot_box = ttk.Combobox(bottom_frame, values=VALID_CODES)
    bot_box.pack(side='left')

    button = ttk.Button(window, text="Converter", command=convert)
    button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
    print("Encerrou")
