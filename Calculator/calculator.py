import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, width=312, height=272.5, bg="grey")
        btns_frame.pack()

        buttons = [
            ("C", 1, 0), ("%", 1, 1), ("/", 1, 2), ("*", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
            ("0", 5, 0), (".", 5, 1)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.btn_click(x) if x not in ("=", "C") else self.btn_equal() if x == "=" else self.btn_clear()
            tk.Button(btns_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff" if text not in ("=", "C") else "#f44336" if text == "C" else "#4CAF50",
                      cursor="hand2", command=action).grid(row=row, column=col, padx=1, pady=1, columnspan=1 if text != "0" else 2, sticky="nsew")

        # Adjust grid weights
        for i in range(6):
            btns_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            btns_frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
